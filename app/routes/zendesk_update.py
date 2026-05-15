from fastapi import APIRouter

router = APIRouter(prefix="/webhooks/zendesk")


@router.post("/update")
async def zendesk_update(payload: dict):

    ticket_id = payload["ticket_id"]

    return {
        "message": "zendesk update recebido",
        "ticket_id": ticket_id
    }