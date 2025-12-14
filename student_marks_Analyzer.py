#Take marks of n students
#Calculate average,highest and lowest

def average(marks):
    total=0
    for m in marks:
        total+=m
    return total/len(marks)

num=int(input("Enter number of students: "))
marks=[]

for i in range(num):
    marks.append(int(input("Enter marks: ")))      #add marks obe by one

print(f"Average: {average(marks)}")
print(f"Highest: {max(marks)}")
print(f"Lowest: {min(marks)}")

