numbers = [10, 3, 4, 7, 2, 9, 6, 11, 14, 1, 5]
oddNumbers = []

#Find even numbers and put them in a new list?
for i in numbers:
    if i % 2 != 0:
        print(i, "is an odd number!")
        oddNumbers.append(i)
    else:
        print(i, "is an even number")

print(oddNumbers)
