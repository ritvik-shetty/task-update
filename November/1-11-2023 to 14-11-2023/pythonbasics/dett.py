a={1,4,5,1} # A set is similar to a dictionary but repetation isn't allowed
print(a)

b=set()   # to create an empty set we use this syntax
# print(type(b))

b.add(4)

b.add((4,5))  # We can add a tupple as it is immutable. We cant add any of the mutable data types like list dictionaty etc.
b.add((4,5))  # We can add any item only once. Repetative isnt allowed. 


print(b)
print(len(b))

# b.remove((4,5))
b.pop()
print(b)
print(len(b))


print(b.union({2,11}))