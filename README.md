# Mise en Production d'une API LLM avec FastAPI & Groq

[![Deploy on Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/)

API Python déployée sur Render : [https://mise-en-production-ml.onrender.com](https://mise-en-production-ml.onrender.com)

## Description

Cette API permet d'interroger un modèle LLM (Llama 4 Scout 17B via Groq) en français, pour obtenir des réponses claires et structurées à vos questions. Elle est construite avec FastAPI et déployée sur Render.

## Fonctionnalités
- **Route GET /** : Informations sur l'API.
- **Route POST /grok** : Envoie un prompt et reçoit une réponse générée par le modèle LLM.

## Exemple d'utilisation

### 1. Obtenir des informations sur l'API
```bash
curl https://mise-en-production-ml.onrender.com/
```

### 2. Envoyer une question au modèle
```bash
curl -X POST https://mise-en-production-ml.onrender.com/grok \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Explique le principe de la gravité en physique."}'
```

**Réponse attendue :**
```json
{
  "result": "1. La gravité est une force d'attraction..."
}
```

## Déploiement local

1. **Cloner le dépôt**
```bash
git clone <url-du-repo>
cd Mise en Production Python sur Render
```

2. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

3. **Configurer la clé API**
Créer un fichier `.env` à la racine avec :
```
API_KEY=your_groq_api_key
```

4. **Lancer le serveur**
```bash
uvicorn main:app --reload
```

## Variables d'environnement
- `API_KEY` : Clé d'API Groq (obligatoire)

## Exemple d'appel en Python

Voici comment consommer l'API depuis un script Python :

```python
import requests
import json

def poser_question(phrase):
    url = "https://mise-en-production-ml.onrender.com/grok"
    headers = {"Content-Type": "application/json"}
    payload = {"prompt": phrase}
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    response.raise_for_status()  # Lève une exception pour les codes d'erreur HTTP
    return response.json()

# Exemple d'utilisation
reponse = poser_question("Explique le principe de la gravité en physique.")
print(reponse["result"])
```

## Technologies utilisées
- Python 3.11+
- FastAPI
- Groq
- Render (hébergement)

## Auteur
- AVADRA Martial

## Licence
MIT
