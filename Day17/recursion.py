'''def sumofn(n):
    if n==0:
        return 0
    return n+sumofn(n-1)
n=int(input('Enter the n: '))
print(sumofn(n))


def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
n=int(input('Enter the n: '))
print(factorial(n))

n=int(input())
sum=0
for i in range(n):
    i=n%10
    sum+=i
    n=n//10
print(sum)

def sumofdigits(n):
    if n==0:
        return 0
    return n%10+sumofdigits(n//10)
n=int(input('Enter the n: '))
print(sumofdigits(n))

def power(base,pow):
    if pow==0:
        return 1
    return base*power(base,pow-1)
n=int(input('Enter the n: '))
print(power(2,5))

def display(s,ind):
    if len(s)+1==ind:
        return
    print(s[:ind])
    display(s,ind + 1)
display('Python Programming',1)


def display(s,ind,wid):
    if ind==len(s)-wid+1:
        return
    print(s[ind:ind+wid])
    display(s,ind + 1,wid)
display('Python Programming',0,4)


res=[i for i in range(1,11)]
print(res)

l=[1,2,3,4,5]
res1=[i*i for i in l]
print(res1)

s='python programming'
res=[i for i in s if i in 'aeiouAEIOU']
print(res)

s=[1,2,23,24,27,45,42,32,85,96,42,54]
res=[i if i%2==0 else 0 for i in s]
print(res)

res=[j for i in range(4) for j in range(1,4)]
print(res)

res=[[j for j in range(1,4)] for i in range(5)]
print(res)
'''
res={i for i in range(1,11)}
print(res)

res={i:i**2 for i in range(1,11)}
print(res)


































