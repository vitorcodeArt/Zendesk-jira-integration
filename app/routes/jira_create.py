from fastapi import APIRouter

from app.services.jira_service import get_issue
from app.services.zendesk_service import create_ticket
from app.services.mapping_service import (
    map_priority,
    map_status
)

router = APIRouter(prefix="/webhooks/jira")


@router.post("/create")
async def jira_create(payload: dict):

    issue_key = payload["issue_key"]

    issue = await get_issue(issue_key)

    fields = issue["fields"]

    zendesk_payload = {
        "ticket": {
            "subject": fields["summary"],
            "comment": {
                "body": fields.get("description", "")
            },
            "priority": map_priority(
                fields["priority"]["name"]
            ),
            "status": map_status(
                fields["status"]["name"]
            )
        }
    }

    response = await create_ticket(zendesk_payload)

    return {
        "status": "success",
        "ticket": response
    }