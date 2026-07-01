'''import random
random.seed(13)
print(random.random())
print(random.randint(12,20))
print(random.uniform(12,20))
l=['java','c++','c','python','html']
print(random.choice(l))
print(random.choices(l,k=4))
print(l)
random.shuffle(l)
print(l)

#password generator
n=input("enter your name:")
sp=['@','#','>','$','!','%','&','*']
f=random.choices(n,k=4)+random.choices(sp,k=2)
print(''.join(f).title()+str(random.randint(1111,9999)))
'''
'''from datetime import date,time,datetime,timedelta
d=date.today()
print(d)
print(d.day)
print(d.month)
print(d.year)
print(d.weekday())
print(d.isoweekday())
d=date(2026,6,12)
print(d)
t=time(23,45,40)
print(t)
print(t.hour)
print(t.minute)
print(t.second)
print(d.strftime('%d/%m/%y'))
print(d.strftime('%d/%m/%y %H:%M:%S'))
print(d.strftime('%d/%m/%y  %I:%H:%M:%S'))
print(d.strftime('%d/%m/%Y  %I:%H:%M:%S %p'))
print(d.strftime('%d/%b/%Y  %I:%H:%M:%S %p'))
print(d.strftime('%d/%B/%Y  %I:%H:%M:%S %p'))
print(d.strftime('%a,%d/%B/%Y  %I:%H:%M:%S %p'))
print(d.strftime('%A,%d/%m/%Y  %I:%H:%M:%S %p'))

d=datetime.now()
d7=d+timedelta(days=60)
print(d7)
h2=d+timedelta(hours=2)
print(h2)
m15=d-timedelta(minutes=15)
print(m15)
s15=d+timedelta(seconds=15)
print(s15)

from itertools import combinations,permutations
res1=list(combinations('abc',2))
res2=list(permutations('abc',2))
print([''.join(i) for i in res1])
print([''.join(i) for i in res2])
'''
from collections import Counter,defaultdict,deque
s='python programming'
l=[1,2,3,12,3,4,5,3,6,7,3,5,8,0]
d=defaultdict(int)
for i in s:
    d[i]+=1
print(d)
print(Counter(s))
print(Counter(l))
d=deque([])
d.append(10)
d.append(20)
d.append(30)
d.append(40)
d.popleft()
d.popleft()
d.append(50)
d.append(60)
d.append(70)
d.popleft()
print(d)
