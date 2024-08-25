n=int(input("enter a number : "))
if(n<0):
    n=-n
while(n>9):
    s=0
    while(n/10!=0):
        s=s+(n%10)
        n=n//10
    n=s
if(s==1):
    print("magic no")
else:
    print("not a magic no")