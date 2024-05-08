grades = ["A+","A","A-","B+","B","B-","C+","C","C-","D+","D","F"]
score = [4.0,4.0,3.7,3.3,3.0,2.7,2.3,2.0,1.7,1.3,1.0,0]
grade = input()

if grade in grades:
    ind = grades.index(grade)
    print(score[ind])
else:
    print("this is a invalid grade")