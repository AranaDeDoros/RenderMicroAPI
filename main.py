from typing import Annotated
from fastapi import APIRouter, Depends, FastAPI, Path
from models.render import   RenderPostgresResponse, RenderServiceResponse, ServiceStateUpdate
from services.RenderService import RenderServiceClient

app = FastAPI()

router = APIRouter()

app.include_router(router, prefix="/api")

def get_render_service() -> RenderServiceClient:
    return RenderServiceClient()

@app.get("/api/services")
async def services( service: RenderServiceClient = 
                Depends(get_render_service)) ->  list[RenderServiceResponse]:
    return service.list_services()

@app.post("/api/services/{service_id}/suspend")
async def suspend_service( service_id: Annotated[str, Path(title="id of service to suspend")], 
                        service: RenderServiceClient = 
                        Depends(get_render_service)) ->  ServiceStateUpdate:
    return service.suspend(service_id)

@app.post("/api/services/{service_id}/restart")
async def restart_service( service_id: Annotated[str, Path(title="id of service to restart")], 
                        service: RenderServiceClient = 
                        Depends(get_render_service)) ->  ServiceStateUpdate:
    return service.restart(service_id)

@app.post("/api/services/{service_id}/resume")
async def resume_service( service_id: Annotated[str, Path(title="id of service to resume")], 
                        service: RenderServiceClient = 
                        Depends(get_render_service)) ->  ServiceStateUpdate:
    return service.resume(service_id)
    
@app.post("/api/services/list_postgres")
async def list_postgres(  service: RenderServiceClient = 
                        Depends(get_render_service))  -> list[RenderPostgresResponse]:
    return service.list_postgres_instances()



