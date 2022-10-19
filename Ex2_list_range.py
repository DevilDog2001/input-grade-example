# Lists II & For loops & Tuples
# J. Sun

##using list() & range()
print('\nlist() & range()\n')

#using range() and list() to make a list of numbers
numbers = list(range(1, 10))
print(numbers)
print()

#using for loop to print each element in the list
for x in numbers:
    print(x)
print()

#using for loop and range() to print each element in the list
for x in range(3):
    print(x)
print()

for x in range(3, 10):
    print(x)
print()

for x in range(3, 10, 2):
      print(x)
print()

#else block executes when the loop is finished
for x in range(5):
    print(x, end = ' ')
else:
	print("\nFinally finished!")
print()
