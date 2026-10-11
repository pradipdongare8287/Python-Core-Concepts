

# if control statment 

age = 18 ;

if age>=10 :
    print('you are eligibal for driving')

OTP = 1234;

if OTP==1234 :
    print('Access Granted');

shoping_amt = 1000;

if shoping_amt>=1000 :
    print('You are claim discount')


bankbalance =10000;

if bankbalance>=1000 :
    print('withdralv3000 amount sucessfull')


username = 'pradip';
password =1234;

if username=='pradip' and password ==1234 :
    print('Login Scussesful')


age = 17;

if age<=18 :
    print('Sorry you can not eleigibal this page beacuse you are minor');




# ======================================================

# if else  control statement 

sub1 = 80;
sub2 = 70;
sub3 = 60;
sub4 = 90;

if sub1>=35 and sub2>=35 and sub3>=60 and sub4>=35 :
    print('Congratulations your pass');
else:
    print('Sorry your fail ')


for i in range(1,100):
    if i % 2 ==0 :
        print(i)


#  if elif control statement 

x =100
y =200
z =300

if x>y and x>z:
    print('x is greeter than y');
elif y>x and y>z:
    print('y is greater than x');
else:
    print('Z is big ')


# Match case

    color = 'pink';

match color:
    case 'red':
        print('stop');
    case 'green':
        print('Please Start Your Vechical');
    case 'yellow' :
        print('Happy Journey you can go now');
    case _:
        print('other color')


