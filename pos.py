#check if a number is positive or negative or zero
def checking(number):
    if number>0:
        print("positive number")
    elif number<0:
        print("negative number")
    else:
        print("zero")

n=int(input("enter the number:"))
checking(n)