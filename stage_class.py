from sqlmodel import SQLModel, Field, create_engine,Session
from typing import Optional,List
from faker import Faker

from database import get_session
from sqlmodel import select

class Stage(SQLModel, table=True):
    __tablename__ = "stages"
    id:Optional[int] = Field(default=None, primary_key=True)
    poste: str
    entreprise: str
    expedition: str
    url: Optional[str] = None


    @classmethod
    def get_all(cls) -> List[dict]:
        with get_session() as session:
            statement = select(cls)
            results = session.exec(statement).all()
            return [  stage.model_dump() for stage in results  ]

    @classmethod
    def get_one(cls, id: int) -> Optional[dict]:
        with get_session() as session:
            statement = select(cls).where(cls.id==id)
            result = session.exec(statement).first()
            return result.model_dump() if result else None

    @classmethod
    def insert(cls,
               poste: str,
               entreprise: str,
               expedition: str,
               url: str
               ) -> dict:
        with get_session() as session:
            item = cls(poste=poste,entreprise=entreprise,expedition=expedition,url=url)
            session.add(item)
            session.commit()
            session.refresh(item)
            return item.model_dump()
    @classmethod
    def delete(cls, id: int) -> bool:
        with get_session() as session:
            statement = select(cls).where(cls.id==id)
            result = session.exec(statement).first()
            if result:
                session.delete(result)
                session.commit()
                return True
            return False
def fake_stage():
    fake = Faker("fr_FR")
    return Stage(
        poste = fake.job(),
        entreprise = fake.company(),
        expedition = fake.date_this_month().isoformat(),
        url = fake.url(),
    )
                   
if __name__ == '__main__':
    stage = Stage.get_all()
    print(stage)
    stage = Stage.get_one(id=1)
    print(stage)

    #stage = Stage.insert(
    #    poste="retardataire",
    #    entreprise="Quentin",
    #    url="https://api.richnou/image.jpg",
     #   expedition="2024-11-18"
    #)
    #print(stage)

    ok = Stage.delete(id=3)
    print(ok)


