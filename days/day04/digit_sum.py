def digit_sum(n):
    is_negative = n < 0
    
    n = abs(n)
    sum_of_digits = 0
    while n > 0:
        digit = n % 10
        if is_negative and n // 10 == 0:    # The left most digit takes the sign, so -123 is 4
            sum_of_digits-=digit
            break
        
        sum_of_digits+= digit

        n//=10
    return sum_of_digits

tests = [
    (123, 6),
    (7, 7),
    (10, 1),
    (999, 27),
    (1000, 1),
    (0, 0),
    (-123, 4),
    (-7, -7),
]

for test in tests:
    output = digit_sum(test[0])
    print(f'the input is {test[0]} and the expected is {test[1]}, the output is {output}, the test: {"Pass" if output == test[1] else "Fail" }')

