#string methods are functions which acts on strings
#examples

course = "Python for beginners"
print(len(course))
#the len function is really restricted to strings is generally multipurposed

#when a function belongs to a particular structure it is called a method
#for strings the are prefixed by dot

print(course.upper())
print(course.lower())
print(course)

#we the following for finding characters in a string
print(course.find('P'))
print(course.find('beginners'))
print(course.find('e'))
#note that the find method is case sensitive and starts at beginning of what is needed word wise
#if character is not find negative 1 is show in the terminal

#the following is for replacing in strings
print(course.replace('Python', 'HTML'))

#we also have the in operator to check the existence of a character in a list. note that the difference between the in and the find is that the find shows index position while the in shows bolean

print('Python' in course)