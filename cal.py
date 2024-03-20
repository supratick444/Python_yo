
# Read command line argument :
import sys   #module that is used.

#Read the environment variables we need this module !!
import os 

print(os.getenv("password"))
print(os.getenv("token"))

def add(num1 , num2):
    return num1 + num2


num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == "add" :
    output = add(num1,num2)
    print(output)