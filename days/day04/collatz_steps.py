def collatz_steps(n):
    counter = 0
    while n > 1:
        if n % 2 == 0:
            n//=2
        else:
            n = (3 * n) + 1
        counter+=1
    return counter


collatz_tests = [
    (1, 0),
    (2, 1),
    (3, 7),
    (6, 8),
    (7, 16),
    (27, 111),
]

for test in collatz_tests:
    output = collatz_steps(test[0])
    print(f'the input is {test[0]} and the expected is {test[1]}, the output is {output}, the test: {"Pass" if output == test[1] else "Fail"}')