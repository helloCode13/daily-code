# Grade calculator program
def main():
    tests = [100, 90, 89, 60, 59, 0, -1, 101]
    for score in tests:   # 8 test inputs
        print("Grade:",score_to_grade(score))

def score_to_grade(score: int) -> str:
    if score < 0 or score > 100:
        return "Invalid score"
    
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

main()