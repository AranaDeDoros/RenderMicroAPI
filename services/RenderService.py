import requests
from pydantic import TypeAdapter

from config import settings
from models.render import (
    RenderPostgresResponse,
    RenderServiceResponse,
    ServiceStateUpdate,
    ServiceStatusChange,
)


class RenderServiceClient:
    
    def __init__(self) -> None:
        self._api_key: str = settings.RENDER_API_KEY
        self._limit: str = settings.RENDER_LIMIT
        self._api_url: str = settings.RENDER_API_URL


    def list_services(self) -> list[RenderServiceResponse]:
        url: str = (
            f"{self._api_url}services?includePreviews=true&limit={self._limit}"
        )

        headers: dict[str, str] = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self._api_key}",
        }

        response: requests.Response = requests.get(url, headers=headers)
        response.raise_for_status()

        return TypeAdapter(
            list[RenderServiceResponse]
        ).validate_python(response.json())
    
    def suspend(self, service_id: str) -> ServiceStateUpdate:
        url: str = (
            f"{self._api_url}services/{service_id}/suspend"
        )

        headers: dict[str, str] = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self._api_key}",
        }

        response: requests.Response = requests.post(url, headers=headers)
        response.raise_for_status()

        return ServiceStateUpdate(
                    service_id=service_id,
                    status_change=ServiceStatusChange.RESTARTED,
                )
    
    def restart(self, service_id: str) -> ServiceStateUpdate:
        url: str = (
            f"{self._api_url}services/{service_id}/restart"
        )

        headers: dict[str, str] = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self._api_key}",
        }

        response: requests.Response = requests.post(url, headers=headers)
        response.raise_for_status()
        
        return ServiceStateUpdate(
            service_id=service_id,
            status_change=ServiceStatusChange.RESTARTED,
        )
    
    def resume(self, service_id: str) -> ServiceStateUpdate:
        url: str = (
            f"{self._api_url}services/{service_id}/resume"
        )

        headers: dict[str, str] = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self._api_key}",
        }

        response: requests.Response = requests.post(url, headers=headers)
        response.raise_for_status()
        
        return ServiceStateUpdate(
            service_id=service_id,
            status_change=ServiceStatusChange.RESTARTED,
        )
    
    def list_postgres_instances(self)  -> list[RenderPostgresResponse]:
            url: str = (
                f"{self._api_url}postgres"
            )
    
            headers: dict[str, str] = {
                "Accept": "application/json",
                "Authorization": f"Bearer {self._api_key}",
            }
            response: requests.Response = requests.get(url, headers=headers)
            response.raise_for_status()
        
            return TypeAdapter(
                        list[RenderPostgresResponse]
                    ).validate_python(response.json())

