# Versa AI

# Architecture Patterns

---

# Objetivo

Este documento define os padrões oficiais de desenvolvimento da Versa AI.

Todo novo módulo, componente ou funcionalidade deverá seguir as regras descritas neste documento.

O objetivo é garantir:

- consistência
- baixo acoplamento
- alta coesão
- facilidade de manutenção
- escalabilidade

---

# Estrutura da aplicação

```
Application
        │
        ▼
Managers
        │
        ▼
Services
        │
        ▼
Repositories
        │
        ▼
Entities
```

---

# Estrutura de diretórios

```
app/

├── core/
├── domain/
├── providers/
├── repository/
├── managers/
├── memory/
├── knowledge/
├── conversation/
├── workflow/
├── intent/
├── tools/
└── pipeline/
```

Cada módulo deverá possuir estrutura semelhante.

---

# Entity Pattern

As Entities representam o domínio.

Responsabilidades:

- representar dados
- pequenas regras relacionadas ao próprio estado
- serialização simples

Nunca devem:

- acessar banco
- chamar APIs
- utilizar Providers
- utilizar Managers
- executar regras complexas

Exemplo:

```
Memory

Conversation

Message

User
```

---

# Repository Pattern

Todo acesso à persistência deverá ocorrer através de Repository.

Responsabilidades:

- save
- update
- delete
- get_by_id
- get_all
- exists
- count
- clear

Nunca deve:

- chamar APIs
- utilizar LLM
- enviar emails
- tomar decisões

Todo Repository deve herdar de:

```
BaseRepository
```

---

# Service Pattern

Toda regra de negócio pertence ao Service.

Responsabilidades:

- validações
- processamento
- decisões
- regras de negócio

Nunca deve conhecer:

- interface gráfica
- pipeline
- controllers

Exemplo:

```
MemoryService
ConversationService
WorkflowService
```

---

# Manager Pattern

Todo módulo deverá possuir um Manager.

O Manager representa a interface pública do módulo.

Responsabilidades:

- coordenar Services
- simplificar acesso
- centralizar operações

Nunca implementa regras complexas.

Exemplo:

```
MemoryManager

KnowledgeManager

ToolManager
```

---

# Provider Pattern

Representa integrações externas.

Exemplos:

```
OpenAI

Supabase

Email

Internet

PDF

Outlook
```

Responsabilidades:

- autenticação
- comunicação
- acesso externo

Nunca implementa regras de negócio.

---

# Tool Pattern

Representa uma ação executável.

Exemplos:

```
OCR

Rename PDF

Download Email

Upload File

Move File
```

As Tools executam tarefas.

As decisões pertencem aos Managers.

---

# Core Pattern

Todo código reutilizável deverá permanecer no Core.

Exemplos:

```
time_utils

logger

config

constants

exceptions

validation

string_utils

json_utils

file_utils
```

Nunca duplicar funções utilitárias.

---

# Dependency Pattern

Dependências sempre seguem uma única direção.

```
Manager

↓

Service

↓

Repository

↓

Entity
```

Nunca:

```
Entity → Repository

Repository → Manager

Service → Manager
```

---

# Dependency Injection

Nesta versão:

Injeção manual.

Futuro:

Container de Dependências.

---

# Test Pattern

Todo módulo deve possuir:

- Smoke Test

Fluxo obrigatório:

```
Implementação

↓

Smoke Test

↓

Documentação
```

Nenhum módulo será considerado concluído sem testes.

---

# Documentation Pattern

Todo módulo deverá possuir documentação.

Estrutura mínima:

- Objetivo
- Arquitetura
- Responsabilidades
- Fluxo
- Benefícios
- Evolução
- Status

---

# Logging Pattern

Todo erro relevante deverá utilizar o Logger central da aplicação.

Nunca utilizar:

```
print()
```

para logs de produção.

---

# DateTime Pattern

Toda data deverá utilizar:

```
utc_now()
```

Nunca utilizar:

```
datetime.now()

datetime.utcnow()
```

diretamente na aplicação.

---

# Naming Pattern

Classes:

```
PascalCase
```

Funções:

```
snake_case
```

Variáveis:

```
snake_case
```

Constantes:

```
UPPER_CASE
```

Arquivos:

```
snake_case.py
```

---

# Module Pattern

Todo novo módulo deverá possuir:

```
module/

repositories/

services/

providers/

tools/

module_manager.py

README.md
```

Nem todas as pastas são obrigatórias.

Mas a estrutura deve permanecer previsível.

---

# Smoke Test Pattern

Cada módulo deverá possuir um teste de validação.

Exemplo:

```
tests/

smoke/

test_memory.py

test_memory_service.py

test_memory_manager.py
```

---

# Documentation Flow

Todo desenvolvimento seguirá:

```
Planejamento

↓

Implementação

↓

Smoke Test

↓

Documentação
```

---

# Arquitetura Cognitiva

Fluxo oficial da IA.

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

Tool Selector

↓

Tool

↓

LLM

↓

Resposta
```

---

# Evolução futura

Arquitetura v2.0 deverá incluir:

- Dependency Injection
- Event Bus
- Plugin System
- Reflection Engine
- Multi-Agent
- Vector Memory
- Workflow Engine

---

# Checklist para novos módulos

Antes de finalizar qualquer módulo verificar:

- Entity criada
- Repository criado
- Service criado
- Manager criado
- Smoke Test criado
- Documentação criada

---

# Princípios

Todo código da Versa AI deve seguir:

- Clean Code
- Clean Architecture
- SOLID
- DDD
- Repository Pattern
- Service Layer
- Separation of Concerns
- Simplicidade

---

# Conclusão

Os padrões definidos neste documento representam a arquitetura oficial da Versa AI.

Todo novo desenvolvimento deverá respeitar estes padrões para garantir consistência e evolução sustentável da plataforma.

---

Autor

Raphael Wilson

Projeto

Versa AI

Versão

1.0
