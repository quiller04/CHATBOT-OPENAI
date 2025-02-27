from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
modelo = "gpt-3.5-turbo-0125"

def categoriza_produto(nome_produto, lista_categorias_possiveis):
    prompt_sistema = f"""
        Você é um categorizador de produtos.  
        Você deve classificar o produto informado com base nas categorias listadas abaixo.  

        # Lista de Categorias Válidas  
        {lista_categorias_possiveis.split(",")}  

        # Regras de Categorização  
        - **Apenas** utilize as categorias fornecidas.  
        - **Não crie, invente ou sugira categorias novas.**  
        - Se o produto **não se encaixar em nenhuma categoria**, retorne exatamente:  

        # Formato da Saída  
        Produto: Nome do Produto  
        Categoria: [Categoria correspondente]  

        # Exemplo de Saída  
        Produto: Escova elétrica com recarga solar  
        Categoria: Eletrônicos Verdes  

        # Exemplo de Saída  
        Produto: macarrão com linguiça  
        Categoria: categoria não encontrada, Por favor, forneça mais detalhes sobre o produto.

        # Exemplo de Saída  
        Produto: Dragon Ball  
        Categoria: Games  

        # Exemplo de Saída  
        Produto: Planta  
        Categoria: Árvore
    """

    resposta = cliente.chat.completions.create(
        messages=[
            {
                "role":"system",
                "content" : prompt_sistema
            },
            {
                "role" : "user",
                "content" : nome_produto
            }

        ],
        model=modelo,
        temperature = 0,
        max_tokens=200
    )

    return resposta.choices[0].message.content

categorias_validas = input("Informe as categorias válidas, separando por vírgula: ")

while True:
    nome_produto = input("Digite o nome do produto: ")
    texto_resposta = categoriza_produto(nome_produto, categorias_validas)
    print(texto_resposta)