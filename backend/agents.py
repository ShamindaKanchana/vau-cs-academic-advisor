from states import UserInput,SubjectContentBased,ResultBased,ResultsInfoRetrieval,SubjectGrade,AcademicAdvice_ready,Final_user_response,Shit

from langchain_google_genai import ChatGoogleGenerativeAI
from prompts import user_input_handler_prompt,subject_content_based_prompt,subject_information_retrieval_prompt,result_based_infor_extraction_prompt,results_info_retrieval_prompt,academic_advice_ready_prompt,general_information_prompt,final_user_response_prompt
from langchain_core.prompts import ChatPromptTemplate
import os 

llm = ChatGoogleGenerativeAI(google_api_key=os.getenv("GEMINI_API_KEY"), model="gemini-2.0-flash-exp")




def user_input_handler(state: dict) -> dict:
    """Identify user requirements and return structured format"""
    # Get user input from state
    user_input = state.get("user_input")
    if not user_input:
        raise ValueError("No user input provided in state")
    
    # Process the input
    response = llm.with_structured_output(UserInput).invoke(
        user_input_handler_prompt(user_input)
    )
    
    if response is None:
        raise ValueError("User input handler failed to return a response")
        
    print("\n\nAfter finishing the user input handler (first step) ...\n\n",response,"\n\n")
    return {
        **state,  # Include all previous state
        'user_input': user_input,  # Store the raw input
        'user_input_handler': response  # Store the processed response
    }



# def subject_content_based(state:dict)->dict:
#      user_input: UserInput = state["user_input_handler"]
#      response=llm.with_structured_output(SubjectContentBased).invoke(subject_content_based_prompt())
#      if response is None:
#         raise ValueError("Subject content based failed to return a response")
#      print(response)
#      return {'subject_content_based':response}

def subject_content_based(state: dict) -> dict:
    # Get the processed user input from the previous state
    user_input_handler = state.get("user_input_handler")
    if not user_input_handler:
        raise ValueError("No processed user input found in state. Make sure user_input_handler runs first.")
    
    # Get the raw user input for the prompt
    user_input = state.get("user_input", "")
    
    # Generate the response
    response = llm.with_structured_output(SubjectContentBased).invoke(
        subject_content_based_prompt(user_input)
    )
    
    if response is None:
        raise ValueError("Subject content based failed to return a response")
        
    print("After finishing the subject content based (second step) based on the decison of user input...\n\n",response,"\n\n")
    
    # Return the updated state with the new response
    return {
        **state,  # Include all previous state
        "subject_content_based": response
    }

def result_based_infor_extraction(state: dict) -> dict:
    extracted_data=llm.with_structured_output(ResultBased).invoke(result_based_infor_extraction_prompt(state["user_input"]))   
    if extracted_data is None:
        raise ValueError("Result based information extraction failed to return a response")
    

    print("\n\nAfter finishing the result based information extraction (second step) based on the decison of user input...\n\n",extracted_data,"\n\n")
    return {
        **state,
        "result_based_infor_extraction": extracted_data
    }   

from database_supporter import DatabaseRetriever

def results_info_retrieval(state: dict) -> dict:
    
    final_info_list=[]
    print("\n\nAfter finishing the results extraction info retrieval (third step)... \n\n")
    print("###############################################\n\n")
    rounds=len(state["result_based_infor_extraction"].task_list)
    for i in range(rounds):
        print("Starting round ",i+1,"__________________________________________________________________\n\n")
        task_list=state["result_based_infor_extraction"].task_list
        subject_grades=state["result_based_infor_extraction"].subject_grades
        current_task=task_list[i]
        print("Current task  ",current_task,"processing...\n")
        database_request_query=results_info_retrieval_prompt(subject_grades,current_task)
        final_info=DatabaseRetriever(["modules"]).query(database_request_query)
        print("Result provded from llama index for current task:\n\n",final_info,"\n\n")
        print("__________________________________________________________________\n\n")
        
        print("###################################################\n\n")
        
        if final_info is None:
            raise ValueError("Results information retrieval failed to return a response")
        final_info_list.append(final_info)
        print("Final info list:",final_info_list,"\n\n")

    return {
        **state,
        "results_info_retrieval": final_info_list
    }



def subject_information_retrieval(state: dict) -> dict:
    retriever = DatabaseRetriever(["modules"])
    
    print("States ##########################",str(state))
    prompt=subject_information_retrieval_prompt(state["subject_content_based"].subjects,str(state["user_input"]))
    #print("User prompt is like :",prompt,"\n")

    user_info=retriever.query(prompt,raw=True)

    print("\n\nAfter finishing the subject information retrieval (third step)...  \n\n",user_info,"\n\n")
    user_info_=""
    if not user_info or 'result' not in user_info or not user_info['result']:
        print("\n....................No results found in database\n")
        user_info_ = "I couldn't find any information about the requested module. Could you please provide more details or check the module name?"
    else:
        user_info_ = user_info['result']
    return {
        **state,
        "subject_information_retrieval": user_info_
    }


def academic_advice_ready(state: dict) -> dict:
    needed_info=llm.with_structured_output(AcademicAdvice_ready).invoke(academic_advice_ready_prompt(state["user_input"]))
    if needed_info is None:
        raise ValueError("Academic advice ready failed to return a response")
    print("\n\nUser input based on the academic advice so go with academic based state... \n\n")
    print("Academic advice ready state:",needed_info,"\n\n")
    return {
        **state,
        "academic_advice_ready": needed_info
    }

        

    
def general_information_provider(state: dict) -> str    :
    retriever = DatabaseRetriever(["modules"])
    general_info=retriever.query(general_information_prompt(state["user_input"]),raw=True)
    if general_info is None:
        raise ValueError("General information provider failed to return a response")
    print("\n\nAfter finishing the general information provider (second step)...  \n\n",general_info,"\n\n")
    return general_info['result']
            





def final_user_response(state: dict) -> str:
    user_input=state["user_input"]
    states=str(state)
    print("Entering to final state..................\n\n")
    
    final_response=llm.with_structured_output(Final_user_response).invoke(final_user_response_prompt(user_input,states))
    if final_response is None:
        raise ValueError("Final user response failed to return a response")
    print("\n\nAfter making the cleaned reponse###############  \n\n",final_response,"\n\n")


    return final_response.final_response

def shit_manager(state: dict) -> str:
    return "Dont ask  shitty questions"   