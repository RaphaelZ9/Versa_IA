from dataclasses import dataclass


@dataclass(frozen=True)
class Config:

    # Aplicação
    APP_NAME: str = "Versa IA"
    VERSION: str = "0.1.0"
    ENVIRONMENT: str = "development"

    # Ollama
    OLLAMA_HOST: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "qwen2.5:3b"

    # Logs
    LOG_LEVEL: str = "INFO"

    # Banco de Dados (Supabase)
    SUPABASE_URL: str = ""
    SUPABASE_KEY: str = ""

    # Memória
    MAX_HISTORY: int = 20