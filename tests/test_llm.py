import pytest

from briefbot import config, llm


def test_fake_provider(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "fake")
    config.get_settings.cache_clear()
    assert llm.get_llm().invoke("hi").content == "fake response"
    config.get_settings.cache_clear()


def test_unknown_provider(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "nope")
    config.get_settings.cache_clear()
    with pytest.raises(ValueError):
        llm.get_llm()
    config.get_settings.cache_clear()
