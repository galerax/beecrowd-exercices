
# This is a generic function able to return params according to the data type desired
def process_inputs(n_inputs=1, n_params=1, r_type=int):
    inputs = [input().split() for i in range(n_inputs)]
    for input_index in range(len(inputs)):
        for entry_index in range(len(inputs[input_index])):
            inputs[input_index][entry_index] = r_type(
                inputs[input_index][entry_index])
    return_values = []
    for input_index in range(len(inputs)):
        for entry in inputs[input_index]:
            return_values.append(entry)
    return tuple(return_values)
