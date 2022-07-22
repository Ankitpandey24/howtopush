from hashlib import new
from itertools import count
from os import remove


countries=['India','Australia','America','Spain','Russia']
# print(countries[2])
# print(countries[3][0])
# print(countries[1:])
# print(countries[:3])
# print(countries[-1])  #TO GET ELEMENT FROM LAST

#                                      METHODS

list1=[3,7,1.6,4,5]
list2=['apple','banana','oranges','pineapple','cherry']
list1.extend(list2)
print(list1)
list2.append('guava')
print(list2)
list2.insert(2,'mango')
print(list2)
list2.remove('oranges')
print(list2)
print(list2.index('cherry'))
list3=[2,3,4,6,8,1]
list3.sort()
print(list3)
list2.pop()
print(list2)
print(list2.pop(2))