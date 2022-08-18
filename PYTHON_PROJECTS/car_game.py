game = ''
started = False
while True:
	game = input('> ').lower()
	if game == 'start':
		if started:
			print('car is already started')
		else:
			started = True
			print('the car has started')
	elif game == 'stop':
		if not started:
			print('car is already stopped')
		else:
			started = False
			print('the car has been stopped successfully')
	elif game == 'help':
		print("""
start- to start the car
stop- to stop the car
quit- to end the game
			""")
	elif game == 'quit':
		print('Goodbye')
		break
	else:
		print('i dont understand that')