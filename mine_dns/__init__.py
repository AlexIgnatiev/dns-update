from functools import cached_property

from pydantic import BaseSettings


class Settings(BaseSettings):
    dns_url: str = "https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{record_id}"
    cf_api_key: str
    zone_id: str = "7de91979b718ff54a910029690afc9d8"
    record_id: str = "3479e463f2a418d3e2e9486a51de121b"

    @property
    def update_record_endpoint(self):
        return self.dns_url.format(zone_id=self.zone_id, record_id=self.record_id)


settings = Settings()
