# Managers

## Versa AI

---

# Objetivo

O módulo **Managers** é responsável por gerenciar componentes da Versa AI.

Enquanto os Providers acessam fontes de informação e as Tools executam ações, os Managers coordenam e organizam esses componentes, fornecendo uma interface única para o restante da aplicação.

Todo Manager deve herdar da classe `BaseManager`.

---

# Arquitetura

```
                    BaseManager
                         │
        ┌────────────────┴────────────────┐
        ▼                                 ▼
 ToolManager                     KnowledgeManager
        │                                 │
        ▼                                 ▼
     BaseTool                     BaseProvider
```

No futuro, novos Managers poderão ser adicionados sem alterar a arquitetura existente.

Exemplos:

```
MemoryManager

IntentManager

WorkflowManager

AgentManager

TelemetryManager

ConfigurationManager
```

---

# Estrutura

```
app/
├── managers/
│   └── base_manager.py
│
├── knowledge/
│   └── knowledge_manager.py
│
└── tools/
    └── tool_manager.py
```

Cada Manager é responsável por um único domínio do sistema.

---

# BaseManager

Todos os Managers herdam da classe:

```
BaseManager
```

Ela fornece uma infraestrutura comum para gerenciamento de componentes.

---

## Funcionalidades

A BaseManager implementa automaticamente:

- register()
- unregister()
- get()
- get_all()
- count()
- clear()
- shutdown()

Além disso, disponibiliza:

- logger próprio
- armazenamento interno dos componentes
- gerenciamento padronizado

---

# Responsabilidades

A BaseManager não conhece o tipo do componente.

Ela apenas gerencia seu ciclo de vida.

Cada Manager especializado adiciona apenas regras específicas.

---

# ToolManager

Responsável por gerenciar todas as Tools disponíveis.

Permite:

- registrar Tools
- remover Tools
- localizar Tools
- listar Tools

Não executa Tools.

A execução pertence à própria Tool.

---

# KnowledgeManager

Responsável por gerenciar os Providers da Versa AI.

Sua responsabilidade é:

- registrar Providers
- carregar Providers padrão
- pesquisar conhecimento
- consolidar resultados

O KnowledgeManager nunca consulta diretamente bancos de dados, APIs ou documentos.

Toda consulta é delegada aos Providers.

---

# Fluxo

```
Usuário

↓

KnowledgeManager

↓

Seleciona Providers

↓

Provider.search()

↓

SearchResult

↓

KnowledgeManager

↓

Resposta
```

---

# Como criar um novo Manager

1. Herdar de BaseManager.

Exemplo:

```python
class MemoryManager(BaseManager):
```

2. Adicionar apenas regras específicas.

3. Não reimplementar funcionalidades já existentes na BaseManager.

4. Criar Smoke Test.

5. Criar Teste de Integração.

6. Atualizar esta documentação.

---

# Convenções

Todos os Managers devem seguir o mesmo padrão:

- responsabilidade única
- herança da BaseManager
- documentação completa
- type hints
- docstrings
- baixo acoplamento
- alta coesão

---

# Testes

## Smoke Test

```
py -m unittest tests.smoke.test_managers
```

Objetivo:

Validar a arquitetura básica dos Managers.

---

## Testes de Integração

Os testes de integração garantem que todos os Managers respeitam o contrato definido pela BaseManager.

---

# Roadmap

Managers previstos para a Versa AI:

- ToolManager
- KnowledgeManager
- MemoryManager
- IntentManager
- WorkflowManager
- AgentManager
- TelemetryManager
- ConfigurationManager

---

# Benefícios

A utilização da BaseManager proporciona:

- padronização
- reutilização
- redução de código duplicado
- facilidade para testes
- baixo acoplamento
- manutenção simplificada
- escalabilidade

---

# Conclusão

O módulo Managers representa a camada de orquestração da Versa AI.

Cada Manager possui uma única responsabilidade e coordena componentes especializados, sem conhecer detalhes de implementação.

A BaseManager fornece toda a infraestrutura comum, permitindo que novos Managers sejam adicionados de forma consistente, mantendo a arquitetura simples, modular e escalável.
