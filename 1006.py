
# This is a generic function able to return params according to the data type desired
def process_inputs(params=[], r_type = int):
    for param_index in range(len(params)):
        params[param_index] = r_type(input())
    return tuple(params)

# Function that returns the mean of some variables given
def get_ponderate_mean(grades:list, weights:list):
    sum_grades = sum([grades[i] * weights[i] for i in range(len(grades))])
    sum_weights = sum(weights)
    return sum_grades/sum_weights

# Function that logs the mean
def log_prod(mean:float):
    print(f'MEDIA = {mean:.1f}')

# Calling the respective funcs and solving the problem
n1:int = 0
n2:int = 0
n3:int = 0

n1,n2, n3 = process_inputs([n1,n2,n3], float)
result = get_ponderate_mean([n1,n2,n3], [2,3,5])
log_prod(result)
