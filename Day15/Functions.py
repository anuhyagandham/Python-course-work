'''
def iseven(num):
    if num%2==0:
        return 'Even Number'
    else:
        return 'Odd Number'
print(iseven(11))
print(iseven(12))
print(iseven(14))
print(iseven(15))


def isprime(num):
    for i in range(2,num):
        if num%2==0:
            return f'{num}-Not a Prime Number'
        else:
            return f'{num}- Prime Number'
print(isprime(14))
print(isprime(7))

def isprime(n):
    for num in range(2,n+1):
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num,end=' ')
            
isprime(100)


def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    print(f'Factorial of {n}: {f}')
fact(4)
fact(5)
fact(6)
        
'''
#Positional Arg
def display(name,email):
    print('name:',name)
    print('email:',email)
display('anuhya','anuhya@gmail.com')
display('anuhya@gmail.com','anuhya')

#keyword Arg
def display(name,email):
    print('name:',name)
    print('email:',email)
display(name='anuhya',email='anuhya@gmail.com')
display(name='anuhya@gmail.com',email='anuhya')

#default Arg
def display(name,email='',pd=''):
    print('name:',name)
    print('email:',email)
display(name='anuhya')
display(name='anuhya@gmail.com',email='anuhya')
display(name='anuhya@gmail.com',email='anuhya')

#Variable length Arg
def display(*num):
    print('num:',num)
   
display(1)
display(1,2,3)
display(1,2,3,4)
display(1,2,,3,4,5)

def display(**num):
    print('num:',num)
   
display(k1=1)
display(k1=1,k2=2,k3=3)
display(k1=1,k2=2,k3=3,k4=4)
display(k1=1,k2=2,k3=3,k4=4,k5=5)

