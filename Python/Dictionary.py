from optparse import Values


MyDictionary={
"Deputy":'''the second most important person in a particular organization, who does the work 
of his/her manager if the manager is away''',
"Assignment":'''a job or type of work that you are given to do''',
"Cupboard":'''a piece of furniture, usually with shelves inside and a door or doors at the 
front, used for storing food, clothes, etc.''',
"Heat":'''the feeling of something hot''',
"Prison":'''a building where criminals are kept as a punishment''',
"NestedDictionary":{"Speed":'''fast movement'''},
1:2
}
print(MyDictionary["Assignment"])
print(" ")
print(MyDictionary["Cupboard"])
print(" ")
print(MyDictionary["Deputy"])
print(" ")
print(MyDictionary["Heat"])
print(" ")
print(MyDictionary["Prison"])
print(" ")
print(MyDictionary["NestedDictionary"]["Speed"])
print(" ")
print(MyDictionary[1])
print(" ")
print(list(MyDictionary.keys()))
print(" ")
print(list(MyDictionary.values()))
print(" ")
