# n = input("enter your string: ")
# if len(n) < 5:
#     print("the string is less than 5")
#
# elif len(n) < 10:
#     print("the string is less than 10")
#
# elif len(n) > 20:
#     print("the string is greater than 20")
# else:
#     print("the string is above 20")



# story = 'i have a shop to-let , but the shop has a bad toilet facility , i also think the shop need renovation,the good thing here is the shop is situated in a lovely environment'
# print(story.count('shop'))
# new_story = story.replace('shop','warehouse')
# print('new_story:\n',new_story)
#  count = 0
#  for letter in story_list:
#      if letter == "shop":
#          count += 1
#
# shop_comp = [each_item for each_item in story_list if each_item == "shop"]
# shop_comp = [story_list.count(each_item) for each_item in story_list if each_item == "shop"]
#
# print(count)
# print(shop_comp)


# num = 'this is a common interview question'
# all_freq = {}
# for letters in num:
#     if letters in all_freq:
#         all_freq[letters] += 1
#     else:
#         all_freq[letters] = 1
# print('count of all characters in This is a common interview question is:\n' + str(all_freq))

# num = 'this is a common interview question'
# res = {}
# for letters in num:
#     res[letters] =res.get(letters,0) + 1
# print(res)
# print('count of all the characters in This is a common interview question:\n' + str(res))


# list_a = [1,2,3,4,5,6,7]
# set_a = [1,2,3,4,5,6]
# set_b = [7,8,9,10]
# new_list = [i for i in list_a]
# new_dict = {f"number_{i}":i for i in list_a}
# print(new_list)
# print(new_dict)

# packing and unpacking
# def fun(a,b,c,d):
#     print(a,b,c,d)
# my_list = [1,2,3,4]
# print(fun(*my_list))

# number = int(input("enter your factorial: "))
# fact = 1
# while number > 0:
#     fact = fact * number
#     number = number - 1
#
# print("factorial of the number is: ")
# print(fact)

# n = int(input("enter the number of list1: "))
# n_list = []
# print('for list1:')
# for element in range(n):
#     total = int(input("element"+ str(element+1) + ':'))
#     n_list.append(total)
# print(n_list)
#
# print('for list2:')
# p = int(input("enter the number of list2: "))
# p_list = []
# for element in range(p):
#     total_2 = int(input("enter element" + str(element+1) + ":"))
#     p_list.append(total_2)
# print(p_list)
# print("The intersection is: ")
# print(set(n_list) & set(p_list))


# file_name = input("enter file name: ")
# word = input("enter word to be searched: ")
# k = 0
# with open(file_name,'r') as f:
#     for line in f:
#         words = line.split()
#         for i in words:
#             if i == word:
#                 k += 1
# print("occurrences of the word:")
# print(k)


f = open("demofile2.txt",'a')
f.write("now the file has more content!")
f.close()
f = open("demofile2.txt", 'r')
print(f.read())
