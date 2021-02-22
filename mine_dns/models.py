import enum
from ipaddress import IPv4Address
from typing import Any

from pydantic import BaseModel


class RecordType(str, enum.Enum):
    A = "A"
    AAAA = "AAAA"
    CNAME = "CNAME"


class UpdateDNSIn(BaseModel):
    ip: IPv4Address


class DNSRecordPayload(BaseModel):
    type: RecordType = RecordType.A
    name: str = "mine.amalta.xyz"
    content: IPv4Address
    ttl: int = 1  # 1 for auto
    proxied: bool = True


class DNSRecordResponse(BaseModel):
    success: bool
    errors: list
    messages: list
    result: dict[str, Any]
