from sqlmodel import SQLModel, Field, create_engine,Session
from typing import Optional
from faker import Faker

class Project(SQLModel, table=True):
    __tablename__ = "projects"
    id:Optional[int] = Field(default=None, primary_key=True)
    rubrique: str
    name_project: str
    image: str
    rendu: str

