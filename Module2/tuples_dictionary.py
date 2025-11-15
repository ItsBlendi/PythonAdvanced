grades = {
    ("John", "Math"): 5,
    ("Alice", "Biology"): 4,
    ("Eve", "Music"): 3,
    ("John", "Engish"): 4


}

john_math = grades[("John", "Math")]
print("Joh's grade in math is:" , john_math)

grades [("Florjon" , "Edukat fizike")] = 5
print(grades)

keys = list(grades.keys())
print(keys)

student, subject = keys[0]
print(student,"'s grade in",subject,"is", john_math)