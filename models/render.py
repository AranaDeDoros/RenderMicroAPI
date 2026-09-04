from datetime import datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

from common.helpers import render_to_camel

# ---------------------------------------------------------------------------
# Base
# ---------------------------------------------------------------------------

class RenderServiceModel(BaseModel):
    model_config = ConfigDict(
        alias_generator=lambda field_name: "".join(
            word.capitalize() if i else word
            for i, word in enumerate(field_name.split("_"))
        ),
        populate_by_name=True,
    )

class ServiceType(str, Enum):
    WEB_SERVICE = "web_service"
    STATIC_SITE = "static_site"
    BACKGROUND_WORKER = "background_worker"
    CRON_JOB = "cron_job"
    PRIVATE_SERVICE = "private_service"


class ServiceStatus(str, Enum):
    SUSPENDED = "suspended"
    NOT_SUSPENDED = "not_suspended"

class ServiceDetails(RenderServiceModel):
    build_command: str | None = None
    publish_path: str | None = None
    url: str | None = None
    build_plan: str | None = None
    pull_request_previews_enabled: str | None = None
    
    
class RenderService(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        extra="ignore",
    )

    id: str
    name: str
    type: ServiceType
    suspended: ServiceStatus | None = None

    branch: str | None = None
    repo: str | None = None

    created_at: datetime
    updated_at: datetime
    
    dashboard_url : str
    
    service_details: ServiceDetails | None = None

class RenderServiceResponse(BaseModel):
    service: RenderService
    cursor: str | None = None
    
class ServiceStatusChange(str, Enum):
    SUSPENDED = "suspended"
    RESUMED = "resumed"
    RESTARTED = "restarted"
    
class ServiceStateUpdate(BaseModel):
    service_id : str
    status_change: ServiceStatusChange
    @property
    def message(self):
        return  f"{self.service_id} {self.status_change.value}"



class PostgresInstance(BaseModel):
    model_config = ConfigDict(
        alias_generator=render_to_camel,
        populate_by_name=True,
        extra="ignore",
    )
    
    id: str
    plan : str
    disk_size_gb: int | None = None # free accounts seem to get null
    region: str
    name: str
    created_at : datetime
    updated_at : datetime
    expires_at : datetime
    

class RenderPostgresResponse(BaseModel):
    postgres: PostgresInstance
    cursor: str | None = None