from app.mappings.priorities import JIRA_TO_ZENDESK_PRIORITY
from app.mappings.statuses import JIRA_TO_ZENDESK_STATUS


def map_priority(priority):
    return JIRA_TO_ZENDESK_PRIORITY.get(priority, "normal")


def map_status(status):
    return JIRA_TO_ZENDESK_STATUS.get(status, "open")