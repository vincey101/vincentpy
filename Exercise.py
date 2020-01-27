n = int(input("Enter your lower range here: "))
x = int(input("Enter your upper range here: "))
divisor = int(input("what is the divisor: "))
tries = 0
for num in range(n, x+1):
    if num % divisor == 0:
        tries += 1
        print("the numbers in range that are divisible by", divisor,"is:", num)
print("this operation can be performed",tries, "times")