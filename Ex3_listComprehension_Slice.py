# Lists II & For loops & Tuples
# J. Sun

## using range() and append() to create a list in a for loop
print('\nList Comprehension & Slicing\n')
squares = []
for value in range (1,11):
    squares.append(value**2)
print(squares)
print()

##list comprehension
# generates a list of all square from 1 and 10 inclusive
squares = [value**2 for value in range(1, 11)]
print(squares)
print()


# slicing : print elements with the index 0 1 2 3
print('squares[0:4] =', squares[0:4])

# slicing : print element with the index 2
print('squares[2:3] =', squares[2:3])

# slicing : print elements from the start to index 5
print('squares[:6] =', squares[:6])

# slicing : print elements from index 6 to the end
print('squares[6:] =', squares[6:])

# slicing : print last three elements
print('squares[-3:] =', squares[-3:])
print()

# loop throught a slice:
for i in squares[:5]:
    print(f"Prefix-{i}", end = " | ")
print()

# use slicing to create a new distinct list
# that is a duplicate of the old list
x = squares[:]
y = list(squares)
z = squares.copy()
x.append(123)
y.append(456)
z.append(789)

print(x)
print(y)
print(z)
print(squares)
print()
