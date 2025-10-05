"""LLM provider configurations and initialization."""
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

from ..models.config import settings
from ..utils.logger import setup_logger

logger = setup_logger(__name__)


def get_groq_llm(model: str | None = None, temperature: float | None = None):
    """Initialize Groq LLM.
    
    Args:
        model: Model name (default from settings)
        temperature: Temperature setting (default from settings)
    """
    return ChatGroq(
        api_key=settings.groq_api_key,
        model=model or settings.default_model,
        temperature=temperature or settings.temperature,
        max_tokens=settings.max_tokens,
    )


def get_openai_llm(model: str = "gpt-4o", temperature: float | None = None):
    """Initialize OpenAI LLM (for future use).
    
    Args:
        model: Model name
        temperature: Temperature setting
    """
    if not settings.openai_api_key:
        raise ValueError("OpenAI API key not configured")
    
    return ChatOpenAI(
        api_key=settings.openai_api_key,
        model=model,
        temperature=temperature or settings.temperature,
        max_tokens=settings.max_tokens,
    )


def get_google_llm(model: str = "gemini-1.5-flash", temperature: float | None = None):
    """Initialize Google Gemini LLM (for future use).
    
    Args:
        model: Model name
        temperature: Temperature setting
    """
    if not settings.google_api_key:
        raise ValueError("Google API key not configured")
    
    return ChatGoogleGenerativeAI(
        api_key=settings.google_api_key,
        model=model,
        temperature=temperature or settings.temperature,
        max_tokens=settings.max_tokens,
    )
