# Coding Standards

Este documento define os padrões de desenvolvimento da Versa IA.

---

# Organização

Cada módulo possui apenas uma responsabilidade.

Exemplo:

```
knowledge/

search/

ranking/

providers/
```

Nunca misturar responsabilidades.

---

# Managers

Responsáveis por coordenar componentes.

Exemplo:

```
SearchManager

ToolManager

MemoryManager
```

---

# Providers

Responsáveis pela integração.

Exemplo:

```
OpenAI

Gemini

Internet

Supabase
```

---

# Strategies

Implementam regras específicas.

```
InternetStrategy

PdfStrategy

SupabaseStrategy
```

---

# Entities

Devem conter apenas dados.

Nunca lógica de negócio.

---

# Utils

Devem conter apenas funções reutilizáveis.

Nunca:

- Banco
- IA
- Providers
- APIs
- Regras de negócio

---

# Nomenclatura

Classes

```
PascalCase
```

Arquivos

```
snake_case.py
```

Funções

```
snake_case()
```

Constantes

```
UPPER_CASE
```

---

# Estrutura

Sempre que possível:

```
Manager

↓

Selector

↓

Registry

↓

Implementation
```

---

# SOLID

Todo código novo deve seguir:

- SRP
- OCP
- DIP

---

# Comentários

Documentar:

- Classes públicas
- Métodos públicos
- Fluxos complexos

---

# Logging

Nunca utilizar print().

Sempre utilizar Logger.

---

# Testes

Todo novo módulo deve possuir testes unitários.

---

# Arquitetura

Cada camada conhece apenas a camada imediatamente inferior.

```
VersaAI

↓

Kernel

↓

Orchestrator

↓

Managers

↓

Providers
```

Nunca quebrar essa regra.