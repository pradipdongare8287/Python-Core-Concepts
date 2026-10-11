
# print('Hellow',end=' ')
# print('A2Z',end=' ')
# print('A2Z',end=' ')
# print('A2Z',end=' ')
# print('A2Z',end=' ')
# print('A2Z',end=' ')

# print('\nA2Z \n IT \n HUB')
# print('A2Z\tIT\tHUB')

# print('*')
# print('**'*3)

# print(' '*4+'*')
# print(' '*3+'***')
# print(' '*2+'*****')
# print(' '*1+'*******')



# print('2026','09','24',sep="-")


# for i in range(1,11):
#     for ii in range(1,6):
#         print(ii,end=' ')
#     print(' ')


# for i in range(1,6) :
#     for v in range(1,6) :
#         print('*',end=" ")
#     print()


# for b in range (1,7):
#     for bb in range(b):
#         print('*',end='')
#     print()

# for c in range(1,7):
#     for cc in range(5-c):
#         print("*",end=' ')
#     print()

# row=4;
# i=0,1
# space=> row-i-1 4-0-1=3,4-1-1=2
# star=>2*i+1 2*0+1=1,2*1+1=3

row=10;
for i in range(row):
    for space in range(row-i-1):
        print(" ",end="")
    for star in range(2*i+1):
        print("*",end="")
    print()


row1 = 5
for i in range(row1):
    for space in range(row1-i-1):
        print(' ',end='')
    for star in range(2*i+1):
        print('*',end="")
    print()
    