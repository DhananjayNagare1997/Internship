#!/usr/bin/env python
# coding: utf-8
Q11 to Q15 are programming questions. Answer them in Jupyter Notebook.
11.	Write a python program to find the factorial of a number.
12.	Write a python program to find whether a number is prime or composite.
13.	Write a python program to check whether a given string is palindrome or not.
14.	Write a Python program to get the third side of right-angled triangle from two given sides.
15.	Write a python program to print the frequency of each of the characters present in a given string.
11.	Write a python program to find the factorial of a number.
# In[4]:


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(2,n+1):
            fact *= i
        return fact
#Taking the user input for calculate a factorial.
num = int(input("Enter a number to calculate the factorial"))

#Check for the number was not negative.
if num < 0:
    print("Factorial can't calculate of negative numers")
else:
    result = factorial(num)
    print(f"The factorial of {num} is: {result}")

12.	Write a python program to find whether a number is prime or composite.
# In[6]:


def check_prime_or_composite(n):
    if n <= 1:
        return "Neither prime nor composite"
    elif n == 2:
        return "Prime"
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return "Composite"
        return "Prime"

# Taking user input
num = int(input("Enter a number to check if it's prime or composite: "))

result = check_prime_or_composite(num)
print(f"The number {num} is {result}")

13.	Write a python program to check whether a given string is palindrome or not.
# In[10]:


def is_palindrome(s):
    #Removing space & Convert it into lowercase.
    s = s.replace(" ", "").lower()
    
    #Comparing string with it's reverse.
    if s == s[::-1]:
        return True
    else:
        return False
    
#User input String for check the palindrome.   
string = input("Enter a string to check for Palindrome")

if is_palindrome(string):
    print(f"The string '{string}' is a palindrome.")
else:
    print(f"The string '{string}' is not a palindrome.")

14.	Write a Python program to get the third side of right-angled triangle from two given sides.
# In[24]:


def cal_hypotenuse(a, b):
    hypotenuse = ((a**2) + (b**2))**0.5
    return hypotenuse

# Taking user input for the lengths of the two sides
side1 = float(input("Enter the length of the first side of the right-angled triangle: "))
side2 = float(input("Enter the length of the second side of the right-angled triangle: "))

# Calculate the hypotenuse (third side)
hypotenuse = cal_hypotenuse(side1, side2)

print(f"The length of the hypotenuse (third side) is: {hypotenuse:.2f}")

15.	Write a python program to print the frequency of each of the characters present in a given string.
# In[27]:


def cal_character_frequency(input_string):
    # Creating an empty dictionary to store character frequencies
    frequency = {}
    
    # Counting frequency of each character in the string
    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
            
    # Displaying the character frequencies
    print("Character frequencies in the given string:")
    
    for char, freq in frequency.items():
        print(f"'{char}' occurs {freq} time(s)")
        
# Taking user input for the string
user_ip_string = input("Enter a string: ") 

# Calling the function to find and display character frequencies
cal_character_frequency(user_ip_string)


# In[ ]:





# In[ ]:





# In[ ]:




