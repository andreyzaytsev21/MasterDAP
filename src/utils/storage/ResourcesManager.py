import json


class ResourcesProvider:
    def __init__(self, resources_path):
        self.resources_path = resources_path

    def _get_config_path(self):
        return self.resources_path + "dap.json"

    def _get_deals_path(self):
        return self.resources_path + "numbers.json"

    def _replace_deals(self, new_deals_json):
        file_pointer = open(self._get_deals_path(), 'w', encoding='utf-8')
        file_pointer.write(str(json.dumps(new_deals_json, ensure_ascii=False, sort_keys=True, indent=4)))
        file_pointer.close()

    def load_config(self):
        with open(self._get_config_path(), 'r', encoding='utf-8') as f:
            return json.load(f)

    def put_deal(self, deal_number: str, deal_json):
        deals = self.load_deals()
        deals[deal_number] = deal_json
        self._replace_deals(deals)

    def remove_deal(self, deal_number: str):
        deals = self.load_deals()
        del deals[deal_number]
        self._replace_deals(deals)

    def load_deals(self):
        file_pointer = open(self._get_deals_path(), 'r', encoding='utf-8')
        deals = json.load(file_pointer)
        file_pointer.close()
        return deals