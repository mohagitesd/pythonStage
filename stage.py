from sqlmodel import SQLModel, Field, create_engine,Session
from typing import Optional
from faker import Faker

class Stage(SQLModel, table=True):
    __tablename__ = "stages"
    id:Optional[int] = Field(default=None, primary_key=True)
    poste: str
    entreprise: str
    expedition: str
    url: Optional[str] = None

def fake_stage():
    fake = Faker("fr_FR")
    return Stage(
        poste = fake.job(),
        entreprise = fake.company(),
        expedition = fake.date_this_month().isoformat(),
        url = fake.url(),
    )