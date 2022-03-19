
# This is a generic function able to return params according to the data type desired
def process_inputs(params=[], r_type = int):
    for param_index in range(len(params)):
        params[param_index] = r_type(input())
    return tuple(params)

# Function that returns the mean of some variables given
def get_mean(params:dict):
    sum_grades = sum([key*params[key] for key in params.keys()])
    sum_weights = sum([params[key] for key in params.keys()])
    result = sum_grades/sum_weights
    return result

# Function that logs the mean
def log_prod(mean:float):
    print(f'MEDIA = {mean:.5f}')

# Calling the respective funcs and solving the problem
n1:int = 0
n2:int = 0

n1,n2 = process_inputs([n1,n2], float)
result = get_mean({
    n1:3.5,
    n2:7.5
})
log_prod(result)
