import httpx
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder

from mine_dns import settings
from mine_dns.models import UpdateDNSIn, DNSRecordPayload, DNSRecordResponse

router = APIRouter()


@router.post("/update-dns")
async def update_dns(data: UpdateDNSIn):
    async with httpx.AsyncClient() as client:
        result = await client.put(
            settings.update_record_endpoint,
            headers={"authorization": f"Bearer {settings.cf_api_key}"},
            json=jsonable_encoder(DNSRecordPayload(content=data.ip).dict())
        )
        result.raise_for_status()
        result = DNSRecordResponse(**result.json())
        if not result.success:
            raise HTTPException(status_code=500, detail=f"errors: {result.dict()}")
        return result
