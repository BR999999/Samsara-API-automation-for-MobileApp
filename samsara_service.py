from pip._vendor import requests


class SamSaraService():
    host = 'https://api.samsara.com'
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer samsara_api_7otN6sz2Iyv9iwp8MFR1hMC2j8ZIk3'
    }
    org_id = 14804

    @classmethod
    def get_all_address(cls):
        url = cls.host + '/addresses'
        return requests.get(url=url, headers=cls.headers)

    @classmethod
    def save_address(cls, payload):
        url = cls.host + '/addresses'
        return requests.post(url=url, json=payload, headers=cls.headers)
