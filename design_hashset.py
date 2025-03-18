class MyHashSet:
    
    def __init__(self):
        self.data = []
        

    def add(self, key: int) -> None:
        if key not in self.data:
            return self.data.append(key)
        

    def remove(self, key: int) -> None:
        if key in self.data:
            return self.data.remove(key)
        

    def contains(self, key: int) -> bool:
        return key in self.data
        
        
    


newhash = MyHashSet()
newhash.add(2)
print(newhash.contains(1))

# print(newhash)