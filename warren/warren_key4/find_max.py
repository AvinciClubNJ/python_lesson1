numbers = [1, -20, 0, 100, -5, 4, 10, 23, -19, 99]
maxnumber = numbers[0]

iterNumbers = iter(numbers)
next(iterNumbers)

for x in iterNumbers:
    if x > maxnumber:
        maxnumber = x
print(maxnumber)