import datetime

class Date:
    def __init__(self, dd, mm, yy):
        self.dd = dd
        self.mm = mm
        self.yy = yy
        self.__checkDate()
    
    def __checkDate(self):
        isValid = True
        try:
            datetime.datetime(self.yy, self.mm, self.dd)
        except ValueError:
            isValid = False
        
        if isValid:
            print("Inputted Date is valid")
        else:
            raise ValueError("Invalid Date")
    

date = input("Enter Date, Month and Year in the following format[dd.mm.yyyy]: " )
try:
    dd = int(date.split('.')[0])
    mm = int(date.split('.')[1])
    yr = int(date.split('.')[2])
    d = Date(dd, mm, yr)
except ValueError:
    print("Date entered is incorrect format", date)