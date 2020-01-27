students = ["melzy","pelz","aylz","vilz"]
scores = [{"math": 2, "eng": 5,"name": "melzy"},
          {"math": 1, "eng": 5, "name": "pelz"},
          {"math": 4, "eng": 2, "name": "aylz"},
          {"math": 5, "eng": 1, "name": "vilz"}]
for student in students:
    print(student)
    for score in scores:
        if student == score.get("name"):
            print(score.get("eng"))
            print(score.get("math"))
