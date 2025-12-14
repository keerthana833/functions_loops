#Ask user how many numbers they wants to check
#for each number:
             #check if it is prime 
             #print the result

def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        #check if number is divisible by any number
        if n%i==0:          
            return False    #if yes,return false
    return True


number=input("How many numbers you would like to check? ")
#checking if it is a digit
if number.isdigit():        
    number=int(number)

    for _ in range(number):
        num=input("Enter a number: ")
        if num.isdigit():
            num=int(num)
            if is_prime(num):
                print(f"{num} is a prime number")
            else:
                print(f"{num} is not a prime number")
        else:
            print("Invalid!please enter positive whole numbers")
else:
    print("Invalid!please enter positive whole numbers")
