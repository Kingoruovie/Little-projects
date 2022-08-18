number = 9
i = 1
while i <= 3:
	guess = int(input('Guess: '))
	i += 1
	if guess == number:
		print(f'That was great you got the answer')
		break
	elif guess != number:
		print(f'That was wrong try again')
else:
	print('YOU FAILED')
