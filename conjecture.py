
num  = int(input("Enter a number"))
cycles = 0
while True:
    cycles +=1
    print(num)
    if (num %2==0):
        num = num/2
    elif num==1:
        break
    else:
        mum = num * 3 + 1
