from fastapi import APIRouter
import json

from app.services.zendesk_service import create_ticket
from app.services.mapping_service import (
    map_priority,
    map_status
)
from app.services.jira_service import (
    get_issue,
    extract_description_text
)

router = APIRouter(prefix="/webhooks/jira")


@router.post("/create")
async def jira_create(payload: dict):

    issue_key = payload["issue_key"]

    issue = await get_issue(issue_key)
    # print(issue)
    
    with open("jira_response.json", "w") as f:
        json.dump(issue, f, indent=2, default=str)

    fields = issue["fields"]

    zendesk_payload = {
        "ticket": {
            "subject": f'[{issue_key}] - {fields["summary"]}',
            "comment": {
               "body": extract_description_text(
                    fields.get("description")
                )
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