'''
class Instagram:
    def login(self,username,password):
        self.username=username
        print(f'{self.username},Welcome to the Instagram')
anuhya=Instagram()
anuhya.login('Anuhya',1234)
'''
class Redbus:
    seats={}
    for i in range(1,11):
        if i%3==0:
            seats[i]='Booked'
        else:
            seats[i]='Available'
    def displayseats(cls):
        for i in cls.seats:
            print(f'[|{i}|{cls.seats[i]}|')
    def booking(self,seatno):
        if Redbus.seats[seatno]=='Booking':
            print('Already Booked')
        else:
            Redbus.seats[seatno]=='Booked'
            print('Successfully Booked')
anuhya=Redbus()
anuhya.displayseats()
anuhya.booking(1)
anuhya.booking(7)
anuhya.booking(9)
anuhya.displayseats()
