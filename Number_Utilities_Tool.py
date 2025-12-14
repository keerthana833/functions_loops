#Take a number and show-
#count of digits
#reverse of numbers
#sum of digits

def count_digits(n):
    count=0
    if n==0:
        return 1
    #loop until all digits are processed
    while n!=0:   
        n//=10  #removes last digit
        #count increases when ever digit removed   
        count+=1  
        return count
    
def reverse_number(n):
    rev=0
    while n!=0:
        #shifts digit left and adds last digit of n
        # ex:[123]=0x10+[3]=(3) ,3x10+[2]=3(2) ,32x10+[1]=320(1) = (3)(2)(1)
        rev=rev*10+n%10  
        n//=10             
    return rev

def sum_of_digits(n):
    sum=0
    while n!=0:
        #extracts last digit and adds it
        sum+=n%10    
        n//=10              
    return sum
num=input("Enter a number: ")
if num.isdigit():
    num=int(num)
    print(f"digits :{count_digits(num)}")
    print(f"Reverse :{reverse_number(num)}")
    print(f"Sum :{sum_of_digits(num)}")
else:
    print("Invalid input,please enter a positive integer")