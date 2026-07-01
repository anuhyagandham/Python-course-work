'''
def display():
    n=10
    def inner():
        nonlocal n
        n+=10
        print('Inner function: ',n)
    inner()
    print('Outer Function: ',n)
display()

def display():
    course='Java Full Stack'
    print('Starting: ',course)
    def change():
        course='Python Full Stack'
        print('Updated: ',course)
    change()
    print('Final: ',course)
display()

def display():
    course='Java Full Stack'
    print('Starting: ',course)
    def change():
        nonlocal course
        course='Python Full Stack'
        print('Updated: ',course)
    change()
    print('Final: ',course)
display()

s='python'
print(len(s))
len=10
print(len(s))

s='python'
print(len(s))
len=10
print(len)

def update(n):
    n=10
    print('Inside: ',n)
n=20
update(n)
print('Outside: ',n)


def update(n):
    n=4.5
    print('Inside: ',n)
n=2.3
update(n)
print('Outside: ',n)

def update(n):
    n=4+3j
    print('Inside: ',n)
n=2+3j
update(n)
print('Outside: ',n)

def update(n):
    n=n.upper()
    print('Inside: ',n)
n='python'
update(n)
print('Outside: ',n)

def update(n):
    n.append(40)
    print('Inside: ',n)
n=[10,20,30]
update(n)
print('Outside: ',n)


def update(n):
    n=n+(40,50)
    print('Inside: ',n)
n=(10,20,30)
update(n)
print('Outside: ',n)


def update(n):
    n.update({40,50})
    print('Inside: ',n)
n={10,20,30}
update(n)
print('Outside: ',n)

def update(n):
    n.update({4:40,5:50})
    print('Inside: ',n)
n={1:10,2:20,3:30}
update(n)
print('Outside: ',n)

def update(n):
    n=True
    print('Inside: ',n)
n=False
update(n)
print('Outside: ',n)

def display(n):
    if n>10:
        return
    print(n)
    display(n+1)
display(1)

def display(n):
    if n>10:
        return
    display(n+1)
    print(n)
display(1)

def display(s,ind):
    if ind==len(s):
        return
    display(s,ind+1)
    print(s[ind])
display('Python Programming',0)
'''
def display(s,ind):
    if ind==len(s):
        return
    print(s[ind])
    display(s,ind+1)
    print(s[ind])
display('Python Programming',0)
