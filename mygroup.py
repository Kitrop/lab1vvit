from statistics import mean

groupmates = [
    {
        "name": "Евгений",
        "surname": "Годин",
        "exams": ["Философия", "История", "Web"],
        "marks": [2, 5, 4]
    },
    {
        "name": "Артем",
        "surname": "Сорокин",
        "exams": ["Философия", "АиГ", "Ввит"],
        "marks": [2, 3, 5]
    },
    {
        "name": "Алексей",
        "surname": "Момотенко",
        "exams": ["Философия", "КГ", "Выш.Мат"],
        "marks": [2, 5, 5]
    }
]


def students(stud):
    print("Введите среднюю оценку")
    needScore = float(input())
    needStudents = []
    for i in range(len(stud)):
        studScore = stud[i]['marks']
        # 1-й способ
        # middleScoreStud = mean(studScore)
        # 2-й способ
        summary = sum(studScore)
        middleScoreStud = summary / len(stud[i]['marks'])
        if middleScoreStud > needScore:
            needStudents.append(stud[i])
    print(needStudents)


students(groupmates)
