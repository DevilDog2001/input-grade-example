# Lists II & For loops & Tuples
# J. Sun

## tuples: ordered sequences of items
print('\nTuples\n')
t = 5, 7, 6, 2
print(t)
print(len(t), max(t), min(t))
print(f'{len(t)} {max(t)}{min(t)}')
print(t[0], t[-1], t[:2])

# tuple slicing:
print(t[-7:7])
print(t[-7:2])
#del t[1:4]  #TypeError: 'tuple' does not support item delection
del t
#print(t)    #NameError: name 't' is not defined

# out of bounds error
#print(t[7])
#print(t[-7])

# creating new tuples
a = 1, 2, 3
b = ('a', 'b', 'c')
c = a + b
t = (a, b, c)
print(t)

tNums = tuple(range(6))
print(tNums[:3])

# use for loop to display items in tuples
for n in tNums[:3]:
    print(n, end = " | ")
print()

fruits = ["apple", "banana", "cherry"]
for item in fruits:
    print(item)
print()
fruits = ["apple", "pear", 'python',]
for item in fruits:
    print(f'{item.title()} is my favorite!')
    print(f'I want to have more {item}.\n')
print()
#PE5_7
#practice
#E
n = -6,7,3,-2,6,3,9
print(len(n),max(n),min(n),sum(n),sep = "\n")
print(f'{len(n)}\n{max(n)}\n{min(n)}\n{sum(n)}') # F-string
print(n.count(3),n.index(3),n[-6:6], sep = "\n") 
print(f'{n.count(3)}\n{n.index(3)}\n{n[-6:6]}')  # F-string
print(n, sorted(n), sep = "\n")
print(f'{n}\n{sorted(n)}') #2 F-string
print()
#Given an integer, , perform the following conditional actions:

#If  is odd, print Weird
#If  is even and in the inclusive range of 2 to 5, print Not Weird
#If  is even and in the inclusive range of 6 to 20, print Weird
#If  is even and greater than 20, print Not Weird


n = int(input().strip())
if n >= 2 and n <=5:
    print("Not weird")
