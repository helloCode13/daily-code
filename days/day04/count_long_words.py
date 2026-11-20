def count_long_words(sentence, min_len):
    pointer = 0
    word_count = 0
    while pointer < len(sentence):
        char = sentence[pointer]
        while char == ' ':
            pointer+=1
            if pointer == len(sentence):
                break
            char = sentence[pointer]

        word_length = 0
        while char!=' ':
            word_length+=1
            pointer+=1
            if pointer == len(sentence):
                break
            char = sentence[pointer]

        if word_length >= min_len and word_length > 0:
            word_count+=1
    
    return word_count
        

words_tests = [
    (("the quick brown fox", 5), 2),
    (("the quick brown fox", 3), 4),
    (("the quick brown fox", 6), 0),
    (("  extra   spaces  here ", 5), 2),
    (("", 3), 0),
    (("hello", 5), 1),
    (("  hi  ", 0), 1,),    
]


for test in words_tests:
    output = count_long_words(test[0][0],test[0][1])
    print(f'the inputs are ("{test[0][0]}") and {test[0][1]} and the expected is {test[1]}, the output is {output}, the test {"Pass" if output == test[1] else "Fail"}')

