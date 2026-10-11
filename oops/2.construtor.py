
                                            # CONSTRUCTOR (MAGIC METHOD)

class student:
    name = 'a2z'
    def __init__(self):
        print('Welcome')

s1 = student()
print(s1.name)


class student1:
    name = 'a2z'
    def __init__(self):
       print(f'welcome {self.name}')

s2 = student1()

class Demo:
    def __init__(self,name,age):
        print(f'MY name is {name} my age is {age}')

s3 = Demo('Pradip',21)
s3 = Demo('Rahul',21)
s3 = Demo('Rohit',21)

class  Demo:
    def __init__(self,name):
        self.name = name

s4 = Demo('A2Z IT HUB')
print(s4.name)


class Result:
    def __init__(self,sub1,sub2,sub3):
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
    def tota(self):
        total = self.sub1 + self.sub2 + self.sub3
        return total;
    def per(self):
        total = self.sub1 + self.sub2 + self.sub3
        percentage = total/3
        return percentage;

Result_class = Result(14,25,43)
print(Result_class.tota())
print(Result_class.per())

Result_class = Result(14,80,43)
print(Result_class.tota())
print(Result_class.per())




        

        