Student_ID=int(input("Please enter your ID:"))
print(Student_ID)

Student_name=input("Please enter your name:")
print(Student_name)

Student_attendence=float(input("Please enter your attendence:"))
print(Student_attendence)

print("_________")

scores=[]#assigning variable to collect values

while True:# dynamic assignmet whhen no of loops unknown
    score=float(input("Enter score:"))
    scores.append(score) 
    choice=input("Do you want another score:")
    if choice!='yes':
        break
total_score=sum(scores)
count_score=len(scores)  
average_score=total_score/count_score

                  # grading based on avg score
if average_score>=85:
    print("Grade A")
elif average_score>=70 and average_score<=85:
    print("Grade B")
elif average_score>=69 and average_score<=50:
    print("Grade C")
else:
    print("Grade D")
print("__________")

                    #attendance Warning
if Student_attendence>=75:
    print("Ok Good Attendence")
else:
    print("Warning low Attendance")
print("____________")

                        #Award eligibility
if Student_attendence>=75 and average_score>=85:
    print("Award Eligibility")
else:
    print("Not eligible for Award")
print("___________________")







