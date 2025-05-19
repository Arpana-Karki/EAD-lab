

# Practice:
name ="Abcd Karki"
age =22
patient_type ="new patient" # Or use: is_new = True
print(name +" is a " +  patient_type + " of " + str(age) + " years old.")


# Practice: WAP to ask a person's name and favorite color and, print a message including the person's name and favorite colour
person_name = input("What  is your name ? ")
personal_favorite_color = input("What is your favorite color ? ")
print(person_name +"'s favorite color is " + personal_favorite_color +".")


#Practice: WAP to ask a user their weight in pound, convert it to kilograms and print on the terminal
weight_in_pounds = input("What is your weight in pounds? ")
weight_in_kg = int(weight_in_pounds) * 0.453592 
print("Your weight in kilograms is: " + str(weight_in_kg) +" kilograms.") # 
print(type(weight_in_kg)) 
print(type(weight_in_pounds))


# Use of different types of quotes according to situation in python:
#Case 1: Use of ""
string1 = "Arpana's money"
print(string1)

#Case 2: Use of ''
string2 = 'My name is "Arpana Karki"'
print(string2)

#Case 3: Use of """ """ or ''' '''
description=""" 
My name is Arpana Karki.

I study at:
Gandaki College Of Engineering And Science
Lamachaur,Pokhara,Nepal

"""
description2 =''' 
I am currently studying "Bachelor Of Software Engineering".
I am writing this code for python practice.
'''
print(description)
print(description2)

print(string1[1:]) # prints from array index 1 to ending
print(string1[1:4]) # prints from array index 1 to 3
print(string1[:3]) # prints from array index 0 to 2
print(string1[3]) # prints value at array index 3 from front or left
print(string1[-2]) # prints value at array index 2 from back or right
print(string1[:]) # used just to copy a string , returns string value same as in previous variable


