"""Configuration models using Pydantic for validation."""
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # LLM API Keys
    groq_api_key: str = Field(..., alias="GROQ_API_KEY")
    openai_api_key: str | None = Field(None, alias="OPENAI_API_KEY")
    google_api_key: str | None = Field(None, alias="GOOGLE_API_KEY")
    
    # Search API
    tavily_api_key: str = Field(..., alias="TAVILY_API_KEY")
    
    # LangSmith (Optional)
    langchain_tracing_v2: bool = Field(False, alias="LANGCHAIN_TRACING_V2")
    langchain_api_key: str | None = Field(None, alias="LANGCHAIN_API_KEY")
    
    # Project Config
    environment: str = Field("development", alias="ENVIRONMENT")
    log_level: str = Field("INFO", alias="LOG_LEVEL")
    
    # LLM Settings
    default_llm_provider: str = "groq"
    default_model: str = "llama-3.1-70b-versatile"
    max_tokens: int = 2048
    temperature: float = 0.7
    
    # Research Settings
    max_search_results: int = 5
    report_max_words: int = 1000  # 2-page report (~500 words per page)
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )


# Global settings instance
settings = Settings()
