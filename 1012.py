
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


class Area_Calculator:
    a: float
    b: float
    c: float

    triangle_area: float
    circle_area: float
    trapeze_area: float
    square_area: float
    rectangle_area: float

    def __init__(self, first_value, second_value, third_value):
        self.a = first_value
        self.b = second_value
        self.c = third_value

        self.set_all_areas()

    def set_triangle_area(self):
        self.triangle_area = self.a * self.c / 2

    def set_circle_area(self):
        PI = 3.14159
        self.circle_area = PI*self.c**2

    def set_trapeze_area(self):
        self.trapeze_area = (self.a + self.b)*self.c/2

    def set_square_area(self):
        self.square_area = self.b**2

    def set_rectangle_area(self):
        self.rectangle_area = self.a*self.b

    def set_all_areas(self):
        self.set_triangle_area()
        self.set_circle_area()
        self.set_trapeze_area()
        self.set_square_area()
        self.set_rectangle_area()

    def log_all_areas(self):
        print(f'TRIANGULO: {self.triangle_area:.3f}')
        print(f'CIRCULO: {self.circle_area:.3f}')
        print(f'TRAPEZIO: {self.trapeze_area:.3f}')
        print(f'QUADRADO: {self.square_area:.3f}')
        print(f'RETANGULO: {self.rectangle_area:.3f}')


# Calling funcs, objects and solvind the problem
ENTRY = process_inputs(n_params=3, r_type=float)
A, B, C = ENTRY
my_area_calculator = Area_Calculator(A, B, C)
my_area_calculator.log_all_areas()
