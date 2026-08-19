# 🤖 Versa IA

**Plataforma de Inteligência Artificial para operações corporativas**, desenvolvida para compreender contexto, responder perguntas, utilizar conhecimento, executar ferramentas e orquestrar diferentes capacidades de IA por meio de linguagem natural.

O projeto foi desenvolvido com uma **arquitetura modular e extensível**, permitindo trabalhar com diferentes provedores de modelos de linguagem, memória, conhecimento, ferramentas, planejamento e agentes especializados.

> Projeto de desenvolvimento e pesquisa aplicada em Inteligência Artificial, automação e integração de sistemas.

---

## 🚀 Principais Características

* Arquitetura modular
* Suporte a múltiplos LLMs
* Sistema de memória
* Planning Engine
* Sistema de ferramentas (Tools)
* Busca inteligente de conhecimento
* RAG — Retrieval-Augmented Generation
* Providers intercambiáveis
* Cache
* Telemetria
* Automações
* Agentes especializados
* Integração com APIs e sistemas externos

### Modelos e Providers

* OpenAI
* Google Gemini
* Anthropic Claude
* Ollama

---

## 🧠 Arquitetura

A aplicação foi estruturada em módulos independentes, permitindo separar responsabilidades e facilitar a evolução da plataforma.

```text
┌─────────────────────┐
│       Usuário       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│      VersaAI        │
│   Interface de IA   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│    VersaKernel      │
│  Núcleo da aplicação│
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Chat Orchestrator  │
└──────────┬──────────┘
           │
     ┌─────┼─────┬──────────┬────────┬────────┐
     ▼     ▼     ▼          ▼        ▼        ▼
 Planning Knowledge Memory    AI      Tools   Context
```

A arquitetura permite que cada componente evolua de forma independente, reduzindo o acoplamento entre as diferentes responsabilidades da aplicação.

---

## 🏗️ Componentes

### Planning

Responsável pelo planejamento de tarefas que exigem múltiplas etapas de execução.

### Knowledge

Camada responsável pela busca e utilização de conhecimento para contextualizar as respostas da IA.

### Memory

Gerenciamento de informações utilizadas durante as interações, permitindo preservar contexto e histórico.

### AI

Camada responsável pela comunicação com os diferentes provedores de modelos de linguagem.

### Tools

Estrutura para disponibilização de ferramentas que podem ser utilizadas pela inteligência artificial durante a execução das tarefas.

### Context

Responsável pelo gerenciamento das informações de contexto utilizadas durante o processamento das solicitações.

---

## 🤖 Agentes Especializados

A arquitetura permite trabalhar com **agentes especializados**, possibilitando distribuir diferentes responsabilidades entre componentes específicos da plataforma.

Essa abordagem permite construir fluxos mais complexos sem concentrar toda a lógica em um único agente.

---

## 🔎 RAG e Knowledge Search

A plataforma possui suporte a **Retrieval-Augmented Generation (RAG)** e mecanismos de busca de conhecimento.

O objetivo é permitir que os modelos utilizem informações relevantes durante a geração das respostas, reduzindo a dependência exclusivamente do conhecimento incorporado ao modelo.

---

## 🔌 Integrações

A plataforma foi projetada para trabalhar com integrações externas por meio de APIs e serviços.

Entre os componentes utilizados no projeto estão:

* REST APIs
* Supabase
* PostgreSQL
* Microsoft Teams
* WhatsApp
* Serviços de modelos de linguagem

---

## 🛠️ Tecnologias

### Backend

`Python`

### Inteligência Artificial

`OpenAI` `Gemini` `Anthropic Claude` `Ollama`

### Dados

`Supabase` `PostgreSQL`

### Integrações

`REST APIs` `JSON` `Microsoft Teams API` `WhatsApp API`

### Arquitetura

`RAG` `Agents` `Planning` `Memory` `Tools` `Knowledge Search`

---

## 📁 Estrutura do Projeto

```text
Versa-AI/
│
├── app/
├── docs/
├── logs/
├── tests/
│
├── main.py
├── README.md
└── requirements.txt
```

A organização do projeto separa aplicação, documentação, testes e demais componentes, favorecendo manutenção e evolução da plataforma.

---

## ▶️ Execução

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a aplicação:

```bash
python main.py
```

As configurações necessárias para execução devem ser definidas no ambiente local conforme a configuração utilizada pelo projeto.

---

## 🎯 Objetivos

A plataforma foi concebida para explorar o uso de Inteligência Artificial em ambientes corporativos, permitindo:

* Conversação utilizando linguagem natural
* Consulta de conhecimento
* Utilização de ferramentas
* Integração com APIs
* Automação de processos
* Gerenciamento de memória
* Planejamento de tarefas
* Utilização de múltiplos modelos de IA
* Orquestração de agentes especializados

---

## 🧩 Princípios de Arquitetura

O projeto segue princípios voltados à construção de uma aplicação modular e extensível:

* **Responsabilidade Única**
* **Baixo Acoplamento**
* **Alta Coesão**
* **Arquitetura Modular**
* **Providers Plugáveis**
* **Estratégias Independentes**
* **Facilidade de Extensão**

A separação das responsabilidades permite adicionar ou modificar componentes sem exigir alterações generalizadas na aplicação.

---

## 📌 Sobre o Projeto

O Versa IA representa um projeto de aplicação prática de **Inteligência Artificial, agentes, automação, integração de sistemas e arquitetura de software**.

O projeto faz parte da experiência de desenvolvimento de soluções tecnológicas para o ambiente corporativo.

### Tecnologias principais

`Python` `LLMs` `RAG` `AI Agents` `Supabase` `PostgreSQL` `REST APIs` `Ollama`

---

## 🔒 Propriedade Intelectual

Este projeto contém componentes desenvolvidos para ambiente corporativo.

Informações internas, dados, credenciais, regras de negócio e demais elementos proprietários não fazem parte deste material público.
