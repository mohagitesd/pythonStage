```sh
python -m venv venv

# mac
source venv/bin/activate
## installation de package
venv/bin/pip install ...

# win
.\venv\Scripts\activate
## installation de package
.\venv\Scripts\pip install fastapi
.\venv\Scripts\pip install uvicorn
### REQUIREMENTS
.\venv\Scripts\pip freeze > requirements.txt

```

# Fast API

- API
- Route = chemin menant aux données
- définir des 'chemins' => fonctions python
- methode http
  - GET : renvoyer des données
  - POST : recevoir (insert) + renvoyer des données
  - PUT/PATCH : recevoir (update) + renvoyer des données
  - DELETE : recevoir (delete)
- renvoit aussi un code http
  - 200
  - 201
  - 400
  - ...

Authentification

# Créer un site web

- Créer uns sous dossier template
- créer un fichier index.html
- définir une route /home
- définir la fonction read_home
- installer jinja2
