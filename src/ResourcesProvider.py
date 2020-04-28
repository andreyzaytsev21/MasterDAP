class ResourcesProvider:
    def __init__(self, resources_path):
        self.resources_path = resources_path

    def getConfigPath(self):
        return self.resources_path + "dap.json"

    def getDealsPath(self):
        return self.resources_path + "numbers.json"