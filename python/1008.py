
# This is a generic function able to return params according to the data type desired
def process_inputs(n_params, r_type = int):
    params = [r_type(input()) for param in range(n_params)]
    return tuple(params)

# Function that returns the salary for some variables given
def get_salary(hours_spent, hour_value):
    return hours_spent*hour_value

# Function that logs the difference
def log_salary(n_worker,salary:float):
    print(f'NUMBER = {n_worker:.0f}')
    print(f'SALARY = U$ {salary:.2f}')

# Calling the respective funcs and solving the problem

n_worker, hours_spent, hour_value = process_inputs(n_params = 3, r_type = float)
salary = get_salary(hours_spent, hour_value)
log_salary(n_worker,salary)
