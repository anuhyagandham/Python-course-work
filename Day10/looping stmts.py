'''
for var in seq:
        stmts
    seq:str,lst,tup,set,dict,range()

'\nfor var in seq:\n        stmts\n    seq:str,lst,tup,set,dict,range()\n'

s='python programming'
for ch in s:
    print(ch)


products=['laptop','mouse','keyboard','charger']
for product in products:
    print(product)

names=('anu','vasu','siri','bbabu')
for name in names:
    print(name)

s={'mysql','python','java','c'}
for i in s:
    print(i)

d={'bag':2000,'book':3000,'pen':300,'pencil':650}
for i in d:
    print(i,d[i])

for i in range(1,11):
    print(i)


for i in range(0,41,2):
    print(i)

for i in range(1,39,-2):
    print(i)

for i in range(10,0,-1):
    print(i)


s='python programming'
for i in range(len(s)):
    print(i)

s='python programming'
for i in range(len(s)):
    print(i,s[i])
    
products=['laptop','mouse','keyboard','charger']
for i in range(len(products)):
    print(i,products[i])

products=('laptop','mouse','keyboard','charger')
for i in range(len(products)):
    print(i,products[i])


s='python programming'
for i in enumerate(s):
    print(i[0],i[1])


products=['laptop','mouse','keyboard','charger']
for i in enumerate(products):
    print(i[0],i[1])

products=('laptop','mouse','keyboard','charger')
for i in enumerate(products):
    print(i[0],i[1])

s={'mysql','python','java','c'}
for i in enumerate(s):
    print(i[0],i[1])

d={'bag':2000,'book':3000,'pen':300,'pencil':650}
for i in enumerate(d):
    print(i[0],i[1])

d={'bag':2000,'book':3000,'pen':300,'pencil':650}
for i in enumerate(d):
    print(i[0],i[1],d[i[1]])


for i in range(20):
    if i==15:
        break
    print(i)

for i in range(20):
    if i==15:
        continue
    print(i)

for i in range(1,11):
    pass
if True:
    pass

'''

pin=1234
for i in range(5):
    epin=int(input('Enter pin: '))
    if pin==epin:
        print('Unlock the phone')
        break
    else:
        print('Incorrect Pin ,Try Again')
else:
    print('Try Again After 60sec')




