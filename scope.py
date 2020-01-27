# students = [{"name":"vincent","gender":"male","score":70},
#             {"name":"pelumi","gender":"female","score":73},
#             {"name":"ayo","gender":"female","score":75},
#             {"name":"mercy","gender":"female","score":71}]
#
# # print(type(students))
# # for list in students:
# a =[sex["gender"] for sex in students]
# b = {f"number_{sex}": sex["gender"] for sex in students}
# print(a)
# print(b)


# my_dict = {'fruits':['banana','apple','orange'],
#            'vegetables':['pepper','carrot'],
#            'cheese':['swiss','cheddar','brie']}
# item = 'cheddar'
# for i in my_dict.keys():
#     if item in my_dict[i]:
#         print(i)


# my_list = [{"values":"apple","blah":2},
#            {"values":"banana","blah":3},
#            {"values":"cars","blah":4}]
# for variety in my_list:
#     a = variety["values"]
#     print(a)


# my_dict = {'apple':{'american':12,'mexican':24,'chinese':5},
#            'orange':{'arabian':14,'indian':29}}
# for (key,value) in my_dict:
#     if key == 'apple':
#         if 'american' in value:
#             print(value['american'])


# a = []
# n = int(input("enter the number of element in the list: "))
# for x in range(n):
#     elem = int(input("enter the element" + str(x+1) + ": "))
#     a.append(elem)
# b = [sum(a[0:x+1]) for x in range(0,len(a))]
# print("The original list is: ",a)
# print("The new list is: ",b)


# num = int(input("enter the number of elements: "))
# result = []
# for elem in range(num):
#     z = int(input("enter element"+ str(elem+1) + ": "))
#     result.append(z)
# swap = result[0]
# result[0] = result[num-1]
# result[num-1] = swap
# print("New list is:")
# print(result)


# def remove(string,n):
#     first = string[:n]
#     last = string[n+1:]
#     return first + last
# string = input('enter the string: ')
# n = int(input("enter the index: "))
# print("modified string: ")
# print(remove(string,n))


# n = int(input("enter the number of elements: "))
# result = []
# for word in range(0,n):
#     elem = input("enter element"+ str(word+1) + ": ")
#     # y = len(str(n+1))
#     result.append(elem)
# max1 = len(result[0])
# temp = result[0]
# for longest in result:
#     if len(longest) > max1:
#         max1 = len(longest)
#         temp = longest
# print("the word with the longest length is: ")
# print(temp)


# print('enter a hyphen separated sequence of words:')
# lst = [n for n in input().split('-')]
# lst.sort()
# print('sorted:')
# print('-'.join(lst))

# word = 'this is a common interview question'
# b = word.split()
# freq = []
# for elements in b:
#     freq.append(b.count(elements))
# print('string\n' + word + '\n')
# print('list\n' + str(b) + '\n')
# print('frequency\n' + str(freq) + '\n')
# print('pairs\n' + str(list(zip(b,freq))))
