from requests import Session
from resusables.data import data


class apimodules:
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
        return self.client.post(url, json=json)
