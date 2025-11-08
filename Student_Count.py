student_heights = input("Input a list of student heights ").split()
'''for n in range(0, len(student_heights), 1):
  student_heights[n] = int(student_heights[n])'''
total_height = 0
for height in student_heights:
  total_height += int(height)
print(total_height)

total_students = 0
for i in student_heights:
  total_students += 1
print(total_students)
