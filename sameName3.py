def spam(divideBy):
    try:
        return 42 / divideBy
    exceptZeroDivsionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

