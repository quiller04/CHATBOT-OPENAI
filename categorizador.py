from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
cliente  = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

resposta = cliente.chat.completions.create(
    messages=[
        {
            "role" : "system",
            "content" : """
            classifique o produto abaixo em uma das categorias: higiene pessoal, moda ou casa e de uma descrição da categoria.
            """
        },
        {
            "role" : "user",
            "content" : """
            escova de dentes de bambu
            """
        }
    ],
    model="gpt-4",
    temperature = 0,
    max_tokens=200,
    n = 3 #determina a quantidade de respostas
)

print(resposta.choices[0].message.content)