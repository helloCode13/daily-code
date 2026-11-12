def number_to_string(num: int) -> str:
    if num == 0:
        return '0'

    is_negative = num < 0
    num = abs(num)
    digits = []

    while num > 0:
        digit = num % 10
        char = chr(ord('0') + digit)
        digits.append(char)
        num //=10

    if is_negative:
        digits.append('-')

    digits.reverse()
    return "".join(digits)

def main():
    print('-7232 ->', number_to_string(-7232))
    print('4422 ->', number_to_string(4422))

main()