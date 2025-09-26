def user_input_handler_prompt(user_input: str):
    INPUT_HANDLER_PROMPT = f"""
    You are an agent who able to identify the user requirements and based on that you will return the structured format. FOr i case of to determine whether the user request 
    is Subject content ot result based , the result_based requests also with the subjets and grades both but the Subject content based
    only with the subjects. In user input there no any subject/module names mentioned then it will belongs  to below 4 general_information category.
    In a case that if user ask any non academic related questions which like a stuff not based with academic then it belongs to shit category.
    
    . So the user input is " {user_input}" and you need to  return the output based on the below list contain types:
    1. result_based
    2. Subject_content_based
    3. academic_advice
    4. general_information
    5. shit
    """
    return INPUT_HANDLER_PROMPT

def subject_content_based_prompt(user_input: str):
    SUBJECT_CONTENT_BASED_PROMPT = f""" You are an agent who able to find the information from the database based on the user input. 
    Below tasks you need to complete:
    1. Identify the subjects which are need to know for the user 

    the user input is {user_input}
   
 """
    return SUBJECT_CONTENT_BASED_PROMPT


#If the user input is result_based then this state will be triggered
def result_based_infor_extraction_prompt(user_input: str):
    RESULT_BASED_INFORMATION_EXTRACTION_PROMPT = f""" The given user input you need to extract the subject name and grade 
    with maintaining the order. 
    
    the user input is {user_input}
    
    
    
    
    """
    return RESULT_BASED_INFORMATION_EXTRACTION_PROMPT


#After resault xtraction the input comes to this state
from states import SubjectGrade
def results_info_retrieval_prompt(subjects_grades: list[SubjectGrade],current_task: str):
    RESULTS_INFO_RETRIEVAL_PROMPT = f""" You are an advicer who able to provide valueble information to the students who provide their subject grades. 
    You need look at the results provided and based on that you need to give advice or information to the student. You also can  access the database if you need 
    any information need from that. (Each of module description,credit_value info). So seeing the contents provide most valueble brief information to the student.
    
    The subjects grades are {subjects_grades} 
    The current task is {current_task}
    

    """
    return RESULTS_INFO_RETRIEVAL_PROMPT
    

def subject_information_retrieval_prompt(subjects: list[str],userinput: str):
    SUBJECT_INFORMATION_RETRIEVAL_PROMPT = f""" You are an agent who able to find the information from the 
    database based on the user subjects. 
    the subjects are {subjects} 
    User wants to know {userinput}.

    You have resonsibility to understand the user need from his states and get the user needs based on that
    """
    return SUBJECT_INFORMATION_RETRIEVAL_PROMPT
    

def academic_advice_ready_prompt(user_input: str):
    ACADEMIC_ADVICE_READY_PROMPT = f"""For the requested input you need to identify the subjects that user have
     doubts and if the inut is more large then can make sub topics/doubts
    
    the user input is {user_input}
    """
    return ACADEMIC_ADVICE_READY_PROMPT    


def general_information_prompt(user_input: str):
    GENERAL_INFORMATION_PROMPT = f""" Based on the user input provide the information user need
    
    the user input is {user_input} """

    return GENERAL_INFORMATION_PROMPT    


def final_user_response_prompt(user_input: str,final_state: str):
    FINAL_USER_RESPONSE_PROMPT = f"""
    You are an agent who can provide the better human reponse based on the user input and the states until reach the goal. 
    We having the states since the user given the input and until reach the expected results. Normally the found result will exist in the 
    last state. SO I think when seeing the states results yu can identify the user needs because  you also have the user entered input. 
    
    Your task is to provide the final response to the user.
    
    the user input is:  {user_input} and 
    
    states until reach the final state: {final_state}




    So remind if user input type {user_input.type}==shit  then you need to provide the final response 'I'm sorry, but I can't assist with that shit.'
    """
    return FINAL_USER_RESPONSE_PROMPT

