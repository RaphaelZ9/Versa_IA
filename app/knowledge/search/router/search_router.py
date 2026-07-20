class SearchRouter:
    """
    Responsável por decidir se uma pergunta
    necessita de pesquisa externa.
    """

    def should_search(self, question: str) -> bool:

        question = question.lower()

        palavras_chave = [

            "hoje",
            "agora",
            "atualmente",

            "último",
            "ultima",
            "ultimas",
            "últimas",

            "cotação",
            "cotacao",

            "notícia",
            "noticias",
            "notícias",

            "clima",
            "tempo",

            "resultado",
            "placar",

            "quem ganhou",
            "quem é",
            "quem foi",

            "presidente",

            "valor",
            "preço",
            "preco",

            "quando",
            "onde",
            "qual o valor"
        ]

        return any(
            palavra in question
            for palavra in palavras_chave
        )