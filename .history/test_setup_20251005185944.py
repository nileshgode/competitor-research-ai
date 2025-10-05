"""Test basic setup and configuration."""
from src.research_report import settings, llm_router
from src.research_report.utils.logger import setup_logger

logger = setup_logger(__name__)


def test_config():
    """Test configuration loading."""
    logger.info("Testing configuration...")
    print(f"Environment: {settings.environment}")
    print(f"Default LLM: {settings.default_llm_provider}")
    print(f"Default Model: {settings.default_model}")
    print(f"Groq API Key loaded: {bool(settings.groq_api_key)}")
    print(f"Tavily API Key loaded: {bool(settings.tavily_api_key)}")


def test_llm():
    """Test LLM initialization."""
    logger.info("Testing LLM initialization...")
    llm = llm_router.get_llm("planning")
    response = llm.invoke("Say 'Hello, LangGraph!' in one sentence.")
    print(f"\nLLM Response: {response.content}")


if __name__ == "__main__":
    test_config()
    print("\n" + "="*50 + "\n")
    test_llm()
    print("\n✅ Phase 2 Setup Complete!")
