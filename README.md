## 🚀 Backend Video API - FastAPI
### 📋 Aperçu du Projet
Backend léger et performant construit avec FastAPI, fournissant des endpoints pour la gestion de vidéos.

### 🛠 Technologies Utilisées
- **Framework**: FastAPI
- **Langage**: Python 3.8+
- **Principales Bibliothèques**:
- Uvicorn (Serveur ASGI)
- Pydantic (Validation de données)
- Python-multipart (Gestion des requêtes)
### 🔧 Prérequis
- **Python 3.8+**
- **pip ou venv**
## 📦 Installation
```bash
# Création d'un environnement virtuel
python -m venv venv
source venv/bin/activate  # Unix
venv\Scripts\activate     # Windows

# Installation des dépendances
pip install -r requirements.txt
```
## 📦 Lancement du Serveur
```bash
fatapi main:app
```
## 📦 Documentation
[Documentation](https://fastapi.tiangolo.com/)
## 📂 Structure du Projet
```
BackEnd/
│
├── main.py             # Point d'entrée principal
├── Data/               # Données statiques
│   └── data.py         # Définition des données
├── requirements.txt    # Dépendances du projet
└── README.md           # Documentation du projet
## 🌐 Endpoints Principaux
```
- `/videos` : Retourne une liste de videos
- `/videos/{video_id}` : Retourne les détails d'une video