# briefbot

Give it a topic, get a sourced research brief. A planner splits the topic into questions,
parallel researchers gather evidence, a writer drafts, and a critic loops until it's good enough,
then a human approves.

> Learning project for **FastAPI + LangChain + LangGraph**, built to run on free tiers.

## Target graph

```
topic -> planner (3-5 sub-questions)
      -> [fan-out] researcher x N   (search + fetch, parallel via Send)
      -> synthesizer -> writer (citations)
      -> critic --fail--> planner (max 2 loops)
             \--pass--> HUMAN REVIEW (interrupt) -> final brief
```

**Current state:** `src/briefbot/graph.py` is a one-node stub. Replacing it is the main learning task.

## Quickstart

```bash
uv sync
cp .env.example .env        # set LLM_PROVIDER and the matching key
uv run uvicorn briefbot.api:app --reload
uv run pytest
uv run ruff check .
```

```bash
curl -X POST localhost:8000/briefs -H 'content-type: application/json' \
  -d '{"topic": "vector databases"}'
```

## LLM providers

All model access goes through `get_llm()` in `src/briefbot/llm.py`. Set `LLM_PROVIDER` to
`gemini`, `groq` or `ollama` (plus `LLM_MODEL`). `fake` is for tests.

## Layout

```
src/briefbot/  config.py  llm.py  graph.py  api.py
tests/
docs/jules-issues.md   # well-scoped issues for Google Jules
```

## Milestones

1. Local, linear: planner, one searcher, writer, `/briefs`, pytest.
2. Real graph: parallel researchers (`Send`), critic loop, SQLite checkpointer, SSE streaming, `interrupt()` approval.
3. Dev env: Docker Compose + Postgres, `.env.dev`, GitHub Actions CI, eval set with LLM judge.
4. Prod: Cloud Run / Fly.io, secrets, rate limits, token and search budget caps, health checks.
