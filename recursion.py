def recurfact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*recurfact(n-1)
num=int(input())
if num<0:
    print("factorial does not exist for negative number")
else:
    print("factorial:",recurfact(num))