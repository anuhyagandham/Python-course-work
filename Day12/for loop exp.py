'''
price=list(map(int,input('Enter bill: ').split()))
bill=0
for i in price:
    bill+=i
print('Bill: ',bill)

pd=input('Enter password: ')
uc=lc=dc=sc=0
for i in pd:
    if i.isalpha():
        if i.isupper():
            uc+=1
        else:
            lc+=1
    elif i.isdigit():
        dc+=1
    else:
        sc+=1
print('Uppercase Count: ',uc)
print('Lowercase Count: ',lc)
print('Digits Count: ',dc)
print('Special Characters Count: ',sc)


movies=input('Enter Movies: ').split()
for i in range(len(movies)):
    print(i+1,'.',movies[i])
    

records=eval(input('Enter records: '))
print('Highest Salary: ',max(records.values()))
print('Lowest Salary: ',min(records.values()))
print('Average Salary: ',sum(records.values())/len(records))


scores=list(map(int,input('Enter the scores: ').split()))
tr=bd=db=0
for i in scores:
    if i==4 or i==6:
        bd+=1
    elif i==0:
        db+=1
    tr+=1
print('Total Runs: ',tr)
print('Boundary Runs: ',bd)
print('Dot Balls: ',db)

emails=input('Enter the email: ').split()
for i in emails:
    print(i.split('@')[1])


attempts=0
pin=1234
while attempts<3:
    epin=int(input('Enter the pin: '))
    if epin==pin:
        print('Access Granted')
        break
    attempts+=1
else:
    print('Card blocked')

c=0
while True:
    items=input('Enter items or exit:')
    if items=='exit':
        print('total items:',c)
        break
    c+=1
    
at=3
c='python'
while at>0:
    ans=input('Enter the answer: ')
    if ans == c:
        print('You Win')
        print('Lives Remaining:',at)
        break
    at-=1
else:
    print('Game Over\n Lives Remaining: 0')

s=input('Enter: ')
i=0
j=len(s)-1
while i<=j:
    print(s[i],s[j])
    i+=1
    j-=1
    
'''
n=int(input('Enter amount: '))
notes=[2000,500,100,50,10]
for i in notes:
    req=n//i
    n=n%i
    if req!=0:
        print(req,i)


























