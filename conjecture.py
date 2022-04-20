
num  = int(input("Enter a number\n"))
cycles = 0
while True:
    cycles = cycles + 1
    print(num)
    if num==1:
        break
    elif num%2==0:
        num = num / 2
    else:
        num = num * 3 +1

print("\n" + str(cycles))
