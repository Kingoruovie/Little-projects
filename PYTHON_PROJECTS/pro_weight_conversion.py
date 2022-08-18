weight = input('Weight: ')
unit_in = input('convert from(kg or lbs): ')
unit_to = input('convert to(kg or lbs): ')
print(f'your weight in unit given is {weight}{unit_in}')

weight = int(weight)
if unit_to == 'kg':
	weight *= 0.45
elif unit_to == 'lbs':
	weight *= 2.204
	weight = round(weight)
print(f'Your weight is {weight}{unit_to}')