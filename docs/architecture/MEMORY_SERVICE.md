# Memory Service

## Objetivo

O MemoryService implementa todas as regras de negócio relacionadas à memória da Versa AI.

Ele atua entre o MemoryManager e os repositórios, centralizando toda a lógica da camada de memória.

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
      ▼
Implementação
```

---

# Responsabilidades

O MemoryService é responsável por:

- armazenar memórias
- recuperar memórias
- atualizar memórias
- remover memórias
- pesquisar memórias
- eliminar memórias expiradas
- fornecer estatísticas

Não é responsabilidade do serviço:

- acessar banco de dados diretamente
- conhecer Supabase
- conhecer Redis
- executar OCR
- acessar APIs
- manipular arquivos

---

# Métodos

## remember()

Armazena uma memória.

```
Memory

↓

Repository.save()
```

---

## recall()

Recupera uma memória através do identificador.

---

## update()

Atualiza uma memória existente.

---

## forget()

Remove uma memória.

---

## get_all()

Retorna todas as memórias.

---

## exists()

Verifica se uma memória existe.

---

## count()

Retorna o total de memórias armazenadas.

---

## clear()

Remove todas as memórias.

---

## cleanup_expired()

Percorre todas as memórias removendo aquelas expiradas.

---

# Fluxo

```
Usuário

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

- separação entre negócio e persistência
- reutilização
- facilidade para testes
- desacoplamento
- evolução simples

---

# Evolução prevista

No futuro o serviço deverá implementar:

- busca semântica
- embeddings
- RAG
- sumarização
- consolidação
- deduplicação
- promoção para Long Term Memory
- arquivamento
- restauração

Sem alterar o MemoryManager.

---

# Testes

```
py -m unittest tests.smoke.test_memory_service
```

Objetivo:

Validar todas as regras básicas do serviço.

---

# Status

| Item | Status |
|------|--------|
| remember() | ✅ |
| recall() | ✅ |
| update() | ✅ |
| forget() | ✅ |
| get_all() | ✅ |
| cleanup_expired() | ✅ |
| Smoke Test | ✅ |

---

Autor

Raphael Wilson

Projeto

Versa AI

Versão

1.0