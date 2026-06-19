'''
n=int(input('Enter Size: '))
for i in range(n):
    for j in range(n):
        print('*',end=' ')
    print()

n=int(input('Enter Size: '))
for row in range(n):
    for col in range(n):
        print(col%2,end=' ')
    print()

n=int(input('Enter Size: '))
for i in range(n):
    for j in range(n):
        print(i%2,end=' ')
    print()

n=int(input('Enter Size: '))
for i in range(n):
    for j in range(n):
        print((i+j)%2,end=' ')
    print()

n=int(input('Enter Size: '))
for i in range(n):
    for j in range(n):
        print(int(i+j>=n-1),end=' ')
    print()

n=int(input('Enter Size: '))
for i in range(n):
    for j in range(n):
        print(int(i+j<=n-1),end=' ')
    print()

n=int(input('Enter Size: '))
c=1
for i in range(n):
    for j in range(n):
        print(str(c).zfill(2),end=' ')
        c+=1
    print()

n=int(input('Enter Size: '))
for i in range(n):
    for j in range(i+1):
        print('*',end=' ')
    print()

n=int(input('Enter Size: '))
for i in range(n):
    for j in range(n-i):
        print('*',end=' ')
    print()

c=65
n=int(input('Enter Size: '))
for i in range(n):
    for j in range(i+1):
        print(chr(c),end=' ')
        c+=1
    print()

c=65
n=int(input('Enter Size: '))
for i in range(n):
    for j in range(n-i):
        print(chr(c),end=' ')
        c+=1
    print()

'''
n=int(input('Enter Size: '))
for i in range(n):
    for j in range(n-i-1):
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()
'''
n=int(input('Enter Size: '))
for i in range(n):
    for j in range(n-i-1):
        print('',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()

n=int(input('Enter Size: '))
for i in range(n):
    for k in range(i):
        print(' ',end=' ')
    for j in range(n-i):
        print('*',end=' ')
    print()

n=int(input('Enter Size: '))
m=n//2
for i in range(n):
    if i<=m:
        
        for j in range(i+1):
            print('*',end=' ')
    else:
        
        for j in range(n-i):
            print('*',end=' ')
    print()
'''















