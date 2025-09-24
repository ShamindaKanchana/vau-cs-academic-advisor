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