stdname =input("Enter the student name:")
stdno =int(input("Enter stdno:"))
stdgroup =input("Enter the group:")
sub01= int(input("C-programming Marks:"))
sub02= int(input("Data structures Marks:"))
sub03= int(input("Python Marks:"))
sub04= int(input("Java Marks:"))
sub05= int(input("Operating System Marks:"))
sub06= int(input("DBMS Marks:"))
total= sub01+sub02+sub03+sub04+sub05+sub06
avg= total/6
if avg>=91:
         print("O-grade")
elif avg>=81:
         print("A-grade")
elif avg>=71:
         print("B-grade")
elif avg>=61:
         print("C-grade")
elif avg>=51:
         print("D-grade")
elif avg<=35:
         print("FAIL")
else:
    print("PASS")
        


