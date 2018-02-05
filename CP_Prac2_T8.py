#Computing Practical 2 - Task 8

student_number = int(input("Input number of students: "))

student_name = []
student_score = []

name_1 = 0
score_1 = 0
name_2 = -1
score_2 = -1

for i in range(student_number):
    student_name.append(input("Input student name: "))
    student_score.append(int(input("Input student score: ")))
    
    if student_score[i] > score_1:
        score_2 = score_1
        name_2 = name_1
        
        score_1 = student_score[i]
        name_1 = student_name[i]
    
    elif student_score[i] > score_2:
        score_2 = student_score[i]
        name_2 = student_name[i]
        
print("The highest scoring student is {0} with {1} marks. The second highest scoring student is {2} with {3} marks." .format(name_1, score_1, name_2, score_2))
