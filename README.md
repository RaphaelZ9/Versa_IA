# 🤖 Versa IA

Versa IA É uma plataforma de inteligência operacional especializada no setor elétrico, capaz de compreender contexto, responder dúvidas técnicas, executar tarefas, orquestrar automações e integrar sistemas corporativos utilizando linguagem natural.

---

# Principais Características

- Arquitetura modular
- Suporte a múltiplos LLMs
  - OpenAI
  - Gemini
  - Anthropic
  - Ollama
- Sistema de Memória
- Planejamento de Execução (Planning Engine)
- Sistema de Ferramentas (Tools)
- Busca Inteligente (Knowledge Search)
- RAG (Retrieval Augmented Generation)
- Suporte a Providers
- Cache
- Telemetria
- Automações
- Agentes Especializados

---

# Arquitetura

A Versa IA é organizada em módulos independentes.

```
Usuário
    │
    ▼
VersaAI
    │
    ▼
VersaKernel
    │
    ▼
Chat Orchestrator
    │
    ├── Planning
    ├── Knowledge
    ├── Memory
    ├── AI
    ├── Tools
    └── Context
```

Mais detalhes podem ser encontrados em:

```
docs/ARCHITECTURE.md
```

---

# Estrutura do Projeto

```
Versa-AI/

app/
docs/
logs/
tests/

main.py
README.md
requirements.txt
```

---

# Tecnologias

- Python 3.12+
- OpenAI
- Google Gemini
- Anthropic Claude
- Ollama
- Supabase
- PostgreSQL
- REST APIs

---

# Execução

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute:

```bash
python main.py
```

---

# Objetivos do Projeto

A Versa IA foi concebida para ser uma plataforma de IA corporativa capaz de:

- Conversar com usuários
- Consultar documentos
- Executar ferramentas
- Integrar ERPs
- Consultar APIs
- Automatizar processos
- Utilizar memória de curto e longo prazo
- Planejar tarefas complexas
- Trabalhar com múltiplos modelos de IA

---

# Filosofia

A Versa IA segue alguns princípios fundamentais:

- Responsabilidade Única
- Baixo Acoplamento
- Alta Coesão
- Arquitetura Modular
- Fácil Extensão
- Providers Plugáveis
- Estratégias Independentes

Cada módulo possui apenas uma responsabilidade.

---

# Licença

Projeto privado.
