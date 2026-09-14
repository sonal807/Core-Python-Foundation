#Walrus Operator: The Walrus Operator (:=) is an assignment expression operator in Python 
#that allows us to assign a value to a variable and use that value within the same expression.

#Normal assignment
name = "Aman"    #Here frist the value is assigned
print(name)      #And then it is used

#Walrus (:=) opertor
print(name := "Sonal")    #here we can assign value and use it in same line

#Basic syntax:
# variable := expression   #But there is one thing to remember it can be used as a standalone statement

#The main purpose of walrus operator is to assign inside expresseion

#example:
#x := 10    #If we write this alone it will not work and will show syntax error

print(x := 10)  #It will run smoothly


#Wlarus operator in if statement:

#normal approach
num = 10

if num > 10 :
    print("Number is greater than 5")

#With walrus operator
if(number := 10) > 5:  #Here (number := 10) first assigns 10 in number and then checks condition > 5
    print("The number is greater than 5")

#Example:
#Normal approach
name = input("Enter your name: ")

if len(name) > 5:
    print(name)

#With walrus
if ((name := input("Enter the name:")) and len(name)>5):   #Usually it make clearer to use parantheses with comparison
    print (name)


#Walrus operator with while

#Without walrus:
name = input("Enter your name: ")

while name != "quit":
    print(f"Hello, {name}")
    name = input("Enter your name: ")  #Here we have to use input two times one outside loop and another inside loop

#With walrus (:=)
while (name := input("Enter your name: ")) != "quit":  #here taking input, storing in name and comparing it is done in same line
    print(f"Hello, {name}")


# Walrus (:=) with list

# Suppose we have to calculate the lenght of list and check it at the same time
numbers = [10, 20, 30, 35, 30, 35]

if(length := len(numbers)) > 3:
    print(f"List has {length} elements")

#The main advantage of walrus opertor is that if we want to calculate and immediately use the result
#of any expression so we can use it and avoid unnecessary repetition.

#Withot walrus:
text = input("Enter something: ")

if len(text) > 5:
    print(f"Length: {len(text)}")  #Here we have to calculate len(text) two times

#With walrus:
text = input("Enter Something: ")

if (length := len(text)) > 5:  #Here its calculated once
    print(f"Length: {length }")


#= → Assignment
#:= → Assignment + Expression

#Example:
if (marks := 75) > 50:
    print("Marks is greater than 50")

#Example:
print(x := 20)

#Example:
while (number := int(input("Enter the number: "))) !=0:
    print(f"You entered: {number}")

#Example:
if (n := len([1, 4, 5, 6, 7])) > 3:
    print(f"List is too long({n} elements, expected <= 3)")