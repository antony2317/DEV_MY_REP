with open("students.txt", "r", encoding="utf-8") as file:
    for line in file:
        surname, name, grade = line.split()
        grade = int(grade)
        if grade < 3:
            print(f"{surname} {name}")
