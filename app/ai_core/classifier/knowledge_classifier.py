from app.knowledge.knowledge_source import KnowledgeSource


class KnowledgeRouter:

    SUPABASE_PATTERNS = [

        "cliente",
        "clientes",
        "cpf",
        "cnpj",
        "fatura",
        "segunda via",
        "boleto",
        "pagamento",
        "vencimento",
        "consumo",
        "unidade consumidora",
        "contrato",
        "protocolo"

    ]

    ENERGY_PATTERNS = [

        "aneel",
        "ons",
        "ccee",
        "epe",
        "energia elétrica",
        "energia solar",
        "bandeira tarifária",
        "tarifa",
        "tarifária",
        "tusd",
        "te",
        "kwh",
        "kwp",
        "geração distribuída",
        "geracao distribuida",
        "microgeração",
        "microgeracao",
        "compensação de energia",
        "compensacao de energia"

    ]

    EQUIPMENT_PATTERNS = [

        "growatt",
        "goodwe",
        "solis",
        "fronius",
        "huawei",
        "foxess",
        "deye",
        "inversor",
        "microinversor",
        "string box",
        "painel solar",
        "módulo",
        "modulo",
        "datasheet",
        "manual"

    ]

    EMAIL_PATTERNS = [

        "email",
        "e-mail",
        "gmail",
        "outlook"

    ]

    AUTOMATION_PATTERNS = [

        "automatizar",
        "automação",
        "automacao",
        "baixar",
        "cadastrar",
        "lançar",
        "lancar",
        "executar",
        "processar"

    ]

    def route(self, question: str) -> KnowledgeSource:

        text = question.lower().strip()
        
        if self._is_general_question(text):
            return KnowledgeSource.INTERNET

        if self._contains(text, self.SUPABASE_PATTERNS):
            return KnowledgeSource.SUPABASE

        if self._contains(text, self.ENERGY_PATTERNS):
            return KnowledgeSource.ENERGY

        if self._contains(text, self.EQUIPMENT_PATTERNS):
            return KnowledgeSource.EQUIPMENT

        if self._contains(text, self.EMAIL_PATTERNS):
            return KnowledgeSource.EMAIL

        if self._contains(text, self.AUTOMATION_PATTERNS):
            return KnowledgeSource.AUTOMATION

        return KnowledgeSource.INTERNET

    def _is_general_question(self, text: str) -> bool:

        general_patterns = [

            "quem é",
            "quem foi",
            "qual é",
            "qual foi",
            "quando",
            "onde",
            "quanto foi",
            "presidente",
            "brasil",
            "noruega",
            "história",
            "historia",
            "futebol",
            "copa do mundo"

        ]

        versa_terms = [

            "energia",
            "aneel",
            "tusd",
            "te",
            "bandeira",
            "kwh",
            "kwp"

        ]

        if any(term in text for term in versa_terms):
            return False

        return any(pattern in text for pattern in general_patterns)

    @staticmethod
    def _contains(text: str, patterns: list[str]) -> bool:

        return any(
            pattern in text
            for pattern in patterns
        )