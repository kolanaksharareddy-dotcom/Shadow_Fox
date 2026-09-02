numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

print("First element:", numbers[0])

numbers.append(60)
print("After append:", numbers)

numbers.insert(2, 25)
print("After insert:", numbers)

numbers.extend([70, 80])
print("After extend:", numbers)

numbers.remove(30)
print("After remove:", numbers)

numbers.pop()
print("After pop:", numbers)

print("Length:", len(numbers))

print("Count of 20:", numbers.count(20))

print("Index of 40:", numbers.index(40))

numbers.sort()
print("Sorted List:", numbers)

numbers.reverse()
print("Reversed List:", numbers)

print("Maximum:", max(numbers))

print("Minimum:", min(numbers))

print("Sum:", sum(numbers))

if 40 in numbers:
    print("40 is present")
else:
    print("40 is not present")