## dictionary

d ={'name':'Teja','age':29,'address':'Hyderabad','Male':True}
print(d['age'])
# print via index
for i in d:
    print(i,d[i])
# print keys
for i in d.keys():
    print(i)
# print only values
for i in d.values():
    print(i)
# print key value pair
for k,v in d.items():
    print(k,v)
# changing values
d['name'] = 'Krishna'
print(d)

# search key
print('name' in d)
# serach value
print('Krishna' in d.values())

## Sets - for unordered unique elements
a=set("123456797")
b=set("456")
print(a^b)
