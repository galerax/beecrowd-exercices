
# This is a generic function able to return params according to the data type desired
def process_inputs(n_params: int = 1, r_type=int):
    params = [r_type(input()) for param in range(n_params)]
    if n_params > 1:
        return tuple(params)
    else:
        return params[0]


# This function return the volume of a shpere based on a global const "CONST_PI" and a given radius "r"
def sphere_volume(r):
    result = 4/3*PI*r**3
    return result


# Function that logs the shpere volume
def log_volume(volume: float):
    print(f'VOLUME = {volume:.3f}')


# Calling the respective funcs and solving the problem
PI = 3.14159
R = process_inputs(r_type=float)
(VOLUME): float = sphere_volume(R)
log_volume(VOLUME)
