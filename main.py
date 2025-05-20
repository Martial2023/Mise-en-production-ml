from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os


load_dotenv()
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY not found in .env file")

client = Groq(api_key=API_KEY)

app = FastAPI()

class PromptInput(BaseModel):
    prompt: str
    
def get_answer(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[{
                "role": "user",
                "content": f"Réponds clairement étape par étape à cette question: {prompt}. Ne fais pas de commentaire ou d'introduction. Vas directement à l'essentiel"
            }],
            temperature=1,
            max_completion_tokens=1024,
            top_p=1,
            stream=False,
            stop=None
        )
        return response.choices[0].message.content
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro calling Graoq API: {str(e)}")
 
@app.get("/")
def get_started():
    return {
        "info": "Cette API FastAPI permet d'exécuter un modèle LLM (Llama 4 Scout 17B) via Groq et de poser des questions en français. Utilisez la route POST /grok avec un prompt pour obtenir une réponse générée."
    }
    
@app.post("/grok")
async def agent(input: PromptInput):
    try:
        result = get_answer(input.prompt)
        return {
            "result": result
        }
    except HTTPException as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)