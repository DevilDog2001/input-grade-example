# Lists II & For loops & Tuples
# J. Sun

## for loops
print('\nFor Loops\n')

## Loop through the letters in strings
for x in "py":
    print(x)
print()

fruits = "apples"
for x in fruits:
    print(x)
print(f"{fruits} are nutritious and delicious!")
print()

## loop through items in the list
fruits = ["apple", "banana", 'python programming',]
# iterate through the list, printing each element once, one at a time
for item in fruits:
    print(item)                                    # indented code is part of the loop
print("Fruits are nutritious and delicious!")      # code that is not indented is not part of the loop
print()
