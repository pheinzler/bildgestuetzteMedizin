#!/usr/bin/python3

class MyClass:
    dic = {}
    def add_entry(self, lis:list):
        self.dic[len(self.dic) + 1] = lis
    def getListWithElement(self, ele):
        lis = []
        for x in self.dic.values():
            if ele in x:
                lis = x
        return lis
    def average(self):
        lis = [y for ele in self.dic.values() for y in ele]
        return sum(lis)/len(lis)
    def median(self):
        lis = [y for ele in self.dic.values() for y in ele]
        lis.sort()
        if len(lis) % 2 == 0:
            return (lis[int(len(lis)/2 - 1)] + lis[int(len(lis)/2)])/ 2
        return lis[int((len(lis)+1)/2) - 1]
    def __repr__(self) -> str:
        return str(self.dic)    
    __str__ = __repr__

myclass = MyClass()
myclass.add_entry([1,8,3])
myclass.add_entry([12,3,4])
myclass.add_entry([3,4,17])
myclass.add_entry([7,35,16])
print(myclass)
print(myclass.getListWithElement(35))
print(myclass.average())
print(myclass.median())
