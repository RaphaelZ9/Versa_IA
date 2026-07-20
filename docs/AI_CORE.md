# Versa IA

# AI Core

---

# Visão

A Versa IA é a plataforma de inteligência operacional da Versa Energia.

Sua missão é compreender solicitações em linguagem natural, responder dúvidas técnicas, executar tarefas, orquestrar automações corporativas e integrar sistemas internos por meio de uma arquitetura baseada em componentes cognitivos.

O AI Core representa o cérebro da plataforma.

---

# Missão

O AI Core é responsável por transformar uma solicitação do usuário em um plano de execução.

Ele não executa ações diretamente.

Ele pensa.

Quem executa são as ferramentas e automações.

---

# Filosofia

O AI Core segue um princípio simples:

> Pensar antes de executar.

Todo comando recebido deve passar por um processo de análise, compreensão e planejamento antes de qualquer ação.

---

# Componentes

O AI Core é composto pelos seguintes componentes:

• Conversation

Responsável pelo histórico da conversa.

---

• Intent

Identifica o objetivo do usuário.

---

• Memory

Recupera informações importantes.

---

• Knowledge

Consulta o conhecimento da empresa.

---

• Context Builder

Monta o contexto completo da solicitação.

---

• Planning Engine

Decide qual estratégia utilizar.

É o principal componente do AI Core.

---

• Tool Selector

Escolhe quais ferramentas executar.

---

• Automation Manager

Decide quando utilizar automações existentes.

---

• Prompt Builder

Monta prompts para os modelos de IA.

---

• LLM Router

Seleciona qual modelo utilizar.

GPT

Claude

Gemini

Ollama

etc.

---

# Fluxo Cognitivo

```
Usuário

↓

Conversation

↓

Intent

↓

Memory

↓

Knowledge

↓

Context Builder

↓

Planning Engine

↓

┌───────────────┬───────────────┐

▼               ▼

Tool Selector   Automation Manager

↓

Prompt Builder

↓

LLM Router

↓

Resposta
```

---

# Princípios

## O LLM não é o cérebro.

O LLM é apenas um mecanismo de linguagem.

Toda decisão pertence ao Planning Engine.

---

## Ferramentas executam.

Ferramentas não tomam decisões.

Recebem comandos.

Executam.

Retornam resultados.

---

## Automações executam processos.

As automações representam workflows corporativos.

São controladas pela Versa IA.

---

## O usuário conversa apenas com a Versa IA.

Nunca diretamente com:

Oracle

Outlook

Supabase

OneDrive

GPT

Claude

etc.

---

## Toda ação deve ser planejada.

Mesmo uma ação simples como:

"Envie um email"

deve passar pelo Planning Engine.

---

# Tipos de resposta

O AI Core pode produzir:

• Resposta textual

• Execução de ferramenta

• Execução de automação

• Consulta ao conhecimento

• Consulta à memória

• Fluxo híbrido

---

# Responsabilidades

O AI Core deve:

✓ compreender

✓ planejar

✓ decidir

✓ coordenar

✓ aprender

---

# Não é responsabilidade

O AI Core NÃO deve:

executar SQL

ler arquivos

enviar emails

chamar Microsoft Graph

processar PDFs

Essas responsabilidades pertencem às Tools.

---

# Objetivo final

O objetivo do AI Core é transformar linguagem natural em ações inteligentes.

---

# Exemplo

Usuário

"Reprocese as faturas GD que falharam ontem."

Fluxo

Conversation

↓

Intent

↓

Context Builder

↓

Planning Engine

↓

Automation Manager

↓

GD Automation

↓

Invoice Tool

↓

Oracle Tool

↓

Resposta

---

# Outro exemplo

Usuário

"Como funciona a compensação de energia?"

Fluxo

Conversation

↓

Intent

↓

Knowledge Search

↓

Prompt Builder

↓

LLM

↓

Resposta

---

# Outro exemplo

Usuário

"Leia este PDF e envie um resumo ao financeiro."

Fluxo

Conversation

↓

Intent

↓

Planning

↓

PDF Tool

↓

Prompt Builder

↓

LLM

↓

Email Tool

↓

Resposta

---

# Arquitetura

```
                     Versa IA

                         │

                  AI CORE

                         │

         ┌───────────────┼───────────────┐

         ▼               ▼               ▼

   Knowledge        Tools         Automations

         │               │               │

         ▼               ▼               ▼

   Oracle        Microsoft Graph    Workers

   PDFs          OneDrive           Schedulers

   Banco         Email              Webhooks
```

---

# Conclusão

O AI Core representa o cérebro da Versa IA.

Toda inteligência da plataforma deverá estar concentrada nele.

Ele não executa tarefas.

Ele decide quem deve executá-las.

Essa separação garante baixo acoplamento, alta escalabilidade e permite que novas ferramentas, automações e modelos de IA sejam incorporados sem alterar a lógica cognitiva da plataforma.