import json


class ResourcesProvider:
    def __init__(self, resources_path):
        self.resources_path = resources_path

    def _get_config_path(self):
        return self.resources_path + "dap.json"

    def load_config(self):
        with open(self._get_config_path(), 'r', encoding='utf-8') as f:
            return json.load(f)

    def get_deals_path(self):
        return self.resources_path + "numbers.json"