from openai import OpenAI
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente
load_dotenv()
cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
modelo = "gpt-3.5-turbo-0125"

def suporte_ti(pergunta_usuario):
    prompt_sistema = """
        Você é um atendente especializado em suporte de TI.
        Seu objetivo é ajudar usuários a resolver problemas com computadores, redes, software e sistemas operacionais.

        # Regras
        - Forneça respostas diretas e claras.
        - Se o problema for comum, sugira soluções práticas.
        - Se precisar de mais detalhes, peça informações ao usuário.
        - Se não souber a resposta, diga: "Não tenho informações suficientes para resolver isso. Você pode fornecer mais detalhes?"

        # Exemplos de Perguntas e Respostas
        Usuário: Meu computador não liga.
        Resposta: Certifique-se de que o cabo de força está conectado corretamente. Se estiver, tente pressionar o botão de ligar por 10 segundos.

        Usuário: Meu Wi-Fi está lento.
        Resposta: Reinicie o roteador e verifique se há muitos dispositivos conectados. Caso o problema persista, tente se aproximar do roteador.

        Usuário: O Windows não inicia.
        Resposta: Você vê alguma mensagem de erro? Se sim, informe-me qual é para que eu possa ajudar melhor.
    """

    resposta = cliente.chat.completions.create(
        messages=[
            {"role": "system", "content": prompt_sistema},
            {"role": "user", "content": pergunta_usuario}
        ],
        model=modelo,
        temperature=0,
        max_tokens=200
    )

    return resposta.choices[0].message.content

while True:
    pergunta_usuario = input("Como posso te ajudar com suporte de TI? ")
    texto_resposta = suporte_ti(pergunta_usuario)
    print(texto_resposta)
