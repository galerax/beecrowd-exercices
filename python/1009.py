
# This is a generic function able to return params according to the data type desired
def process_inputs(n_params, r_type = int):
    params = [r_type(input()) for param in range(n_params)]
    return tuple(params)

# Function that returns the salary + commission for some variables given
def get_total_salary(base_salary, sales_amount, commision_rate):
    commission = commision_rate*sales_amount
    return base_salary + commission

# Function that logs the total salary
def log_salary(salary:float):
    print(f'TOTAL = R$ {salary:.2f}')

# Calling the respective funcs and solving the problem

# This deletes globaly the first input wich is 'name' and isnt't used for anything relevant
NAME = input()
del NAME 

base_salary, sales_amount = process_inputs(n_params = 2, r_type = float)
salary = get_total_salary(base_salary,sales_amount, 0.15)
log_salary(salary)
