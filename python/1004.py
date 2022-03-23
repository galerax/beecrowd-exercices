
# This is a generic function able to return params according to the data type desired
def process_inputs(params=[], r_type = int):
    for param_index in range(len(params)):
        params[param_index] = r_type(input())
    return tuple(params)

# Function that returns the product of some variables given
def get_prod(params = []):
    result = 1
    for param in params:
        result *= param
    return result

# Function that logs the productS
def log_prod(prod:int):
    print(f'PROD = {prod}')

# Calling the respective funcs and solving the problem
n1:int = 0
n2:int = 0

n1,n2 = process_inputs([n1,n2], int)
result = get_prod([n1,n2])
log_prod(result)