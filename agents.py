from states import UserInput,SubjectContentBased,ResultBased

from langchain_google_genai import ChatGoogleGenerativeAI
from prompts import user_input_handler_prompt,subject_content_based_prompt,subject_information_retrieval_prompt,result_based_infor_extraction_prompt
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
        
    print(response)
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
        
    print(response)
    
    # Return the updated state with the new response
    return {
        **state,  # Include all previous state
        "subject_content_based": response
    }

def result_based_infor_extraction(state: dict) -> dict:
    extracted_data=llm.with_structured_output(ResultBased).invoke(result_based_infor_extraction_prompt(state["user_input"]))   
    if extracted_data is None:
        raise ValueError("Result based information extraction failed to return a response")
    print(extracted_data)
    return {
        **state,
        "result_based_infor_extraction": extracted_data
    }   
    


from database_supporter import DatabaseRetriever
def subject_information_retrieval(state: dict) -> dict:
    retriever = DatabaseRetriever(["modules"])
    
    print("States ##########################",str(state))
    prompt=subject_information_retrieval_prompt(state["subject_content_based"].subjects,str(state["user_input"]))
    #print("User prompt is like :",prompt,"\n")
    user_info=retriever.query(prompt)
    print(user_info)
    return {
        **state,
        "subject_information_retrieval": user_info
    }

    
