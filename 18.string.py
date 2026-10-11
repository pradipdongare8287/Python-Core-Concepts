strg = 'Welcome to Python'
print(strg[0])
print(strg[-1])

print(strg[0:3])
print(strg[3:])

for i in strg:
    print(i)

print('Hello'.upper())
print('HELLO'.lower())

# buid in function 
text = "Python"
print(text.startswith('P'))
print(text.endswith('P'))
print(text.endswith('n'))
print(text.replace('Python','Ram'))

print(f"Welcome to {text}")

print('p' in text)
print('P' in text)

