from langchain_core.language_models.chat_models import BaseChatModel

from briefbot.config import get_settings


def get_llm(temperature: float = 0.2) -> BaseChatModel:
    """Single place to swap LLM providers via LLM_PROVIDER / LLM_MODEL env vars."""
    s = get_settings()
    provider = s.llm_provider.lower()
    if provider == "gemini":
        from langchain_google_genai import ChatGoogleGenerativeAI

        return ChatGoogleGenerativeAI(
            model=s.llm_model, google_api_key=s.google_api_key, temperature=temperature
        )
    if provider == "groq":
        from langchain_groq import ChatGroq

        return ChatGroq(model=s.llm_model, api_key=s.groq_api_key, temperature=temperature)
    if provider == "ollama":
        from langchain_ollama import ChatOllama

        return ChatOllama(
            model=s.llm_model, base_url=s.ollama_base_url, temperature=temperature
        )
    if provider == "fake":
        from langchain_core.language_models.fake_chat_models import FakeListChatModel

        return FakeListChatModel(responses=["fake response"])
    raise ValueError(f"Unknown LLM_PROVIDER: {s.llm_provider!r}")
