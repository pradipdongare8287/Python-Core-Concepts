
# declear
def demo():
    print('Welcome')
# call
demo()
demo()
demo()
demo()

# normal def(function)
def wel():
    print('Welcome Ram')
wel()
wel()

# parametarise der(function)

def add(a,b):
    c = a+b
    print(c)
add(10,20) 
add(40,490)

# return keyword 

def ret(a,b):
    c= a+b
    return c;
c=ret(10,20)
print('Hello',c)

# default parameter
def login(username='root',password='root'):
    if username=='root'and password=='root':
        print('welcome')
login()

# flexible nofix value
def no(*number):
    print(sum(number))

no(12,30,49)

# nested 
def cal():
    def add():
        a=10+10
        print(a)
    def multi():
        b=20*20
        print(b)
    add()
    multi()
cal()