print('''
 Here is what I can do for you:
      + for addition
      - for subtraction
      x for multiplication
      / for division
      ''')
choice = input('What do you want to do? ')
first_number = input('What is your first number? ')
second_number = input('What is your second number? ')
first_number = int (first_number)
second_number = int(second_number)
if choice == '+':
    print(first_number + second_number) 
elif choice == '-':
    print(first_number - second_number)
elif choice == 'x':
    print(first_number * second_number) 
elif choice == '/':
    print(first_number / second_number)