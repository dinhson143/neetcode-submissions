class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache.keys():
            return -1
        
        value = self.cache[key]
        del self.cache[key]
        self.cache[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        if len(self.cache) == self.capacity and key not in self.cache.keys():
            # Remove the least recently used key
            first_key = list(self.cache)[0]
            del self.cache[first_key]

        # print(self.cache)
        if key in self.cache.keys():
            del self.cache[key]

        self.cache[key] = value


