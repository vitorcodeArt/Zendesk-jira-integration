from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    JIRA_BASE_URL: str
    JIRA_EMAIL: str
    JIRA_TOKEN: str

    ZENDESK_BASE_URL: str
    ZENDESK_EMAIL: str
    ZENDESK_TOKEN: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()