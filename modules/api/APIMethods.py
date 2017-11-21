from requests import Session
from bases.data import data


class APIMethods:

    def __init__(self):
        self.client = Session()
        self.client.verify = False
        self.client.headers.update({'Content-Type': 'application/json'})

    @staticmethod
    def _kupatana_url():
        _url = 'https://kupatana.com/oc-content/themes/dohi/api/item-phone-number.php'
        return _url

    def get_kupatana_phone_number(self, product_id, json=None):
        if not json:
            json = data.kupatana_phone_number(product_id)
            url = self._kupatana_url()
            resp = self.client.post(url, json=json)
            if resp.status_code is not 200:
                raise ValueError(
                    'Fetching kupartana phone number operation failed: {} \n {}'.format(resp.status_code, resp.json()))
            return resp.json()['data']['phoneNumber']
