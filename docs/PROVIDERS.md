# Providers

## Versa AI

---

# Objetivo

O módulo **Providers** é responsável por fornecer acesso padronizado às diversas fontes de conhecimento utilizadas pela Versa AI.

Cada Provider possui apenas uma responsabilidade:

> Consultar uma fonte de dados e retornar os resultados em um formato padronizado.

Os Providers **não executam regras de negócio**, **não processam documentos**, **não realizam ranking** e **não executam automações**.

Sua única responsabilidade é recuperar informações.

---

# Arquitetura

```
                   KnowledgeManager
                           │
                           │
        ┌──────────────────┴──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
 InternetProvider     PDFProvider      APIProvider
        │                  │                  │
        ▼                  ▼                  ▼
 SearchResult       SearchResult      SearchResult

        ▼
 SupabaseProvider

        ▼
 EmailProvider
```

Todos os Providers implementam a mesma interface definida pela classe BaseProvider.

Isso permite que qualquer módulo da Versa AI utilize um Provider sem conhecer sua implementação interna.

---

# Estrutura

```
knowledge/
└── providers/
    ├── api/
    │   └── api_provider.py
    ├── email/
    │   └── email_provider.py
    ├── internet/
    │   └── internet_provider.py
    ├── pdf/
    │   └── pdf_provider.py
    ├── supabase/
    │   └── supabase_provider.py
    └── base_provider.py
```

Cada Provider possui sua própria pasta para permitir futuras expansões.

Exemplo:

```
internet/

internet_provider.py

google_engine.py

bing_engine.py

duckduckgo_engine.py
```

---

# BaseProvider

Todos os Providers devem herdar da classe:

```
BaseProvider
```

A classe base fornece:

- initialize()
- shutdown()
- is_available()

Cada Provider precisa implementar apenas:

```
search()
```

---

# Contrato

Todos os Providers devem obedecer ao seguinte contrato.

## Entrada

```
query: str
```

## Saída

```
SearchResult
```

Nunca retornar:

- list
- dict
- tuple
- object

Todo Provider deve retornar obrigatoriamente um objeto SearchResult.

---

# SearchResult

Todos os Providers retornam:

```
SearchResult
```

A entidade SearchResult encapsula o resultado de uma pesquisa.

Ela contém:

- sucesso da operação
- origem da pesquisa
- documentos encontrados
- tempo de execução
- mensagens de erro

Isso garante que toda a Versa AI trabalhe com um formato único de resposta.

---

# Providers disponíveis

## InternetProvider

Responsável por pesquisas na Internet.

Exemplos:

- Google
- Bing
- DuckDuckGo

---

## PDFProvider

Responsável por pesquisas em documentos PDF.

Será integrado futuramente ao módulo de análise de documentos.

---

## APIProvider

Responsável por consultas em APIs externas.

Exemplos:

- REST
- SOAP
- Serviços internos

---

## SupabaseProvider

Responsável por consultas ao banco de dados corporativo.

Será a principal fonte de conhecimento da Versa AI.

Exemplos:

- clientes
- contratos
- faturas
- memória
- embeddings
- histórico
- workflows

---

## EmailProvider

Responsável por consultas em caixas postais.

Exemplos:

- Outlook
- Microsoft Graph
- IMAP

---

# Responsabilidades

Os Providers apenas consultam informações.

Não devem:

- baixar arquivos
- renomear arquivos
- mover arquivos
- executar scripts
- gerar PDFs
- enviar e-mails
- gravar banco

Essas responsabilidades pertencem ao módulo Tools.

---

# Fluxo

```
Usuário

↓

KnowledgeManager

↓

Seleciona Provider

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

# Como criar um novo Provider

1. Criar uma pasta.

Exemplo:

```
sharepoint/
```

2. Criar:

```
sharepoint_provider.py
```

3. Herdar de BaseProvider.

4. Implementar apenas:

```
search()
```

5. Retornar obrigatoriamente:

```
SearchResult
```

6. Criar Smoke Test.

7. Criar teste de integração.

8. Atualizar esta documentação.

---

# Testes

## Smoke Test

```
py -m unittest tests.smoke.test_providers
```

Objetivo:

Validar que todos os Providers:

- instanciam corretamente
- inicializam
- desligam
- retornam SearchResult

---

## Teste de Integração

```
py -m unittest tests.integration.test_providers
```

Objetivo:

Garantir que todos os Providers respeitam o contrato definido pela BaseProvider.

---

# Convenções

Todos os Providers devem seguir o mesmo padrão.

- um Provider por pasta
- documentação completa
- docstrings
- type hints
- SearchResult como retorno
- herança da BaseProvider

---

# Roadmap

Próximas integrações previstas.

- SharePoint Provider
- OneDrive Provider
- SAP Provider
- Oracle Provider
- SQL Server Provider
- PostgreSQL Provider
- Azure Blob Provider
- Google Drive Provider

---

# Conclusão

O módulo Providers representa a camada de acesso ao conhecimento da Versa AI.

Sua principal responsabilidade é abstrair diferentes fontes de dados por meio de uma interface única e padronizada.

Graças ao uso da BaseProvider e da entidade SearchResult, qualquer componente da Versa AI pode consultar informações sem conhecer detalhes da implementação de cada fonte.

Essa arquitetura reduz o acoplamento, facilita testes, melhora a manutenção e permite adicionar novos Providers sem modificar o restante do sistema.
