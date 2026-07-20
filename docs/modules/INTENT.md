# Versa AI

# Intent Module

---

## Objetivo

O módulo **Intent** é responsável por representar, armazenar e gerenciar as intenções identificadas durante a interação entre o usuário e a Versa AI.

Ele constitui o primeiro estágio da camada cognitiva da plataforma e será utilizado futuramente pelo **Planning Engine**, **Tool Selector**, **Knowledge Search** e demais componentes da IA.

---

# Arquitetura

```
Usuário
    │
    ▼
IntentManager
    │
    ▼
IntentService
    │
    ▼
IntentRepository
    │
    ▼
Intent Entity
```

---

# Estrutura do módulo

```
app/

domain/
└── entities/
    └── intent/
        ├── intent.py
        └── intent_type.py

intent/
├── repositories/
│   ├── base_intent_repository.py
│   └── in_memory_repository.py
│
├── services/
│   └── intent_service.py
│
└── intent_manager.py
```

---

# Componentes

## Intent

Representa uma intenção identificada.

Contém:

- identificador
- tipo
- texto original
- confiança
- entidades extraídas
- ferramentas sugeridas
- metadados
- data de criação

---

## IntentType

Enum contendo os tipos de intenção suportados.

Exemplos:

- CHAT
- SEARCH
- QUESTION
- SUMMARIZE
- EXTRACT
- EMAIL
- MEMORY
- KNOWLEDGE
- WORKFLOW
- TOOL

---

## BaseIntentRepository

Contrato base para persistência de intenções.

Define operações como:

- save
- update
- delete
- get_by_id
- get_all
- exists
- count
- clear

Além das operações específicas:

- find_by_type
- find_by_confidence
- find_by_text

---

## InMemoryIntentRepository

Implementação utilizando memória RAM.

Utilizado durante:

- desenvolvimento
- testes
- execução local

Não realiza persistência em banco de dados.

---

## IntentService

Responsável pelas regras de negócio relacionadas às intenções.

Coordena o acesso ao repositório.

Não possui conhecimento sobre infraestrutura.

---

## IntentManager

Interface pública do módulo.

Responsável por coordenar o IntentService.

É o ponto de entrada para qualquer componente da plataforma que necessite manipular intenções.

---

# Fluxo

```
Mensagem

↓

Intent

↓

Repository

↓

Service

↓

Manager

↓

Planning Engine (futuro)
```

---

# Casos de uso

Exemplo:

```
Usuário

↓

"Procure a nota fiscal da Eneva"

↓

IntentType.SEARCH

↓

Planning Engine

↓

Tool Selector

↓

Resposta
```

Outro exemplo:

```
Usuário

↓

"Envie um email para o financeiro"

↓

IntentType.EMAIL

↓

Email Tool

↓

Resposta
```

---

# Responsabilidades

O módulo é responsável por:

- representar intenções
- armazenar intenções
- pesquisar intenções
- organizar metadados
- registrar ferramentas sugeridas

---

# Não é responsabilidade

O módulo NÃO deve:

- interpretar linguagem natural
- executar ferramentas
- consultar banco de dados diretamente
- chamar modelos de IA
- executar workflows

Essas responsabilidades pertencem a outros módulos.

---

# Integração

O módulo será utilizado por:

- Conversation
- Memory
- Planning Engine
- Knowledge Search
- Tool Selector
- Workflow Engine
- Telemetry

---

# Smoke Tests

O módulo possui testes para:

- Intent
- Repository
- Service
- Manager

Todos os testes devem permanecer verdes antes de qualquer alteração arquitetural.

---

# Evolução futura

Na Arquitetura v2.0 estão previstas as seguintes evoluções:

- IntentEntity estruturada
- classificação automática por LLM
- múltiplas intenções simultâneas
- ranking de intenções
- score por modelo
- histórico de classificação
- auditoria
- cache de intenções

---

# Benefícios

A arquitetura adotada proporciona:

- baixo acoplamento
- alta coesão
- facilidade de testes
- reutilização
- escalabilidade
- manutenção simplificada

---

# Dependências

```
IntentManager

↓

IntentService

↓

IntentRepository

↓

Intent
```

O fluxo de dependências é unidirecional.

---

# Status

Status do módulo:

- Entity
- Repository
- Service
- Manager
- Smoke Tests
- Documentação

Todos implementados.

---

# Conclusão

O módulo **Intent** representa a base da interpretação das solicitações do usuário.

Embora nesta versão realize apenas o gerenciamento das intenções, sua arquitetura foi preparada para suportar os próximos componentes cognitivos da Versa AI, como o **Planning Engine**, **Tool Selector** e **Knowledge Search**, mantendo a separação de responsabilidades e a escalabilidade da plataforma.

---

**Autor**

Raphael Wilson

**Projeto**

Versa AI

**Versão**

1.0