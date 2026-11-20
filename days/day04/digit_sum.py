def digit_sum(n):
    if n < 0:
        return
    
    n = abs(n)
    sum = 0
    while (n > 0):
        sum+= n % 10
        n//=10
    return  sum

tests = [
    (123, 6),
    (7, 7),
    (10, 1),
    (999, 27),
    (1000, 1),
    (0, 0),
]

for test in tests:
    print(f'the input is {test[0]} and the expected is {test[1]}, the output is {digit_sum(test[0])}')

