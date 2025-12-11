# GMPT — Game Master Powered by AI

[![Repository](https://img.shields.io/badge/repo-FelipeSousa366/game--master--ia-blue)](https://github.com/FelipeSousa366/game-master-ia)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](#)
[![Flask](https://img.shields.io/badge/flask-%20web%20framework-lightgrey)](#)
[![OpenAI API](https://img.shields.io/badge/OpenAI-API-orange)](#)

---

## Visão geral

**GMPT** é um *Mestre de RPG Virtual* (Game Master) que utiliza modelos de linguagem da OpenAI para gerar personagens, narrativas, interpretar ações do jogador e manter coerência de contexto ao longo da aventura — entregue através de uma interface web leve em **Flask**.

O projeto demonstra habilidades práticas em:
- Integração com LLMs (OpenAI API)
- Prompt engineering e gestão de contexto
- Arquitetura limpa (separação entre engine de IA e camada web)
- Boas práticas de desenvolvimento (virtualenv, `.env`, `requirements.txt`, `.gitignore`)
- Preparação para deploy e demonstração (Gradio/Streamlit/Docker possíveis)

---

## Principais funcionalidades

- Geração estruturada de fichas de personagem (atributos, história, habilidades)
- Respostas narrativas dinâmicas a comandos do jogador
- Manutenção de contexto/“memória” simples para sessões
- Interface web com entrada de usuário e exibição de respostas
- Código modular — engine de IA separada do servidor Flask

---

## Demonstração rápida

> **Rodar localmente (Windows, PowerShell)**

```powershell
# clonar repositório
git clone https://github.com/FelipeSousa366/game-master-ia.git
cd game-master-ia

# criar e ativar venv
python -m venv .venv
.\.venv\Scripts\Activate

# instalar dependências
python -m pip install --upgrade pip
pip install -r requirements.txt

# criar .env (não versionar)
# .env (exemplo)
# OPENAI_API_KEY=sk-...

# rodar a aplicação
set FLASK_APP=app.py        # ou: $env:FLASK_APP = "app.py" (PowerShell)
flask run
```


## Demonstração visual

### Tela inicial
![Tela inicial](GMPT/assets/screenshots/Tela%20inicial.png)

### Criação de Personagem
![Criação de Personagem](GMPT/assets/screenshots/Criação%20de%20Personagem.png)

### Ficha gerada pela IA
![Ficha gerada](GMPT/assets/screenshots/Ficha%20gerado%20pela%20IA.png)

### Interação com a IA
![Resposta da IA](GMPT/assets/screenshots/Interação%20com%20o%20GMPT.png)
