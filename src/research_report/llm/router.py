"""LLM routing logic for task-specific model selection."""
from typing import Literal

from .providers import get_groq_llm, get_openai_llm, get_google_llm
from ..models.config import settings
from ..utils.logger import setup_logger

logger = setup_logger(__name__)

TaskType = Literal["planning", "research", "analysis", "writing", "review"]


class LLMRouter:
    """Routes tasks to appropriate LLM based on complexity and requirements."""
    
    def __init__(self):
        """Initialize router with default provider."""
        self.default_provider = settings.default_llm_provider
        logger.info(f"LLM Router initialized with default provider: {self.default_provider}")
    
    def get_llm(self, task_type: TaskType, force_provider: str | None = None):
        """Get appropriate LLM for the task type.
        
        For POC, we use Groq for everything (fast & free).
        Later, you can add routing logic for complex tasks.
        
        Args:
            task_type: Type of task being performed
            force_provider: Override default provider
            
        Returns:
            Configured LLM instance
        """
        provider = force_provider or self.default_provider
        
        logger.info(f"Routing task '{task_type}' to provider: {provider}")
        
        # Task-specific routing (expand this later)
        if provider == "groq":
            return get_groq_llm()
        elif provider == "openai":
            return get_openai_llm()
        elif provider == "google":
            return get_google_llm()
        else:
            logger.warning(f"Unknown provider '{provider}', falling back to Groq")
            return get_groq_llm()


# Global router instance
llm_router = LLMRouter()
