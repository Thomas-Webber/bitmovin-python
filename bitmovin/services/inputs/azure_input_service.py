from bitmovin.resources.models import AzureInput
from ..rest_service import RestService
from .analyse_service import AnalyzeService


class Azure(RestService, AnalyzeService):
    BASE_ENDPOINT_URL = 'encoding/inputs/azure'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=AzureInput)
