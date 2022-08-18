#whenever nubers are stored in variables they are treated as strings and thus they require conversion to work with. we have types of such values stored in variables - strings(str),integers(int),float and so on
#as a coorection to previous misconception one should note that when numbers is stored in variables they are treated as numbers but when called by the input function the are stored as strings.
import datetime
#exercise
weight = input('What is your weight(pounds)? ')
weight = float(weight) * 0.45
print('Your weight is ' + str(weight) + 'kilograms')
today = datetime.datetime.now()
print(today)