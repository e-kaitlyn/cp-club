

grades = ["A+","A","A-","B+","B","B-","C+","C","C-","D+","D","F"]
score = [4.0,4.0,3.7,3.3,3.0,2.7,2.3,2.0,1.7,1.3,1.0,0]
n=0
t=0
while True:
    grade = input()
    if grade == '':
        break
    ind = grades.index(grade)
    t+=score[ind]
    n+=1

print(t/n)