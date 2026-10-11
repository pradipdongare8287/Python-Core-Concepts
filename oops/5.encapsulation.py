

#                                         # ENCAPSULATION

# # _____________________________________Public______________________________________________________
class Demo:
    def __init__(self):
        self.name = 'Pradip'

# Public
s1 = Demo()
print(s1.name)

s1.name = 'Rohit'
print(s1.name)



# # _____________________________________Protected____________________________________________________

# protected
class protected:
    def __init__(self):
        self.name = 'Pradip Dongare'
        self._salary = 30000

s2 = protected()
print(s2.name)
print(s2._salary)


# # _____________________________________Private______________________________________________________

class Private:
    def __init__(self):
        self.name = 'Pradip Shankar Dongare' #Public access
        self._salary = 50000   # Protected 
        self.__commission = 1000 # Private
    def comemii(self):
        print('commission =', self.__commission)

s3 = Private()
print(s3.name)
print(s3._salary)
# print(s3.__commission)
s3.comemii()


# -------------------------------------------------------------Method encapsulation ---------------------------
# method public protected private

class Demo:
    # public
    def bankname(self):
        print("My Bank Name is BOB");
    #protected
    def _atmno(self):
        print('My ATM No=12332t4t324');
    #private
    def __atmpin(self):
        return 1212;
    def showpin(self):
        print("My Pin No=",self.__atmpin());
s1=Demo();
s1.bankname();
s1._atmno();
# s1.__atmpin();
s1.showpin();


class Bank:
    def bname(self):
        print('My Bank Name is Central Bank of india')
    def _atmno(self):
        print('My Atm no is 2232323349348')
    def __atmpin(self):
        return 3434453;
    def viewpin(self):
        print("My atm pin is ",self.__atmpin())

b5 = Bank()
b5.bname()
b5._atmno()
# b5.__atmpin()
b5.viewpin()