class TimeMap:

    def __init__(self):
        self.data = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[f"{key}_{timestamp}"] = value

    def get(self, key: str, timestamp: int) -> str:
        key_pattern = f"{key}_{timestamp}"
        result = self.data.get(key_pattern, "")
        if result is not "":
            return result

        arr = []
        dem = 0
        for item in self.data.keys():
            if f"{key}_" in item:
                if int(item.split("_")[1]) < timestamp:
                    arr.append(self.data.get(item))
                else:
                    dem += 1

        if dem > 0 and len(arr) <= 0:
            return ""

        result = arr.pop() if len(arr) > 0 else ""
        print(result)
        return result
        
