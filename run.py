# #assignment
# students_name = [{"name": "vincent", "gender": "male", "score": 70},
#                  {"name": "pelumi", "gender": "female", "score": 73},
#                  {"name": "ayo", "gender": "female", "score": 75},
#                  {"name": "mercy", "gender": "female", "score": 71}]


# def total_scores(students_score):
#     total_score = 0
#     for student in students_score:
#         total_score = total_score + student["score"]
#     return total_score


# print(total_scores(students))
#
#
# def gender_count():
#     male = 0
#     female = 0
#     for sex in students:
#         if sex["gender"] == "male":
#             male += 1
#     print('male:', male)
#     for sex in students:
#         if sex['gender'] == "female":
#             female += 1
#     print("female:", female)
#     return male, female
#
#
# gender_count()
#
#
# #
# #
# #
# def average_score(students_score):
#     n = len(students_score)
#     average = total_scores(students_score) / n
#     return average
#
#
# print("average score:", (average_score(students)))
#
#
#  def gender_count(students):
#      result = {}
#      for sex in students:
#          if "gender" in sex:
#              result[sex["gender"]] = result.get(sex["gender"], 0) + 1
#      return result
#  print(gender_count(students))
#
#
# def ascending_data(students_score):
#     result = []
#
#     score = [student['score'] for student in students_score]
#     sorted_score = sorted(score)
#
#     while len(result) < len(score):
#         for s_score in sorted_score:
#             for student in students_score:
#                 if student['score'] == s_score:
#                     result.append({"name": student['name'], "score": student['score']})
#
#     print(result)


# ascending_data(students)

# def ascending_data(students):
#     result = []
#
#     name = [student['name'] for student in students]
#     sorted_name = sorted(name)
#
#     while len(result) < len(name):
#         for s_name in sorted_name:
#             for student in students:
#                 if student['name'] == s_name:
#                     result.append({"name": student['name']})
#
#     print(result)
# ascending_data(students_name)


# def add_tags(tag,word):
#     return "<%s> %s </%s>" % (tag, word,tag)
# print(add_tags("a","i'm a boy"))


# name ="my name is peter"
# location = "my address is airport"
# print('<a> %s' %(name), '</a>')
# print("<b> %s" %(location), "</b>")

# x = 0
# y = 5
# for row in range(6):
#     for column in range(6):
#         if row == x and column == y:
#             print("*",end="")
#             x = x + 1
#             y = y - 1
#         elif row == column:
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()


a = [1,2,3,4,5,6,7,8,9,0]
b = [2,6,8,0,12,14]
common = set(a) & set(b)
c_mon = set(a) - (set(a)-set(b))
common_list = [num for num in a if num in b]
print(common)
print(c_mon)
print(common_list)