from fastapi import FastAPI

from app.routes.jira_create import router as jira_create_router
from app.routes.jira_update import router as jira_update_router
from app.routes.zendesk_update import router as zendesk_update_router

app = FastAPI()

app.include_router(jira_create_router)
app.include_router(jira_update_router)
app.include_router(zendesk_update_router)


@app.get("/")
async def home():
    return {"status": "online"}