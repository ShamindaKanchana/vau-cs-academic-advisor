from sqlalchemy import Column, Integer, String, Float, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Module(Base):
    __tablename__ = "modules"
    id = Column(Integer, primary_key=True, index=True)
    course_code = Column(String(30), index=True)
    course_title = Column(String(30), index=True)
    year = Column(Integer)
    semester = Column(Integer)
    description = Column(String(200))
    credit_value = Column(Integer)
    


    def __repr__(self):
        return f"<Module(name={self.name}, year={self.year}, semester={self.semester}, description={self.description})>"
    
    