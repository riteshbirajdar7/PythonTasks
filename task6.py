""" A student is eligible if -
Age is between 17 and 25, inclusive
12th percentage ≥ 60
Entrance percentage ≥ 50
Attendance ≥ 75
Documents are available
"""
age= int(input("Enter age="))
percentage_12th=float(input("Enter percentage marks="))
entrance_percentage= float(input("Enter entrance percentage="))
attendance_percentage= float(input("Enter attendance percentage="))
documents=input("Do you have all required documents (Yes/No)?=")
def booldocuments(documents:str)->bool:
    if documents=="Yes":
        return True
    else:
        return False
if (17<=age<=25)and (percentage_12th>=60) and (entrance_percentage>=50)and (attendance_percentage >= 75) and (booldocuments(documents)==True):
    print("The candidate is eligible")