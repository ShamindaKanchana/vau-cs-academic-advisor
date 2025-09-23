def user_input_handler_prompt(user_input: str):
    INPUT_HANDLER_PROMPT = f"""
    You are an agent who able to identify the user requirements and based on that you will return the structured format. So the 
    user input is {user_input} and you need to  return the output based on the below list contain types:
    1. result_based
    2. Subject_content_based
    3. academic_advice
    """
    return INPUT_HANDLER_PROMPT

def subject_content_based_prompt(user_input: str):
    SUBJECT_CONTENT_BASED_PROMPT = f""" You are an agent who able to find the information from the database based on the user input. 
    Below tasks you need to complete:
    1. Identify the subjects which are need to know for the user 

    the user input is {user_input}
   
 """
    return SUBJECT_CONTENT_BASED_PROMPT



def result_based_infor_extraction_prompt(user_input: str):
    RESULT_BASED_INFORMATION_EXTRACTION_PROMPT = f""" The given user input you need to extract the subject name and grade 
    with maintaining the order. 
    
    the user input is {user_input}
    
    
    
    
    """
    return RESULT_BASED_INFORMATION_EXTRACTION_PROMPT
    

def subject_information_retrieval_prompt(subjects: list[str],userinput: str):
    SUBJECT_INFORMATION_RETRIEVAL_PROMPT = f""" You are an agent who able to find the information from the database based on the user subjects. 
    the subjects are {subjects} 
    User wants to know {userinput}.

    You have resonsibility to understand the user need from his states and get the user needs based on that
    """
    return SUBJECT_INFORMATION_RETRIEVAL_PROMPT
    