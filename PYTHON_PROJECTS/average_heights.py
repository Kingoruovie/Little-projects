# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split(",")
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

total_score = 0
number_of_students = 0

for heights in  student_heights:
  total_score += heights
  number_of_students += 1
print(f'The total height is {total_score}')
print(f'There are {number_of_students} students in total')
average = total_score / number_of_students
average = round(average)

print(f"The average height rounded to the nearest whole number is {average}")
