'''Simple If
------------

sales=int(input('Enter sales: '))
if sales>1000:
    print('Best seller')

eligible=input("Eligible Account: ")
verified=input('Verified Account: ')
if eligible=='True' and verified=='True':
    print('Verification Badge Granted')

status=input('Is it raining outside: ')
if status=='True':
    print('Extra Rain Charges Applied')

If Else
--------------

credentials=('admin','admin@123')
uname=input('Enter uname: ')
pd=input('Enter pd: ')
if (uname,pd)==credentials:
    print('Login Successful')
else:
    print('Invalid credentials')

t=('Laptop','Mobile','Watch')
print('Available Products: Laptop,Mobile,Watch')
selected =input('Enter Selected Product: ')
if selected in t:
    print('Product Available') 
else:
    print('Product Not Available')

bill=int(input('Enter Total Bill: '))
if bill>99:
         print('The Final Bill',bill)
else:
    print('The Final Bill includes delivery charges',bill+30)


budget=int(input('Enter the budget: '))
if budget>10000:
    print('Plan : Trip')
elif budget>5000:
    print('Plan : Resort Stay')
elif budget>3000:
    print('Plan : Movie and Dinner')
elif budget>1000:
    print('Plan : Cafe and Shopping')
elif budget>500:
    print('Plan : Street food and Park Visit')
else:
    print('Stay Home')

'''

t=int(input('Enter the current hour: '))
if 5 <= t<=11:
    print('Good Mrng,Have a nice day')
if 12<= t<= 16:
    print('Good Afternoon'

