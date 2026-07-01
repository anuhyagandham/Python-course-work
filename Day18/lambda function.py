'''
wish=lambda name: f'welcome to the course, {name}'
print(wish('anuhya'))

greater=lambda a,b: a if a>b else b
print(greater(10,3))

avg=lambda a,b,c: (a+b+c)/3
print(avg(10,20,30))


gst=lambda p: p+p*0.18
print(gst(1000))
print(gst(5400))
print(gst(300000))
'''
l=[1,2,3,4,5]
r1=list(map(lambda i:i+10,l))
print(r1)

