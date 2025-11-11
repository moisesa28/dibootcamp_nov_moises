#Exercise 1 : Student Grade Summary
# Instructions
# You are given a dictionary containing student names as keys and 
# lists of their grades as values. Your task is to create a summary 
# report that calculates the average grade for each student, assigns a 
# letter grade, and determines the class average.

#Initial Data:
student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}
#Calculate the average grade for each student and store the 
# results in a new dictionary called student_averages.
student_averages = {}
for names,grades in student_grades.items():
    average = sum(grades)/len(grades)
    student_averages[names]=average


#Assign each student a letter grade (A, B, C, D, F) based on their average grade according to the following scale, and store the results in a dictionary called student_letter_grades:
# A: 90 and above
# B: 80 to 89
# C: 70 to 79
# D: 60 to 69
# F: Below 60
student_letter_grades = {}
for name, avg in student_averages.items():
    if avg >= 90:
         grade = 'A'
    elif avg >= 80:
        grade = 'B'
    elif avg >= 70:
        grade = 'C'
    elif avg >= 60:
        grade = 'D'
    else:
        grade = 'F'
    student_letter_grades[name] = grade

#Calculate the class average (the average of all students’ averages) and print it.
total_average = sum(student_averages.values())
class_size = len(student_averages)
class_average = total_average / class_size

print(student_averages)
print(student_letter_grades)
print(class_average)

max_name_length = max(len(name) for name in student_grades.keys())

for name in student_grades.keys():
    spaces = ' ' * (max_name_length - len(name))
    print(f"{name}:{spaces} Average Grade = {student_averages[name]:.2f}, Letter Grade = {student_letter_grades[name]}")

print(' ')
print('------')
#Exercise 2 : Advanced Data Manipulation and Analysis
# Instructions
# In this exercise, you will analyze data from a hypothetical online
# retail company to gain insights into sales trends and customer behavior. 
# The data is represented as a list of dictionaries, where each dictionary 
# contains information about a single purchase.
sales_data = [
    {"customer_id": 1, "product": "Smartphone", "price": 600, "quantity": 1, "date": "2023-04-03"},
    {"customer_id": 2, "product": "Laptop", "price": 1200, "quantity": 1, "date": "2023-04-04"},
    {"customer_id": 1, "product": "Laptop", "price": 1000, "quantity": 1, "date": "2023-04-05"},
    {"customer_id": 2, "product": "Smartphone", "price": 500, "quantity": 2, "date": "2023-04-06"},
    {"customer_id": 3, "product": "Headphones", "price": 150, "quantity": 4, "date": "2023-04-07"},
    {"customer_id": 3, "product": "Smartphone", "price": 550, "quantity": 1, "date": "2023-04-08"},
    {"customer_id": 1, "product": "Headphones", "price": 100, "quantity": 2, "date": "2023-04-09"},
]

#Total Sales Calculation: Calculate the total sales for each product category
# (i.e., the total revenue generated from each type of product). 
# Use a loop to iterate through the data and a dictionary to store the 
# total sales for each product.
total_sales_by_product = {}
for sale in sales_data:
    product = sale['product']
    revenue = sale['price'] * sale['quantity']
    total_sales_by_product[product] = total_sales_by_product.get(product, 0) + revenue

print(total_sales_by_product)
print('')
#Customer Spending Profile: Determine the total amount spent by each customer.
# Use a dictionary to maintain the sum of amounts each customer has spent.
total_spent_by_customer = {}
for sale in sales_data:
    customer_id = sale['customer_id']
    revenue = sale['price'] * sale['quantity']
    total_spent_by_customer[customer_id] = total_spent_by_customer.get(customer_id, 0) + revenue

print(total_spent_by_customer)
print('')

#Sales Data Enhancement:
# Add a new field to each transaction called “total_price” that 
# represents the total price for that transaction (quantity * price).
# Use a loop to modify the sales_data list with this new information.
for transaction in sales_data:
    transaction["total_price"] = transaction["price"] * transaction["quantity"]

#High-Value Transactions:
# Using list comprehension, create a list of all transactions where the total price is greater than $500.
# Sort this list by the total price in descending order.
