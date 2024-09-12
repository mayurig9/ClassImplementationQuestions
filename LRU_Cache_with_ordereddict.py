from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.cache =OrderedDict()
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.cache[key]=value
        self.cache.move_to_end(key)
    
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


ob = LRUCache(3)
param_1 = ob.get(2)
print(param_1)
ob.put(1,"One")
ob.put(2,"Two")
ob.put(4,"Four")
param5 = ob.get(2)
param6 = ob.get(1)
ob.put(3,"Three")
print(ob.cache)
