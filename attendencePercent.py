
totalclasses  = int(input("Enter the total classes"))
classesattended = float(input("Enter the classesattended"))

attendence = (classesattended / totalclasses) * 100

if (totalclasses == classesattended):
    print("The attendence is 100%")

else:
    print(attendence)
       