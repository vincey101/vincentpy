n = int(input("Enter number of elements to be inserted: "))
a = []
for i in range(n):
    elem = int(input("Enter element: "))
    a.append(elem)
avg = sum(a)/n
print("The average of elements in the list is:", round(avg,2))