# # # Class Decleare 
# # class Student:
# #     name = 'a2z'
# #     age = 25 


# # # print(age)
# # # object = ins

# # s1 = Student()
# # print(s1.name)
# # print(s1.age)

# # s2 = Student()
# # print(s2.name)
# # print(s2.age)

# # class Mobile:
# #     brand = 'Vivo'
# #     Price = 20000

# #     def dis(self):
# #         print('Welcome Student')
# #     def vprint(self):
# #         print(self.brand)
# #         print(self.Price)

# # s1 = Mobile()
# # print(s1.brand)
# # s1.dis()
# # s1.vprint()

# # example 

# class Atm:
#     atmname = ''
#     bank = 'SBI'
#     balance = 5000

#     def mybankname(self):
#         print(f"MY Bank name={self.bank}");
#     def mybankbalance(self):
#         print(f'My Bank Balance={self.balance}');
#     def myalldetails(self):
#         print(f'My Bank Name {self.bank} and bank balance={self.balance}')

# a1 = Atm();
# # a1.mybankname()
# # a1.mybankbalance()

# a1.myalldetails();

class student:
    marks = 500
    def totalmarks(self):
        print(f'my total marks ={self.marks}/600');
    def totalper(self):
        percal = self.marks/6
        print(f'Total per = {percal}')

s1 = student()
s1.marks = 450 
s1.totalmarks();
s1.totalper();



s1 = student()
s1.marks = 400 
s1.totalmarks();
s1.totalper();
