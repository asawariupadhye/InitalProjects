## Problem statement 1: We need to define correct variables for the below requirement
### We checkin a patient named John Smith.
### He is 20 years old and is a new patient


name = "John Smith"
age = 20
is_new = True

## Problem statement 2: We need a mechanism to take input from the terminal for the person's name,
## age and his new/old patient's status. Following this the summary needs to be printed.

name = input("Please tell me the patient's name ")
age = input("What is the patient's age? ")
is_new = input("Is the patient new or old? ")
status = "an existing"

if is_new == "no":
    status = "an old "

print("Hello " + name + ". You are " + str(age) + " old and seems you are " + status + "patient")

