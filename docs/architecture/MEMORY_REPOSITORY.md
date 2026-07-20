# Memory Repository

## Objetivo

O Memory Repository é responsável exclusivamente pela persistência das memórias da Versa AI.

Seu objetivo é abstrair completamente a tecnologia de armazenamento utilizada, permitindo que o restante da aplicação trabalhe apenas com objetos do domínio (`Memory`), sem conhecer detalhes de implementação.

---

# Responsabilidades

O repositório deve ser responsável apenas por operações de persistência.

Exemplos:

- Salvar uma memória
- Atualizar uma memória
- Remover uma memória
- Recuperar uma memória
- Listar memórias
- Verificar existência
- Limpar o armazenamento

Não é responsabilidade do repositório:

- Criar regras de negócio
- Classificar memórias
- Definir prioridades
- Consolidar informações
- Criar embeddings
- Promover memórias para Long Term
- Aplicar Inteligência Artificial

Essas responsabilidades pertencem ao MemoryService.

---

# Arquitetura

```
                MemoryManager
                       │
                       ▼
                MemoryService
                       │
                       ▼
           BaseMemoryRepository
                       │
        ┌──────────────┴──────────────┐
        ▼                             ▼
InMemoryRepository        SupabaseMemoryRepository
                                      │
                                      ▼
                                 PostgreSQL
```

---

# BaseMemoryRepository

Define o contrato que todas as implementações deverão seguir.

Métodos obrigatórios:

```
save()

update()

delete()

get_by_id()

get_all()

exists()

count()

clear()
```

---

# InMemoryRepository

Primeira implementação concreta do repositório.

Características:

- Armazenamento em memória RAM
- Não realiza persistência
- Ideal para desenvolvimento
- Ideal para testes automatizados
- Não possui dependência externa

Estrutura interna:

```
dict[str, Memory]
```

A utilização de um dicionário proporciona busca em tempo constante (O(1)) através do identificador da memória.

---

# Implementações futuras

## SupabaseMemoryRepository

Persistência definitiva das memórias.

Responsável por:

- Inserção
- Atualização
- Exclusão
- Consulta
- Indexação

---

## RedisMemoryRepository

Persistência temporária.

Utilizado para:

- Cache
- Working Memory
- Sessões
- Dados temporários

---

# Fluxo

```
Memory

↓

MemoryService

↓

BaseMemoryRepository

↓

Implementação

↓

Banco de dados
```

---

# Benefícios

Separação completa entre:

- Domínio
- Regras de negócio
- Persistência

Permite substituir a tecnologia de armazenamento sem modificar qualquer regra de negócio.

---

# Boas práticas

Os repositórios nunca devem:

- Chamar APIs
- Criar embeddings
- Realizar OCR
- Tomar decisões
- Alterar prioridades
- Eliminar memórias expiradas

Sua única responsabilidade é persistir e recuperar objetos.

---

# Padrões utilizados

- Clean Architecture
- Repository Pattern
- SOLID
- Dependency Inversion
- Domain Driven Design (DDD)

---

# Evolução prevista

```
BaseMemoryRepository
        │
        ├───────────────┐
        ▼               ▼
 InMemory      Supabase
        │               │
        └───────┬───────┘
                ▼
         MemoryService
                ▼
         MemoryManager
```

---

# Status

| Item | Status |
|------|--------|
| BaseMemoryRepository | ✅ |
| InMemoryRepository | ✅ |
| Smoke Test | ✅ |
| SupabaseRepository | 🔄 Futuro |
| RedisRepository | 🔄 Futuro |

---

Autor

Raphael Wilson

Projeto

Versa AI

Versão

1.0