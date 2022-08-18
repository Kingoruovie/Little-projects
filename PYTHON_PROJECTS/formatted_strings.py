#formatted strings is used for dynamically concatenating strings
#it is usually prefixed by a 'f'
#it is more like writing english sentence but placeholders like variable names are witte in curly bracket

#example
first_name = "Ovie"
last_name = "Oru"
#instead of
message = first_name + " [" + last_name + "] is a programmer"
print(message)
#we use
msg = f'{first_name} [{last_name}] is a programmer'
print(msg)