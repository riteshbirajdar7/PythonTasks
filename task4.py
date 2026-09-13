name=input("Enter Student Name = ")
age=int(input("Enter student age: "))
maths=float(input("Enter maths marks: "))
physics=float(input("Enter physics marks: "))
computer=float(input("Enter computer marks: "))
total_marks= maths+physics+computer
print(f"Total Marks={total_marks}")
avg=total_marks/3
print(f"Average Marks={avg}")
