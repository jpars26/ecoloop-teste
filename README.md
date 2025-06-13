# ecoloop-teste

Desafio Ecoloop – Flask API, análise de dados e operações matemáticas

**Observação:**

* Todos os ambientes foram criados com `python -m venv venv`.
* As dependências estão listadas em cada `requirements.txt`.
* Para rodar cada parte, basta ativar o venv, instalar com `pip install -r requirements.txt` e executar o script correspondente.

## Sumário

* [Visão Geral](#visão-geral)
* [Pré-requisitos](#pré-requisitos)
* [Estrutura de Pastas](#estrutura-de-pastas)
* [Configuração do Ambiente](#configuração-do-ambiente)

  * [Windows (PowerShell)](#windows-powershell)
  * [Unix / macOS (bash)](#unix--macos-bash)
* [Partes do Projeto](#partes-do-projeto)

  * [1. Flask API](#1-flask-api)
  * [2. Análise de Dados](#2-análise-de-dados)
  * [3. Operações Matemáticas](#3-operações-matemáticas)
* [Licença](#licença)

---

## Visão Geral

Este repositório contém a solução para o desafio técnico da Ecoloop, dividido em três partes:

1. **Flask API** – dois endpoints: saudação (GET) e soma (POST).
2. **Análise de Dados** – leitura de Excel com pandas para contar depósitos por máquina e somar pontos.
3. **Operações Matemáticas** – script CLI que faz operações básicas e avalia paridade e primalidade de dois números.

---

## Pré-requisitos

* **Python 3.8+** (testado na 3.13.1)
* **Git**
* (Opcional) **curl** ou **HTTPie** para testar endpoints

---

## Estrutura de Pastas

```
ecoloop-teste/
│
├── flask_api/           # Parte 1: API em Flask
│   ├── app.py           # Código da API
│   ├── requirements.txt # Dependências
│   └── venv/            # Virtualenv (não commitado)
│
├── analise_dados/       # Parte 2: Análise de planilha
│   ├── "Análise de Dados.xlsx"
│   ├── analysis.py      # Script de análise
│   ├── requirements.txt # Dependências
│   └── venv/            # Virtualenv
│
├── operacoes/           # Parte 3: Operações matemáticas
│   └── operacoes.py     # Script de operações
│
└── README.md            # Este arquivo
```

---

## Configuração do Ambiente

### Windows (PowerShell)

```powershell
# Na pasta raiz do projeto
cd path\to\ecoloop-teste

# Para cada subpasta (flask_api, analise_dados):
python -m venv venv
.\venv\Scripts\Activate.ps1

# Instala dependências
pip install -r requirements.txt
```

### Unix / macOS (bash)

```bash
# Na pasta raiz do projeto
cd ~/path/to/ecoloop-teste

# Para cada subpasta (flask_api, analise_dados):
python3 -m venv venv
source venv/bin/activate

# Instala dependências
pip install -r requirements.txt
```

---

## Partes do Projeto

### 1. Flask API

1. **Ative o virtualenv** dentro de `flask_api/`.
2. **Instale** (se ainda não):

   ```bash
   pip install -r requirements.txt
   ```
3. **Execute** a API:

   ```bash
   python app.py
   ```
4. **Endpoints**:

   * `GET /saudacao?nome=SeuNome`
     Retorna `Olá, SeuNome!`
   * `POST /soma`
     JSON body: `{ "a": número, "b": número }`
     Retorna: `{ "soma": resultado }`

**Exemplo com curl.exe (Windows)**

```powershell
curl.exe -X GET "http://127.0.0.1:5000/saudacao?nome=Joao"
curl.exe --% -X POST http://127.0.0.1:5000/soma -H "Content-Type: application/json" -d "{ \"a\":7,\"b\":5 }"
```
## Resposta - Parte 1 - API

      command: 
         curl.exe -X GET "http://127.0.0.1:5000/saudacao?nome=Joao"

      resposta: 
         Olá, Joao!

    command: 
      curl.exe --% -X POST http://127.0.0.1:5000/soma -H "Content-Type: application/json" -d "{ \"a\":7,\"b\":5 }"

      resposta:
                  {
                  "soma": 12
                  }
---

### 2. Análise de Dados

1. **Ative o virtualenv** dentro de `analise_dados/`.
2. **Instale**:

   ```bash
   pip install -r requirements.txt
   ```
3. **Execute**:

   ```bash
   python analysis.py
   ```
4. **O que faz**:

   * Lê `Análise de Dados.xlsx`.
   * Agrupa por **ID MÁQUINA** e conta depósitos.
   * Soma a coluna **PONTOS**.
   * Imprime no console um relatório.

## Resposta - Parte 2 – Exemplo de saída (analysis.py)
      | ID MÁQUINA | Depósitos |
      |-----------:|----------:|
      |         94 |        20 |
      |         97 |        30 |
      |        100 |        21 |
      |        106 |         2 |
      |        119 |         1 |
      |        123 |        25 |
      |        126 |         1 |

      **Pontos totais distribuídos:** 635


---

### 3. Operações Matemáticas

1. **(Opcional)** ative seu ambiente global ou use virtualenv.
2. **Execute** diretamente:

   ```bash
   python operacoes/operacoes.py
   ```
3. **Fluxo**:

   * Solicita dois números inteiros ao usuário.
   * Mostra soma, subtração, multiplicação e divisão.
   * Indica para cada número se é par/ímpar e primo/não primo.


## Resposta Parte 3 – Exemplo de execução (operacoes.py)
```bash
   PS C:\Users\Joao\Documents\Desafio\ecoloop-teste\operacoes> py .\operacoes.py
   Digite o primeiro número inteiro: 5
   Digite o segundo número inteiro: 5

   Soma:         5 + 5 = 10
   Subtração:   5 - 5 = 0
   Multiplicação: 5 * 5 = 25
   Divisão:     5 / 5 = 1.00

   O primeiro número (5) é ímpar e primo.

   O segundo número (5) é ímpar e primo.
```

## Licença

Este projeto está sob a [MIT License](LICENSE) — sinta-se à vontade para usar e modificar.

---

> **Contato**:
> Qualquer dúvida, estou disponível para esclarecimentos. Obrigado pela oportunidade de apresentar este desafio!
