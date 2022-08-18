#in basic terms the if statements are just conditional statements followed by some blocks of code that executes whenever conditional statement evaluates true
#example
is_true = True
if is_true:
	print(f'there is always greatness within everymman')
#if conditional statements evaluates false then the block of codes that follows fails to run
#if statements has basic forms,the if else statement where only one condition is defined and the if elif else(though else might be omitted sometimes) and here more than one condition can be defined

#exercise
house_price = 1000000
good_credit = False
if good_credit:
	down_payment = house_price * 0.1
else:
	down_payment = house_price * 0.2
print(f'The  down_payment is ${down_payment}')

#logical operators are used to combine two or more conditional statements. basically we the AND,NOT and OR logical operator
#examples
above_18 = True
self_employed = True
if above_18 and self_employed:
	print(f'Eligible for loan')
#runs if both conditions are true
if above_18 or self_employed:
	print(f'Eligible for loan')
#runs if at least one condition is true

#comparison operator: these are used alongside if statements to form conditional statement. we have the following comparison operator;>,>=,<,<=,==,!=.

#exercise
name = input("What is you name? ")
length = len(name)
if length <= 3:
	print(f'Your name is too short')
elif length >= 50:
	print(f'Your name is too long')
else:
	print('This is perfect.You have a very nice name')