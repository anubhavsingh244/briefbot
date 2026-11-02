# Starter issues for Jules

Copy each into a GitHub issue. Each is self-contained with acceptance criteria.
Do not touch `src/briefbot/graph.py` (owner is writing it).

## 1. Dockerfile and Docker Compose
Add a multi-stage `Dockerfile` (uv, python 3.12-slim, non-root user) and `docker-compose.yml`
with services `app` (port 8000) and `postgres` (16, with a named volume). Add `.env.dev.example`.
**Done when:** `docker compose up --build` serves `GET /health` -> `{"status":"ok"}` on :8000, and README has a "Docker" section.

## 2. GitHub Actions CI
Add `.github/workflows/ci.yml` triggered on PRs and pushes to main: `uv sync --frozen`,
`uv run ruff check .`, `uv run ruff format --check .`, `uv run pytest`. Cache uv. Use `LLM_PROVIDER=fake`.
**Done when:** workflow passes on a PR and a status badge is in the README.

## 3. Eval dataset
Create `evals/topics.jsonl` with 20 diverse topics (fields: `topic`, `expected_aspects` list,
`difficulty`). Add `evals/run_evals.py` that calls `POST /briefs` for each and prints a table;
include an `llm_judge()` function scoring 1-5 on coverage and citations via `get_llm()`.
**Done when:** `uv run python evals/run_evals.py --limit 3` runs with `LLM_PROVIDER=fake` and has a unit test for the loader.

## 4. Docs
Add `docs/architecture.md` with a Mermaid diagram of the target graph and a glossary of
LangGraph terms used (state, reducer, Send, checkpointer, interrupt).
**Done when:** diagram renders on GitHub.

## 5. Dependency and lint hygiene (recurring)
Run `uv lock --upgrade`, fix any breakage, keep tests green.
