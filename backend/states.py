from typing import Optional
from pydantic import BaseModel,Field


class UserInput(BaseModel):
    type: str = Field(..., description="Identify the type of user input")
    


class SubjectContentBased(BaseModel):
    subjects: list[str] = Field(..., description="List of subjects")





from typing import Dict

class SubjectGrade(BaseModel):
    subject: str = Field(..., description="Subject name")
    grade: str = Field(..., description="Grade")

class ResultBased(BaseModel):
    subject_grades: list[SubjectGrade] = Field(
        ...,
        description="List of subject names and their respective grades "
    )
    task_list: list[str] = Field(..., description="List of tasks that need to complete to give decision to user")



class ResultsInfoRetrieval(BaseModel):
    results_info: list[str] = Field(..., description="Based on the results and the task provide valuble information")


class AcademicAdvice_ready(BaseModel):
    subjects: list[str] = Field(..., description="List of subjects")
    doubts_topics: list[str] = Field(..., description="List of doubts  or topics the student having for some area. If user have more doubts or topics like paragraph of different things to ask then you can list over those else you can get as single topic or doubt.")


class Final_user_response(BaseModel):
    final_response: str = Field(..., description="Final response to user")