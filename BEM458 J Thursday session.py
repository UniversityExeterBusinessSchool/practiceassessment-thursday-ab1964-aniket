#######################################################################################################################################################
# 
# Name:Aniket Bhardwaj
# SID:740096239
# Exam Date:27/03/2025
# Module: BEMM458 (Programming for Business Analytics)
# Github link for this assignment:  https://github.com/UniversityExeterBusinessSchool/practiceassessment-thursday-ab1964-aniket
#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.

# ######################################################################################################################################################
# Question 1 - Loops
# Create a list and use a for loop to answer the following question:
# You are given a dictionary called key_comments. Your allocated keys are the first and last digit of your SID.
# Find the start and end position of each of the items in the sentence using the find command.
# Create and populate a list called my_list with a tuple of (start location, end location) for each value in comments 
 

customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."
"""

# List of words to search for
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',
    8: 'overall',
    9: 'minor'
}

# Write your search code here and provide comments. 

# Initialize an empty list to store (start, end) positions
my_list = []

# Loop through each word in the dictionary

for key in key_comments:
    word = key_comments[key]
    start = customer_feedback.find(word)# finding the starting index of the word
    if start != -1: # if word is found then calculate the end index
        end = start + len(word)
        my_list.append((start, end))# storing the indexes in the tuple
    
    else:
        print("Word is not found")

# Print the list of positions
print("statinga position and ending position of the words in the list are:", my_list)

#OUTPUT
#statinga position and ending position of the words in the list are: 
# [(38, 50), (12, 17), (114, 120), (88, 94), (142, 150), (99, 109), (18, 28), (129, 136), (51, 58), (82, 87)]

##########################################################################################################################################################

# Question 2 - Functions
# Scenario - You are working in an e-commerce firm as a business analyst, and your manager has tasked you to generate weekly reports on financial metrics like 
# Operating Profit Margin, Revenue per Customer, Customer Churn Rate, and Average Order Value. Use Python functions 
# that will take the values and return the metric needed. Use the first two and last two digits of your ID number as the input values.

# Insert first two digits of ID number here:
# Insert last two digits of ID number here:

# Write your code for Operating Profit Margin

# Write your code for Revenue per Customer

# Write your code for Customer Churn Rate

# Write your code for Average Order Value

# Call your designed functions here


#CODE
# Insert your SID digits here:
first_two_digits = 74  
last_two_digits = 39  

# input the values
revenue = 10000 + first_two_digits * 100  
operating_profit = 2500 + last_two_digits * 10
num_customers = 200 + first_two_digits
lost_customers = 15 + last_two_digits
total_orders = 300 + last_two_digits
total_sales_value = 15000 + first_two_digits * 50

# ---------------------- #
# 1. Operating Profit Margin
def operating_profit_margin(profit, revenue):
    """Return operating profit margin as a percentage."""
    if revenue == 0:
        return 0
    return (profit / revenue) * 100

# 2. Revenue per Customer
def revenue_per_customer(revenue, customers):
    """Return average revenue per customer."""
    if customers == 0:
        return 0
    return revenue / customers

# 3. Customer Churn Rate
def churn_rate(lost, total):
    """Return churn rate as a percentage."""
    if total == 0:
        return 0
    return (lost / total) * 100

# 4. Average Order Value
def average_order_value(sales_value, orders):
    """Return average order value."""
    if orders == 0:
        return 0
    return sales_value / orders

# ---------------------- #
# Call and print results
print("Weekly Financial Metrics Report")
print("-" * 35)
print("Operating Profit Margin: {:.2f}%".format(operating_profit_margin(operating_profit, revenue)))
print("Revenue per Customer: {:.2f}".format(revenue_per_customer(revenue, num_customers)))
print("Customer Churn Rate: {:.2f}%".format(churn_rate(lost_customers, num_customers)))
print("Average Order Value: {:.2f}".format(average_order_value(total_sales_value, total_orders)))


#Output
# Weekly Financial Metrics Report
# -----------------------------------
# Operating Profit Margin: 16.61%
# Revenue per Customer: 63.50
# Customer Churn Rate: 19.71%
# Average Order Value: 55.16

##########################################################################################################################################################

# Question 3 - Regression
# A retail store has collected data on seasonal sales and price changes. The table below shows different price levels and their corresponding demand.
# Develop a linear regression model and determine:
# 1. The price at which the store can maximize revenue
# 2. The demand when the price is set at £52

"""
Price (£)    Demand (Units)
---------------------------
20           300
25           280
30           260
35           240
40           210
45           190
50           160
55           140
60           120
65           100
70           85
"""

# Write your code here
# import the libraries
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# defining dependent and independent variables for linear regression
price = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 75]).reshape(-1, 1)
demand = np.array([300, 280, 260, 240, 210, 190, 160, 140, 120, 100, 85]).reshape(-1, 1)

# Loading Linear regression model
model = LinearRegression()
#Fitting the dependent and independent variable in our model
model.fit(price,demand)

# Making the predictions
predict_value_1 = model.predict(max(demand))
predict_value_2 = model.predict(np.array[[52]])

# Printing the values
print("Predicted value with max revenue",predict_value_1[0][0])
print("Predicted value when price is 52",predict_value_2[0][0])

# Plotting the data for getting the regression line
plt.scatter(price, demand, color = 'green')
plt.plot(price, model.predict(price), color = 'red')
plt.xlabel("price")
plt.ylabel("demand")
plt.title("Price vs Demand")
plt.show()



##########################################################################################################################################################

# Question 4 - Debugging; Plotting and data visualization chart

import random
import matplotlib.pyplot as plt

# Generate 100 random numbers between 1 and student id number
max-value = integer(input("Enter your Student ID: ")) 
random_numbers = [random.randint(1, max_value) for i in range(0,100)]

# Plotting the numbers in a line chart
plt.plot(random_numbers, marker='O', markercolor='green', markeredgcolor='red', linestyle='--', lable='Random Numbers', color='blue');
plt.title("Line Chart of 100 Random Numbers")# added the quotes as the text is string and for text we have to use quotes.
plt.xlabel="Index"
plt.ylabel="Random Number"
plt.legend('---')
plt.grid(True)
plt.show()


# Corrected code
import random
import matplotlib.pyplot as plt

# Generate 100 random numbers between 1 and student id number
max_value = int(input("Enter your Student ID: ")) # chnages integer to int and changes the variable name from max-value to max_value as '-' is not allowed in python while declaring the variable name.
random_numbers = [random.randint(1, max_value) for i in range(0,100)]

# Plotting the numbers in a line chart
#plt.plot(random_numbers, marker='O', markercolor='green', markeredgcolor='red', linestyle='--', lable='Random Numbers', color='blue');
plt.plot(random_numbers, marker='o', markeredgecolor='red', linestyle='--', label='Random Numbers', color='blue')# I have removed markercolor='green' attribute as it does not exist in matplotlib and also replaced marker='O' with marker='o'

plt.title("Line Chart of 100 Random Numbers")# added the quotes as the text is string and for text we have to use quotes.
plt.xlabel="Index"
plt.ylabel="Random Number"
plt.legend('---')
plt.grid(True)
plt.show()

# OUTPUT
#Enter your Student ID:  740096239

