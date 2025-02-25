from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
cliente  = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
modelo = "gpt-4"

pronpt_sistema = """
    Você é um categorizador de produtos
    voce deve assumir as categorias presentes na lista abaixo.

    #Lista de categorias validas
    -moda sustentavel
    -produtos para lar
    -beleza natural
    -eletrõnicos verdes
    -higiene individual

    #formato de saída
    produto: Nome do produto
    Categoria: apresenta a categoria do produto

    # Exemplo de saída
    produto: escova elétrica com recarga solar
    Categoria: Eletrônicos Verdes

"""

promot_usuario =  input("apresente o nome de um produto: ")

resposta = cliente.chat.completions.create(
    messages=[
        {
            "role" : "system",
            "content" : pronpt_sistema
        },
        {
            "role" : "user",
            "content" : promot_usuario
        }
    ],
    model=modelo,
    temperature = 0,
    max_tokens=200,
    #n = 3 #determina a quantidade de respostas
)

print(resposta.choices[0].message.content)