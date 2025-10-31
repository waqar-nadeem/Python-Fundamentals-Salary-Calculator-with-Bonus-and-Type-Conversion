basic_salary = input("Enter the Basic Salary: ")
b_percentage = input("Enter the Bonus Percentage: ")
basic_salary = float(basic_salary)
b_percentage = float(b_percentage)
bonus_amount = (b_percentage / 100) * basic_salary
salary = basic_salary + bonus_amount
print("The Total Salary is =", salary)
