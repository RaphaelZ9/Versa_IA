from enum import Enum


class KnowledgeSource(Enum):

    SUPABASE = "supabase"

    ENERGY = "energy"

    EQUIPMENT = "equipment"

    INTERNET = "internet"

    DOCUMENT = "document"

    EMAIL = "email"

    API = "api"

    AUTOMATION = "automation"

    UNKNOWN = "unknown"