#finding substring in a string
#creating a substring using string slicing
def create_substring(string,start,end):
    sub_string=string[start:end+1]
    return sub_string
def find_substring(string,sub_string):
    s = string.split()
    if str(sub_string) in string:
        print("sub string is found")
    else:
         print("sub string is not found")

st=input("enter the string:")
#creation of sub string
s=int(input("enter the start index of sub string:"))
e=int(input("enter the last index of substring:"))
create=create_substring(st,s,e)
print("the substring is\t" +create)
#finding the substring you created
find_substring(st,create)
#you can create your substring
s_s=input("enter the sub string:")
find_substring(st,s_s)