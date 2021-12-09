#declare a variable. When the value is about to be stored in the memory, it gets converted
#into  its binary form

name = "Andrew"
age = 10
print(name + "'s age is " + str(age))
#note: string and int cannot be concatenated, hence we use the str() function

#updating variable(s)
age = age+10
print(name + "'s age after 10 years is " + str(age))

#python is a case sensitive language so True and False should be just that
is_updated = True
#if is_updated = true, python does not understand it

##################################################################
##################################################################

#Taking an input

##################################################################

name = input("What is your name? ")

print("Hi "+ name)
