from . import AbstractInput


class AsperaInput(AbstractInput):

    def __init__(self, host, username, password, min_bandwidth=None, max_bandwidth=None, id_=None,
                 custom_data=None, name=None, description=None):
        super().__init__(id_=id_, custom_data=custom_data, name=name, description=description)
        self.host = host
        self.username = username
        self.password = password
        self.minBandwidth = min_bandwidth
        self.maxBandwidth = max_bandwidth

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        host = json_object['host']
        username = json_object.get('username')
        password = json_object.get('password')
        min_bandwidth = json_object.get('minBandwidth')
        max_bandwidth = json_object.get('maxBandwidth')
        name = json_object.get('name')
        description = json_object.get('description')

        aspera_input = AsperaInput(
            host=host, username=username, password=password,
            min_bandwidth=min_bandwidth, max_bandwidth=max_bandwidth, id_=id_, name=name, description=description)

        return aspera_input
