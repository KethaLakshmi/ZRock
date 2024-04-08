#python program to add two numbers
def addition(a,b):
    result=a+b
    return result
m=int(input("enter first number:"))
n=int(input("enter second number:"))
add=addition(m,n)
print("addition of the two numbers is:"+str(add))