from .http_client import HttpClient
from .azdo_url_builder import AzdoUrlBuilder
from .secret_provider import SecretProvider


class AzdoHttpClient:
    def __init__(self, azdo_url_builder: AzdoUrlBuilder):
        self._azdo_url_builder = azdo_url_builder
        self._client = HttpClient()
        self._secret_provider = SecretProvider()

    def get_workitem_detail(self, work_item_id: int):
        url = self._azdo_url_builder.build_workitem_detail_url(work_item_id)
        print(url)
        return self._client.get(url=url, headers=self.build_headers())

    def get_wis_with_wiql(self, query: dict[str, str]):
        url = self._azdo_url_builder.build_wiql_url()
        print(url)
        return self._client.post(url=url, headers=self.build_headers(), json=query)

    def get_wis_list(self, ids: list[int]):
        url = self._azdo_url_builder.build_work_items_list_url(ids)
        print(url)
        return self._client.get(url=url, headers=self.build_headers())

    def build_headers(self) -> dict[str, str]:
        return {"Authorization": f"Basic {self._secret_provider.get_secret('API_KEY')}"}
