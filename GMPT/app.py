import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import markdown
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Configuração do cliente OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

#Funções

def chat_com_mestre(mensagem_jogador, contexto="", nome="", classe="", origem=""):
    """
    Função para enviar uma mensagem ao chatbot e receber uma resposta.
    
    :param mensagem_jogador: A mensagem do jogador.
    :param contexto: Contexto adicional para o chatbot (opcional).
    :return: Resposta do chatbot.
    """
    try:
        if mensagem_jogador == "":
            resposta = client.chat.completions.create(
                model="gpt-4o",  # Modelo a ser usado
                messages=[
                    {"role": "system", "content": f"""Você é um Mestre de RPG experiente em Dungeons & Dragons. Seja criativo e siga as regras.
                    Ficha do jogador
                    Nome do personagem: {nome} 
                    Classe: {classe}
                    Origem: {origem}
                    Nivel: 1
                    """},
                    {"role": "user", "content": f"""Dê detalhes sobre a ficha do jogador de forma mais tecnica Exemplo:
                Ficha de Personagem - D&D 5ª Edição

                Nome do Personagem:
                Classe e Nível:
                Raça:
                Antecedente:
                Tendência:
                Experiência (XP):

                Atributos:

                Força (For):

                Destreza (Des):

                Constituição (Con):

                Inteligência (Int):

                Sabedoria (Sab):

                Carisma (Car):

                Pontos de Vida (PV):
                Classe de Armadura (CA):
                Iniciativa:
                Deslocamento:

                Testes de Resistência:

                Força:

                Destreza:

                Constituição:

                Inteligência:

                Sabedoria:

                Carisma:


                Perícias:



                Idiomas:

                Equipamento:

                Características e Talentos de Classe:

                Magias (se aplicável):

                Classe de Magia:

                CD para resistir às magias:

                Bônus de Ataque Mágico:

                Espaços de Magia:


                Magias Conhecidas/Preparadas:



                História do Personagem:
                , e no fim inicie a aventura com base no contexto: {contexto}"""}
                ],
                max_tokens=1000,  # Limite de tokens na resposta
                temperature=1,  # Controle de criatividade (0 = mais determinístico, 1 = mais criativo)
            )
        else:    
            resposta = client.chat.completions.create(
                model="gpt-4o",  # Modelo a ser usado
                messages=[
                    {"role": "system", "content": f"""Você é um Mestre de RPG experiente em Dungeons & Dragons. Seja criativo e siga as regras.
                    Ficha do jogador
                    Nome do personagem: {nome} 
                    Classe: {classe}
                    Origem: {origem}
                    Nivel: 1
                    """},
                    {"role": "user", "content": f"{contexto}\nJogador: {mensagem_jogador}"}
                ],
                max_tokens=500,  # Limite de tokens na resposta
                temperature=1,  # Controle de criatividade (0 = mais determinístico, 1 = mais criativo)
            )
        return resposta.choices[0].message.content.strip()
    except Exception as e:
        return f"Erro ao conectar com a API: {e}"



def gerar_imagem(descricao, num_imagens=1, tamanho="1024x1024"):
    try:
        resposta = client.images.generate(
            model="dall-e-3",  # Especifica o modelo DALL-E 3
            prompt=descricao,   # Descrição da imagem que você deseja gerar
            n=num_imagens,      # Número de imagens a serem geradas
            size=tamanho        # Tamanho da imagem (opções: "1024x1024", "1024x1792", "1792x1024")
        )
        # Retorna as URLs das imagens geradas
        return [imagem.url for imagem in resposta.data]
    except Exception as e:
        print(f"Erro ao gerar a imagem: {e}")
        return None
    

#WEB

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/start_game", methods=["POST"])
def start_game():
    dados = request.json
    mensagem = dados.get("mensagem", "")
    contexto = dados.get("contexto", "")
    nome = dados.get("nome", "")
    classe = dados.get("classe", "")
    origem = dados.get("origem", "")
    
    resposta = chat_com_mestre(mensagem, contexto, nome, classe, origem)
    resposta_html = markdown.markdown(resposta)
    contexto=resposta
    return jsonify({"resposta": resposta_html})

@app.route("/chat", methods=["POST"])
def chat():
    dados = request.json
    mensagem = dados.get("mensagem", "")
    contexto = dados.get("contexto", "")
    nome = dados.get("nome", "")
    classe = dados.get("classe", "")
    origem = dados.get("origem", "")
    
    resposta = chat_com_mestre(mensagem, contexto, nome, classe, origem)
    contexto=resposta
    return jsonify({"resposta": resposta})

if __name__ == "__main__":
    app.run(debug=True)
