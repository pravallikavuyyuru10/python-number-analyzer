numbers = [5,8,-2,-7,10]
positive = 0
negative = 0
even = 0
for  i in numbers:
    if i > 0:
        positive = positive + 1
    elif i < 0:
        negative = negative + 1
    if i % 2 == 0:
        even = even + 1


print("Positive:", positive)
print("Negative:", negative)
print("Even:", even)

        

