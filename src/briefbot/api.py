import uuid

from fastapi import FastAPI
from pydantic import BaseModel, Field

from briefbot.graph import build_graph

app = FastAPI(title="briefbot")
_graph = build_graph()
_briefs: dict[str, dict] = {}  # in-memory for now; swap for a checkpointer/DB later


class BriefRequest(BaseModel):
    topic: str = Field(min_length=3, max_length=300)


class BriefResponse(BaseModel):
    id: str
    topic: str
    draft: str


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/briefs", response_model=BriefResponse, status_code=201)
def create_brief(req: BriefRequest) -> BriefResponse:
    result = _graph.invoke({"topic": req.topic})
    brief = {"id": uuid.uuid4().hex, "topic": req.topic, "draft": result["draft"]}
    _briefs[brief["id"]] = brief
    return BriefResponse(**brief)
