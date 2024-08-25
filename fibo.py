def fibo(n):
    if(n<=1):
        return n
    else:
        return fibo(n-1)+fibo(n-2)
    
n=int(input('Enter a number '))
for x in range(0,n,1):
    print(fibo(x))
