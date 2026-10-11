
# normal method and class declear
class Demo:
    name = 'A2Z'
    email = 'a2zithub@gmail.com'
    def __init__(self):
        self.newname = self.name
        self.newemail = self.email

d1 = Demo()
print(d1.name)
print(d1.newname)


# pass & fail
class Result:
    def __init__(self,mark):
        self.mark = mark
    def res(self):
        if self.mark>=35:
            print('Pass')
        else:
            print('Falil')

s1 = Result(50)
s1.res()

s2 = Result(20)
s2.res()
s2.res()

# return method
class Demo1:
    def add(self,a,b):
        c = a+b
        return c
d2 = Demo1()
print(d2.add(30,20))

# method in method 
class Demo:
    def total(self,a,b):
        return a+b;
    def result(self):
        total= self.total(10,20)
        print(total)

dem = Demo();
dem.result()


class Student:
    def __init__(self,name,mark):
        self.mark = mark
        self.name = name

    def result(self):
        if self.mark>=40 :
            print(f'{self.name} Pass')
        else:
            print(f'{self.name} fail')

res = Student('Pradip',30);
res.result()