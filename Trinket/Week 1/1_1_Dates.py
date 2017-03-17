fdays=28
DIM = [0,31,fdays,31,30,31,30,31,31,30,31,30,31]
class Date:
    """ a user-defined data structure that
        stores and manipulates dates
    """

    # the constructor is always named __init__ !
    def __init__(self, month, day, year):
        """ the constructor for objects of type Date """
        self.month = month
        self.day = day
        self.year = year

    # the "printing" function is always named __repr__ !
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.
        """
        s =  "%02d/%02d/%04d" % (self.month, self.day, self.year)
        return s


    # here is an example of a "method" of the Date class:
    def isLeapYear(self):
        """ Returns True if the calling object is
            in a leap year; False otherwise. """
        if self.year % 400 == 0: return True
        elif self.year % 100 == 0: return False
        elif self.year % 4 == 0: return True
        return False

    def tomorrow(self):
        if self.isLeapYear == True:
            fdays=29
        if (self.day +1) > (DIM[self.month])==0:
            self.day=1; self.month+=1;
            if self.month > 12 ==0:
                self.month=1;self.year+=1;
        else:
            self.day+=1
        s = "%02d/%02d/%04d" % (self.month, self.day, self.year)
    def yesterday(self):
        if self.isLeapYear == True:
            fdays=29
        if self.day-1<1:
            self.month-=1; self.day=DIM[self.month];
            if self.month==0:
                self.month=12; self.day=31; self.year-=1;
        else:
            self.day-=1;
        s = "%02d/%02d/%04d" % (self.month, self.day, self.year)
    def addNdays(self,n):
        while n>0 :
            self.tomorrow()
            print(self)
            n-=1;
    def subNdays(self,n):
        while n>0:
            self.yesterday()
            print(self)
            n-=1
    def isbefore(self,d2):
        if self.year < d2.year:
            return True
        elif self.year > d2.year:
            return False
        elif self.year == d2.year:
            if self.month<d2.month:
                return True
            elif self.month > d2.month:
                return False
            elif self.month == d2.month:
                if self.day < d2.day:
                    return True
                elif self.day > d2.day:
                    return False
                elif self.day == d2.day:
                    return False
def copy(self):
    """ Returns a new object with the same month, day, year
        as the calling object (self).
    """
    dnew = Date(self.month, self.day, self.year)
    return dnew
