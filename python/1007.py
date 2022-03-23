
# This is a generic function able to return params according to the data type desired
def process_inputs(params=[], r_type = int):
    for param_index in range(len(params)):
        params[param_index] = r_type(input())
    return tuple(params)

# Function that returns the difference of some variables given
def get_diff(values:list):
    a, b, c, d = tuple(values)
    return a*b-c*d

# Function that logs the difference
def log_diff(diff:float):
    print(f'DIFERENCA = {diff}')

# Calling the respective funcs and solving the problem
n1:int = 0
n2:int = 0
n3:int = 0
n4:int = 0

n1,n2, n3, n4 = process_inputs([n1,n2,n3, n4], int)
result = get_diff([n1,n2,n3, n4])
log_diff(result)
