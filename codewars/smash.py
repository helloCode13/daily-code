def smash (words):
    if len(words) == 0:
        return ""

    result = ""
    for i, word in enumerate(words):
        if(i!=0):
            result+= " "
        result+= word

    return result

def main():
    print(smash([]))
    print(smash(["hello"]))
    print(smash(["hello", "world"]))
    print(smash(["hello", "amazing", "world"]))
    print(smash(["this", "is", "a", "really", "long", "sentence"]))

main()