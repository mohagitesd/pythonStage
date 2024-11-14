from sqlmodel import SQLModel, Field, create_engine,Session

file_name = "database.sqlite"


#Initialiser le moteur = dépend du SGBD utilisé
engine = create_engine(f"sqlite:///{file_name}")


# créer les tables si nécessaire 
SQLModel.metadata.create_all(engine)

def get_session():
    return Session(engine)
