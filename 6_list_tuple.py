## Lists - mutable

# basic List
l = [45,56,30,23,46,34,78,33,10,11]

#print full list
print(l)
#print one element based on index
print(l[2])
# print few elements with start end
print(l[2:5])
# print elements with step
print(l[2:8:2])

# changing values
print(l[3])
l[3]=100
print(l[3])

# adding elements at the end
l.append(99)
print(l)
# add element at a location
l.insert(3,50)
print(l)
# remove element
l.remove(34)
print(l)
# search for an element
print(l.index(50))


# generate list with range function
r = list(range(10))
print(r)
r = list(range(2,5))
print(r)
r = list(range(2,10,3))
print(r)

## tupes - immutable
t = (1,2,3)
print(t)
t[0] = 10  # throws error
