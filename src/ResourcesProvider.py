class ResourcesProvider:
    def __init__(self, resourcesPath):
        self.resourcesPath = resourcesPath

    def getConfigPath(self):
        return self.resourcesPath + "dap.json"

    def getDealsPath(self):
        return self.resourcesPath + "numbers.json"