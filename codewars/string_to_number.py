def string_to_number(s):
    is_negative = s[0] == '-'
    start = 1 if is_negative else 0
    number = 0

    for char in s[start:]:
        number = number * 10 + ord(char) - ord('0')

    return -number if is_negative else number

def main():
    print('1234 ->', string_to_number("1234"))
    print('605 ->',string_to_number("605"))
    print('1405 ->',string_to_number("1405"))
    print('-7 ->',string_to_number("-7"))

main()
