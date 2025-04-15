age = input('How old are you?')
print(f'you are {age} years old.')
age = int(age)
if age < 18:
    print('You are a teenager.')  
elif age <50:
    print('You are an adult.') 
else:
   print ('And you are old.')  