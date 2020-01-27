# n = int(input("enter number of elements: "))
# y = []
# for values in range(n):
#     element = int(input("enter element" + str(values+1) +": "))
#     y.append(element)
# print(y)
#
# count = 0
# num = int(input("enter number to be counted: "))
# for i in y:
#     if i == num:
#         count += 1
#     else:
#         print("Element is not on the list")
#         break
# print("the number of times",num," appears is: ",count)


# n = int(input("enter number of element: "))
# a =[]
# a = [num for num in range(1,n+1) if (int(num**0.5))**2 == num and sum(list(map(int,str(num)))) < 10]
# print(a)


# n = input('enter your word: ')
# def modify(n):
#     final = " "
#     for letter in range(len(n)):
#         if letter % 2 == 1:
#             final = final + n[letter]
#     return final
# print("modify string is:")
# print(modify(n))

# x = input("enter word1: ")
# y = input("enter word2: ")
# count1 = 0
# count2 = 0
# for i in x:
    # count1 += 1
# for j in y:
#     count2 += 1
# if count1 > count2:
#     print("the word with the longest character is :", x)
# elif count1 == count2:
#     print("the words are of the same amount of characters")
# else:
#     print("the word with the longest character is :", y)


# x = input("enter the word: ")
# count_upper = 0
# count_lower = 0
# for letters in x:
#     if letters.isupper():
#         count_upper += 1
#     elif letters.islower():
#         count_lower += 1
# print("the number of lowercase character is:", count_lower)
# print("the number of uppercase character is:", count_upper)


# old_str = input("enter a word of at least 5 character: ")
# new_str = []
# count = 0
# for letters in old_str:
#     count += 1
# join = old_str[0:2] + old_str[count-2:count]
# new_str.append(join)
# print("newly formed string is: ")
# print(new_str)


n = input("enter the string: ")
count = 0
for letters in n:
    count += 1
print(count)
print("the length of the string is:",count)

