# Arquitetura da Versa IA

## Visão Geral

A Versa IA foi construída utilizando uma arquitetura em camadas.

Cada camada conhece apenas a camada imediatamente inferior.

```
main.py
    │
    ▼
VersaAI
    │
    ▼
VersaKernel
    │
    ▼
Orchestrators
    │
    ▼
Planning
Knowledge
Memory
AI
Tools
Context
```

Essa abordagem reduz o acoplamento e facilita a evolução do projeto.

---

# Fluxo Geral

```
Usuário

↓

VersaAI

↓

VersaKernel

↓

ChatOrchestrator

↓

Planning

↓

Knowledge

↓

Memory

↓

Tools

↓

AI Provider

↓

Resposta
```

---

# Estrutura Completa

```
app/

agents/
ai/
api/
auth/
automation/
cache/
capabilities/
context/
conversation/
core/
database/
domain/
email/
events/
exceptions/
integrations/
intent/
knowledge/
memory/
orchestrators/
pipeline/
planning/
query/
rag/
schemas/
services/
telemetry/
tools/
utils/
```

---

# Responsabilidade de Cada Módulo

## agents

Agentes especializados.

Exemplo:

- Comercial
- Financeiro
- Engenharia
- RH

---

## ai

Comunicação com LLMs.

Responsável por:

- Prompt Builder
- Providers
- Response Parser
- Model Manager

Nunca contém regra de negócio.

---

## automation

Execução de tarefas automáticas.

---

## cache

Cache de memória.

Implementações:

- Memory Cache
- Redis

---

## capabilities

Determina as capacidades disponíveis para a IA.

Exemplo:

- Pesquisar
- Enviar Email
- Executar Ferramentas

---

## context

Construção do contexto enviado ao LLM.

Inclui:

- Histórico
- Memória
- Documentos
- Ferramentas

---

## conversation

Gerenciamento das conversas.

---

## core

Núcleo da aplicação.

Contém:

- VersaKernel
- Configurações
- Logger
- Constantes
- Versionamento

---

## database

Abstração do banco de dados.

---

## domain

Entidades de negócio.

---

## email

Integrações de email.

---

## events

Sistema interno de eventos.

---

## exceptions

Exceções customizadas.

---

## integrations

Integrações externas.

Exemplo:

- APIs
- ERP
- CRM
- OCR

---

## intent

Identificação da intenção do usuário.

---

## knowledge

Sistema de conhecimento.

Responsável por:

- Busca
- Providers
- Ranking
- Construção de conhecimento

---

## memory

Memória de curto e longo prazo.

---

## orchestrators

Coordenação entre módulos.

Não executa lógica.

Apenas organiza o fluxo.

---

## pipeline

Pipeline principal da conversa.

---

## planning

Planejamento das ações.

Responsável por:

- Plano
- Passos
- Estratégias

---

## query

Pré-processamento da pergunta.

Responsável por:

- Normalização
- Expansão
- Classificação
- Otimização

---

## rag

Infraestrutura RAG.

---

## schemas

Modelos de entrada e saída.

---

## services

Serviços de domínio.

---

## telemetry

Métricas.

Performance.

Auditoria.

---

## tools

Ferramentas executáveis pela IA.

Fluxo:

```
ToolSelector

↓

ToolManager

↓

Registry

↓

Tool
```

As implementações ficam organizadas por domínio:

```
tools/

implementations/

api/
cliente/
email/
pdf/
propostas/
suporte/
```

---

## utils

Funções utilitárias reutilizáveis.

Não devem conter:

- Regras de negócio
- IA
- Banco
- APIs
- Providers

---

# Princípios Arquiteturais

A Versa IA segue:

- SOLID
- Clean Architecture
- Separation of Concerns
- Strategy Pattern
- Factory Pattern
- Facade Pattern
- Registry Pattern
- Provider Pattern
- Orchestrator Pattern

---

# Camadas

```
Interface

↓

Facade (VersaAI)

↓

Kernel

↓

Orchestrators

↓

Planning

↓

Knowledge

↓

Memory

↓

AI / Tools

↓

Providers
```

---

# Escalabilidade

Novos recursos devem ser adicionados através de:

- Novos Providers
- Novas Strategies
- Novos Tools
- Novos Agents
- Novas Capabilities

Nunca alterando módulos existentes sempre que possível.

---

# Objetivo Final

A Versa IA foi concebida para evoluir de um chatbot para uma plataforma completa de Inteligência Artificial Corporativa capaz de:

- conversar;
- pesquisar;
- raciocinar;
- planejar;
- executar ferramentas;
- automatizar processos;
- integrar sistemas;
- aprender com memória;
- operar com múltiplos modelos de IA.

A arquitetura foi projetada para suportar essa evolução de forma modular, escalável e de fácil manutenção.
