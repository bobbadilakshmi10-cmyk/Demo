#sutndent Attendence
n=int(input("enter the no of students:"))
present=0
for i in range(1,n+1):
    student=input("enter attendence (p/a):")
    if student=="p":
        present+=1
absent=n-present
print("\n attendence summary")
print("total no of counts",n)
print("total present:",present)
print("total absent:",absent)

enter the no of students:3
enter attendence (p/a):p
enter attendence (p/a):f
enter attendence (p/a):f

 attendence summary
total no of counts 3
total present: 1
total absent: 2

#student details
'''student_name=input("enter the name:")
college_name=input("enter the college name:")
branch=input("enter the branch name")
college_fee=int(input("enter the college fee:"))
hostal_fee=int(input("enter the hostal fee:"))
c=college_fee+hostal_fee
print("student name",student_name)
print("college name",college_name)
print("branch name",branch)
print("total fee",c)

enter the name:lakshmi
enter the college name:kbn
enter the branch namecsc
enter the college fee:12
enter the hostal fee:12
student name lakshmi
college name kbn
branch name csc
total fee 24'''
            
            
            
