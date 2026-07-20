# Memory Manager

## Objetivo

O MemoryManager é responsável por coordenar todas as operações relacionadas à memória da Versa AI.

Ele atua como ponto de entrada para o restante da aplicação, delegando todas as regras de negócio ao MemoryService.

O MemoryManager não implementa lógica de negócio nem conhece detalhes de persistência.

---

# Arquitetura

```
Application
      │
      ▼
MemoryManager
      │
      ▼
MemoryService
      │
      ▼
BaseMemoryRepository
      │
      ▼
Implementação
```

---

# Responsabilidades

O MemoryManager possui apenas responsabilidades de orquestração.

Entre elas:

- receber solicitações da aplicação
- delegar operações ao MemoryService
- fornecer uma interface única para gerenciamento de memória

Não é responsabilidade do Manager:

- acessar banco de dados
- remover memórias expiradas
- criar embeddings
- classificar memórias
- consolidar conhecimento
- tomar decisões de negócio

Todas essas operações pertencem ao MemoryService.

---

# Métodos

## remember()

Solicita ao MemoryService o armazenamento de uma memória.

---

## recall()

Recupera uma memória pelo identificador.

---

## update()

Solicita atualização de uma memória.

---

## forget()

Solicita remoção de uma memória.

---

## get_all()

Retorna todas as memórias disponíveis.

---

## exists()

Verifica se uma memória existe.

---

## count()

Retorna a quantidade de memórias armazenadas.

---

## clear()

Solicita limpeza completa do repositório.

---

## cleanup_expired()

Solicita ao MemoryService a remoção de memórias expiradas.

---

# Fluxo

```
Application

↓

MemoryManager

↓

MemoryService

↓

Repository

↓

Persistência
```

---

# Benefícios

A utilização do MemoryManager proporciona:

- baixo acoplamento
- separação de responsabilidades
- facilidade para testes
- reutilização
- escalabilidade

A aplicação nunca acessa diretamente o MemoryService ou os repositórios.

Todo acesso ocorre através do MemoryManager.

---

# Dependências

O MemoryManager depende apenas de:

```
MemoryService
```

O MemoryService é responsável por toda a lógica de negócio.

---

# Evolução prevista

O MemoryManager deverá permanecer pequeno mesmo com a evolução da Versa AI.

Novas funcionalidades serão adicionadas ao MemoryService, mantendo o Manager responsável apenas pela orquestração.

Exemplos futuros:

- busca semântica
- memória vetorial
- RAG
- memória de longo prazo
- consolidação automática
- aprendizado contínuo

Nenhuma dessas funcionalidades deverá alterar significativamente o MemoryManager.

---

# Testes

```
py -m unittest tests.smoke.test_memory_manager
```

Objetivo:

Validar que o MemoryManager coordena corretamente o MemoryService.

---

# Status

| Item              | Status |
| ----------------- | ------ |
| remember()        | ✅     |
| recall()          | ✅     |
| update()          | ✅     |
| forget()          | ✅     |
| get_all()         | ✅     |
| exists()          | ✅     |
| count()           | ✅     |
| clear()           | ✅     |
| cleanup_expired() | ✅     |
| Smoke Test        | ✅     |

---

# Padrões utilizados

- Clean Architecture
- SOLID
- Dependency Inversion
- Domain Driven Design (DDD)
- Manager Pattern
- Service Layer Pattern
- Repository Pattern

---

# Estrutura do módulo Memory

```
app/
└── memory/
    ├── repositories/
    │   ├── base_memory_repository.py
    │   └── in_memory_repository.py
    │
    ├── services/
    │   └── memory_service.py
    │
    └── memory_manager.py
```

---

# Conclusão

O MemoryManager representa a camada de orquestração do módulo de memória da Versa AI.

Seu papel é fornecer uma interface única para a aplicação, mantendo todas as regras de negócio concentradas no MemoryService e toda a persistência encapsulada pelos repositórios.

Essa arquitetura garante uma solução modular, desacoplada e preparada para evoluções futuras.

---

Autor

Raphael Wilson

Projeto

Versa AI

Versão

1.0
