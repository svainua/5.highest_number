# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

highest_score = 0
for HS in student_scores:
  if HS > highest_score: # компьютер сравнивает каждое число сначала с заданным параметром 0, а потом с каждым последующим числом, которое заменят предыдущее, если оно больше, либо проскакивает, если оно меньше. В итоге остается самое большое число
    highest_score = HS
print (f" The highest score in the class is: {highest_score}")
