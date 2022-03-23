
# This is a generic function able to return params according to the data type desired
def process_inputs(n_inputs=1, n_params=1, r_type=int):
    inputs = [input().split() for i in range(n_inputs)]
    for input_index in range(len(inputs)):
        for entry_index in range(len(inputs[input_index])):
            inputs[input_index][entry_index] = r_type(
                inputs[input_index][entry_index])

    return tuple(inputs)


# Function that returns the total to pay for a product based on qnt and unitary value
def get_total_to_pay(qnt, unitary_value):
    return qnt*unitary_value


# Function that logs the total to pay
def log_total(first_total, second_total):
    print(f'VALOR A PAGAR: R$ {(first_total+second_total):.2f}')


first_entry, second_entry = process_inputs(
    n_inputs=2, n_params=3, r_type=float)
id_1, qnt_1, value_1 = first_entry
id_2, qnt_2, value_2 = second_entry

first_total = get_total_to_pay(qnt_1, value_1)
second_total = get_total_to_pay(qnt_2, value_2)

log_total(first_total, second_total)
