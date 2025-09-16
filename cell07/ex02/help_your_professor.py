def average(scores):
    total = sum(scores.values())
    count = len(scores)
    return total / count

class_math = {
    "alice": 16,
    "bob": 14,
    "carol": 18,
    "david": 12,
    "emma": 15,
    "frank": 10,
    "grace": 17
}
class_science = {
    "alice": 9,
    "bob": 11,
    "carol": 14,
    "david": 17,
    "emma": 13,
    "frank": 15,
    "grace": 12
}

print(f"Average for class math: {average(class_math)}", "คะแนน")
print(f"Average for class sciencce: {average(class_science)}", "คะแนน")