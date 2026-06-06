import time

class Store:
    def __init__(self):
        self.data = {}
        self.expiry = {}

    def set(self, key, value, ttl=None):
        self.data[key] = value
        if ttl:
            self.expiry[key] = time.time() + ttl
        elif key in self.expiry:
            del self.expiry[key]

    def get(self, key):
        if key in self.expiry and time.time() > self.expiry[key]:
            del self.data[key]
            del self.expiry[key]
            return None
        return self.data.get(key)

    def delete(self, key):
        self.data.pop(key, None)
        self.expiry.pop(key, None)
        return 1

    def exists(self, key):
        return key in self.data