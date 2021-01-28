def gradingStudents(grades):
  final_grades=[]
  for i in grades:
    if i<38:
      final_grades.append(i)
    else:
      j=i
      while(j):
        if j%5==0:
            t=j-i
            if t<3:
              final_grades.append(j)
            else:
              final_grades.append(i)
            break
        j=j+1
  return final_grades
n=int(input())
grades=[]
for i in range(n):
  grades.append(int(input()))
for i in gradingStudents(grades):
  print(i)
