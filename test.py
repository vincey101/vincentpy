# d1 = {"system tests":{"failed":5,"passed":0,"total":5},
#       "function tests":{"failed":5,"passed":0,"total":5}}
# d2 = {"system tests":{"failed":1,"passed":1,"total":2},
#       "function tests":{"failed":3,"passed":2,"total":5}}
# d3 = {"system tests":{"failed":0,"passed":0,"total":0},
#       "function tests":{"failed":1,"passed":0,"total":1}}
# d4 = {}
# for scores in d1,d2,d3:
#     for test,results in scores.items():
#         if test not in d4:
#             d4[test] = {}
#         for key,value in results.items():
#             if key in d4[test]:
#                 d4[test][key] += value
#             else:
#                 d4[test][key] =value
# print(d4)


# def myfuc(n):
#     return lambda a : a * n
# multiplier = myfuc(3)
# print(multiplier(11))


# name = 'my name is oladimeji vincent'
# each_element ={}
# for letters in name:
#     if letters in each_element:
#         each_element[letters] += 1
#     else:
#         each_element[letters] = 1
# print(each_element)

# a = input('enter dictionary key:')
# b = int(input('enter the dictionary value:'))
# my_dict = {}
# my_dict.update({a:b})
# print('my updated dictionary is:\n'+ str(my_dict))

#
# c = int(input("enter number of element in list: "))
# c_list = []
# d_list = []
# print("for keys:")
# for x in range(0,c):
#     element = int(input("enter number" + str(x+1) + ':'))
#     c_list.append(element)
#
# print('for values:')
# for x in range(c):
#     elem = int(input("enter number" + str(x+1) + ':'))
#     d_list.append(elem)
#
# e = dict(zip(c_list,d_list))
# print('the dictionary is:\n' + str(e))

# my_list = int(input('enter number of list: '))
# result = []
# for elements in range(my_list):
#     each_element = int(input('element' + str(elements+1) + ':'))
#     result.append(each_element)
# print(result)
# print(sum(result))

# recursive function
# def sum_arr(arr,size):
#     if size == 0:
#         return 0
#     else:
#         return arr[size-1] + sum_arr(arr,size-1)
# n = int(input('enter the number of elements for list: '))
# a = []
# for i in range(n):
#     elem = int(input("element:"))
#     a.append(elem)
# print("The list is:\n" + str(a))
# b= sum_arr(a,n)
# print("sum of the list is:\n" + str(b))


# def product(a, b):
#     if a < b:
#         return product(b,a)
#     elif b != 0:
#         return a+product(a,b-1)
#     else:
#         return 0
#
#
# a = int(input("enter first number:"))
# b = int(input("enter second number:"))
# print("product is:", product(a,b))


# n = [[1,2],[3,4]]
# def flatten(n):
#     if n == []:
#         return n
#     if isinstance(n[0],list):
#         return flatten(n[0]) + flatten(n[1:])
#     return n[:1] + flatten(n[1:])
# print("flattened list is:", flatten(n))


# test_int = 5
# test_str = "geeks for geeks"
# test_list = [1,2,3,4]
# print("is test_int integer?:", isinstance(test_int,int))
# print("is test_list dictionary?:",isinstance(test_list,dict))
# print("is test_int integer or list or tuple?:",isinstance(test_int,(str,list,tuple)))