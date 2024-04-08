#finding index of the element in the list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("the list of elements is:")
print(numbers)
element = int(input("enter the element:"))
start=int(input("enter the start index:"))
stop=int(input("enter the stop index:"))
index = numbers.index(element,start,stop)
print(index)