num1 = 3
num2 = 21
result = num1 + num2

print ("The sum of",num1, "and",num2,"is",result) # With default separator

print ("The sum of",num1, "and",num2,"is",result, sep="$") #With custom separator "$"

print ("The result is",end="\n\n") #With end set to ... to have a "reverse" of break
print ("nothing")

statement = "The result is "
print (statement + str(3)) #Concatenating string with a number


name = "Allan"
age = 356
print("{0} is {1} years old.".format(name, age)) #Use .format() function to replace field in print string

print (f"Hello {name} is {age} years old.") #Print with f string