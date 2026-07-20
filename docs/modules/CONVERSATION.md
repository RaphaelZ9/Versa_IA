# Versa AI

# Conversation Module

---

## Objetivo

O módulo **Conversation** é responsável por representar, armazenar e gerenciar o histórico de conversas da Versa AI.

Ele mantém todas as mensagens trocadas entre o usuário, a inteligência artificial, ferramentas e componentes internos do sistema.

Este módulo constitui um dos pilares do domínio da plataforma, juntamente com **Memory** e **Intent**.

---

# Arquitetura

```
ConversationManager
        │
        ▼
ConversationService
        │
        ▼
ConversationRepository
        │
        ▼
Conversation
        │
        ▼
Message
```

---

# Estrutura do módulo

```
app/

domain/
└── entities/
    └── conversation/
        ├── conversation.py
        └── message.py

conversation/
├── repositories/
│   ├── base_conversation_repository.py
│   └── in_memory_repository.py
│
├── services/
│   └── conversation_service.py
│
└── conversation_manager.py
```

---

# Componentes

## Message

Representa uma única mensagem pertencente a uma conversa.

Contém informações como:

- identificador
- papel (role)
- conteúdo
- metadados
- data de criação

Os papéis atualmente suportados são:

- user
- assistant
- system
- tool

---

## Conversation

Representa uma conversa completa.

Cada conversa possui:

- identificador
- título
- lista de mensagens
- metadados
- data de criação
- data de atualização

A Conversation é responsável pelo ciclo de vida das mensagens que contém.

---

## BaseConversationRepository

Contrato base para persistência de conversas.

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

- find_by_title
- find_by_metadata
- find_with_messages

---

## MemoryConversationRepository

Implementação utilizando memória RAM.

Destinado a:

- desenvolvimento
- testes
- execução local

Não realiza persistência permanente.

---

## ConversationService

Responsável pelas regras de negócio relacionadas às conversas.

Além das operações básicas, disponibiliza funcionalidades específicas do domínio:

- append_message
- last_message
- message_count
- clear_messages

---

## ConversationManager

Interface pública do módulo.

Coordena o ConversationService e representa o ponto de entrada para os demais componentes da Versa AI.

---

# Fluxo

```
Usuário

↓

ConversationManager

↓

ConversationService

↓

ConversationRepository

↓

Conversation

↓

Message
```

---

# Casos de uso

## Conversa simples

```
Usuário

↓

"Olá"

↓

Conversation

↓

Message(user)

↓

Resposta da IA

↓

Message(assistant)
```

---

## Histórico de conversa

```
Conversation

├── Message 1
├── Message 2
├── Message 3
├── Message 4
└── Message N
```

---

## Context Builder (futuro)

```
Conversation

↓

Últimas mensagens

↓

Context Builder

↓

Planning Engine
```

---

# Responsabilidades

O módulo é responsável por:

- armazenar conversas
- armazenar mensagens
- recuperar histórico
- organizar metadados
- controlar o ciclo de vida das mensagens

---

# Não é responsabilidade

O módulo NÃO deve:

- interpretar intenções
- consultar memória
- pesquisar conhecimento
- executar ferramentas
- chamar modelos de IA
- montar prompts

Essas responsabilidades pertencem a outros módulos.

---

# Integração

O módulo será utilizado por:

- Intent
- Memory
- Context Builder
- Planning Engine
- Prompt Builder
- Knowledge Search
- Tool Selector

---

# Smoke Tests

O módulo possui testes para:

- Message
- Conversation
- Repository
- Service
- Manager

Todos os testes devem permanecer verdes antes de alterações estruturais.

---

# Evolução futura

Na Arquitetura v2.0 estão previstas as seguintes evoluções:

- ConversationSerializer
- resumo automático
- paginação de mensagens
- anexos
- imagens
- áudio
- chamadas de ferramentas
- contabilização de tokens
- custo por conversa
- múltiplos participantes
- persistência em banco de dados

---

# Benefícios

A arquitetura adotada proporciona:

- baixo acoplamento
- alta coesão
- separação de responsabilidades
- facilidade de testes
- escalabilidade
- manutenção simplificada

---

# Dependências

```
ConversationManager

↓

ConversationService

↓

ConversationRepository

↓

Conversation

↓

Message
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

O módulo **Conversation** representa o histórico oficial das interações realizadas pela Versa AI.

Sua arquitetura foi projetada para fornecer uma base sólida para os componentes cognitivos da plataforma, permitindo que futuras funcionalidades, como o Context Builder, Planning Engine e Prompt Builder, utilizem o histórico das conversas de forma consistente, desacoplada e escalável.

---

## Autor

Raphael Wilson

## Projeto

Versa AI

## Versão

1.0
