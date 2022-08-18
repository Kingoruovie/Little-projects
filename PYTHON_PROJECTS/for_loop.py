#we use for loops in python for iteration that is repetition of a particular task over and over until object being worked on is exhausted. we iterate over list,strings etc
#example
for  item in [1, 2, 3, 4]:
	print(item)
#the range function is always used alongside the foor loop. it basically creates a set of numbers that for loops should work with. eg range(5) is just from 0 to 4. similarly range(5, 10) is from 5 to 9. now there are scenerios that the range function can be used to create list of numbers that increases by certain intervals. eg range(5,15,2), here the increment is 2.
#exercise
prices =[10, 20, 30]
total = 0
for item in prices:
	total += item
print(f"total: {total}")
#note we had to take both the total and print statement out our for loop.
#nested loops are for loops having for loops in them
for x in range(4):
	for y in range(4):
		print(f"({x},{y})")
#exercise
numbers = [5, 2, 5, 2, 2]
for number in numbers:
	print("X" * number)
#trial
trials = [2, 2, 6, 2, 2]
for trial in trials:
	if trial == 2:
		print("X" * trial + " " * trial + "X" * trial)
	else:
		print("X" * trial)
#another method for exercise
numbers = [5, 2, 5, 2, 2]
for number in numbers:
	output = ""
	for item in range(number):
		output += "X"
	print(output)
#take note of the range function function and the inner loop of the alternative form of working on exercise