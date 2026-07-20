"""
===============================================================================
Versa IA
Company Context

Contexto institucional da empresa.

Este módulo contém informações corporativas permanentes
utilizadas pelo PromptBuilder.

NÃO contém:

- Memória
- Histórico
- Conversas
- Documentos
- RAG

Sua responsabilidade é apenas fornecer
o contexto institucional da Versa Energia.
===============================================================================
"""

from __future__ import annotations

from textwrap import dedent


class CompanyContext:

    def build(self) -> str:

        return dedent(
            """
===============================================================================
CONTEXTO INSTITUCIONAL OFICIAL
===============================================================================

Origem

Site institucional da Versa Energia

https://versaenergia.com.br

Versão

1.0

Este documento representa a descrição institucional oficial da
Versa Energia.

As informações abaixo devem ser consideradas como referência
institucional da empresa.

===============================================================================
EMPRESA
===============================================================================

Nome

Versa Energia

Quem Somos

A Versa Energia é uma empresa brasileira especializada em soluções para o
Mercado Livre de Energia.

Fundada em 2014, iniciou sua trajetória no Rio de Janeiro com o propósito
de oferecer uma gestão especializada para consumidores e geradores de
energia.

Ao longo dos anos expandiu sua atuação para todo o território nacional,
auxiliando empresas de diversos segmentos na gestão de energia e na
migração para o Mercado Livre de Energia.

Especialidades

• Mercado Livre de Energia

• Gestão de Energia

• Comercialização de Energia

• Geração Distribuída

• Autoprodução

• Gestão de Usinas

• Certificados de Energia Renovável

Propósito

Entregar soluções inovadoras e sustentáveis que promovam eficiência
energética, redução de custos e segurança para seus clientes.

Abrangência

Atuação em todo o território nacional.

Site Oficial

https://versaenergia.com.br

===============================================================================
FIM DO CONTEXTO INSTITUCIONAL
===============================================================================
"""
        )