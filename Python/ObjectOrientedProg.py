# Classes are like scripatable objects
class Number:
    def  sum(self):
        return self.a +self.b

num=Number()
num.a=12
num.b=34
s=num.sum()
print(s)

PouchPosition="The pouch is kept in the bag."
class FindingPouch:
    def findpouch(self):
        return PouchPosition

PouchLocation=FindingPouch()
p=PouchLocation.findpouch()
print(p)
