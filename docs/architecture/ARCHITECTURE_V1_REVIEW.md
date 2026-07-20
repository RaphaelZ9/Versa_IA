# Versa AI

# Architecture Review v1.0

---

## Objetivo

Este documento consolida todas as decisões arquiteturais tomadas durante o desenvolvimento da primeira versão da Versa AI.

Seu objetivo é estabelecer padrões oficiais de desenvolvimento para garantir consistência, escalabilidade e facilidade de manutenção do projeto.

A partir desta versão, todo novo módulo deverá seguir os padrões aqui definidos.

---

# Filosofia da Arquitetura

A Versa AI foi construída seguindo os princípios de:

- Clean Architecture
- SOLID
- Domain Driven Design (DDD)
- Repository Pattern
- Service Layer Pattern
- Dependency Inversion
- Separation of Concerns

Cada classe possui apenas uma responsabilidade bem definida.

---

# Arquitetura Oficial

Todo módulo deverá seguir a arquitetura abaixo.

```
Entity
     │
Repository
     │
Service
     │
Manager
```

Cada camada possui responsabilidades específicas.

---

# Domain

O domínio representa o núcleo da aplicação.

```
app/domain/
```

Contém:

- Entities
- Enums
- Value Objects (futuro)

O domínio nunca conhece:

- Banco de dados
- APIs
- Providers
- Managers

---

# Entity

As entidades representam os objetos do domínio.

Exemplos:

- Memory
- Conversation
- Agent
- Tool
- User

As entidades podem conter pequenas regras relacionadas ao próprio estado.

Nunca devem:

- acessar banco
- chamar APIs
- executar OCR
- utilizar Providers
- utilizar Managers

---

# Repository

Responsável exclusivamente pela persistência.

Exemplos:

- BaseMemoryRepository
- InMemoryRepository
- SupabaseMemoryRepository (futuro)

Responsabilidades:

- salvar
- atualizar
- remover
- recuperar

Nunca deve:

- tomar decisões
- chamar APIs
- criar embeddings
- resumir dados

---

# Service

Responsável pelas regras de negócio.

Toda inteligência da aplicação deve permanecer nesta camada.

Exemplos:

- MemoryService

Responsabilidades:

- validações
- processamento
- decisões
- regras de negócio

Nunca deve conhecer:

- interface gráfica
- controllers
- pipeline
- LLM

---

# Manager

Responsável pela orquestração.

O Manager representa a interface pública do módulo.

Responsabilidades:

- coordenar Services
- simplificar acesso
- centralizar operações

O Manager nunca deve conter regras complexas.

Toda regra pertence ao Service.

---

# Provider

Representa integrações externas.

Exemplos:

- InternetProvider
- PDFProvider
- APIProvider
- EmailProvider
- SupabaseProvider

Responsabilidades:

- comunicação externa
- autenticação
- acesso a serviços

Nunca contém regras de negócio.

---

# Tool

Representa uma ação executável.

Exemplos:

- OCR
- PDF
- Email
- Filesystem
- Outlook

Ferramentas executam tarefas.

Nunca tomam decisões.

---

# Core

O Core concentra componentes reutilizáveis por toda a plataforma.

```
app/core/
```

Exemplos:

- logger
- config
- time_utils
- constants
- exceptions
- validation
- json_utils
- file_utils

Todo código reutilizável deve ser movido para o Core.

---

# Dependências

As dependências sempre seguem uma única direção.

```
Manager

↓

Service

↓

Repository

↓

Entity
```

Nunca é permitido:

Entity → Manager

Repository → Service

Service → Manager

---

# Comunicação entre módulos

Um módulo nunca acessa diretamente outro Repository.

Sempre utiliza o Manager.

Exemplo:

```
ConversationManager

↓

MemoryManager

↓

MemoryService
```

Nunca:

```
ConversationManager

↓

MemoryRepository
```

---

# Persistência

Toda persistência deve ocorrer através de Repository.

Nunca diretamente em:

- Supabase
- PostgreSQL
- Redis
- SQLite

---

# Testes

Todo módulo deve possuir Smoke Tests.

Fluxo:

```
Implementação

↓

Smoke Test

↓

Documentação
```

Nenhum módulo deve ser considerado concluído sem testes.

---

# Documentação

Todo módulo deverá possuir documentação própria.

Estrutura mínima:

- Objetivo
- Arquitetura
- Responsabilidades
- Fluxo
- Benefícios
- Evolução
- Status

---

# Estrutura de módulos

Sempre que possível um módulo deverá possuir:

```
module/

├── repositories/
├── services/
├── providers/
├── tools/
├── models/
├── module_manager.py
└── README.md
```

Nem todos os módulos utilizarão todas as pastas.

A estrutura deverá ser mantida simples.

---

# Injeção de Dependência

Nesta versão a injeção de dependência é manual.

Exemplo:

```
Manager

↓

Service

↓

Repository
```

Em versões futuras será criado um Container de Dependências.

---

# Fluxo da IA

Toda solicitação deverá seguir o fluxo abaixo.

```
Usuário

↓

Prompt Builder

↓

Intent

↓

Planning

↓

Knowledge Search

↓

Memory

↓

Tools

↓

LLM

↓

Resposta
```

Este fluxo representa a arquitetura cognitiva da Versa AI.

---

# Evoluções previstas

Arquitetura v2.0 deverá incluir:

- BaseRepository genérico
- BaseService
- Dependency Injection Container
- Event Bus
- Plugin System
- Vector Memory
- Multi Agent
- Reflection Engine

---

# Situação Atual

## Implementado

- Core
- Providers
- Managers
- Memory
- Repository
- Services
- Smoke Tests
- Documentação

---

## Em desenvolvimento

- Framework Core
- Intent
- Workflow
- Planning
- Agents

---

# Princípios da Versa AI

Toda implementação deve seguir os seguintes princípios:

1. Uma classe possui apenas uma responsabilidade.

2. Toda regra de negócio pertence ao Service.

3. Toda persistência pertence ao Repository.

4. Todo acesso externo pertence ao Provider.

5. Todo código reutilizável pertence ao Core.

6. Todo módulo deve possuir testes.

7. Todo módulo deve possuir documentação.

8. Simplicidade é preferível à complexidade.

9. Acoplamento baixo.

10. Alta coesão.

---

# Conclusão

A Arquitetura v1.0 estabelece os padrões oficiais da Versa AI.

Seu objetivo é garantir que todos os módulos futuros mantenham a mesma organização, permitindo evolução contínua da plataforma sem perda de qualidade.

Este documento deverá ser revisado sempre que novos padrões arquiteturais forem oficialmente incorporados ao projeto.

---

Autor

Raphael Wilson

Projeto

Versa AI

Versão

1.0