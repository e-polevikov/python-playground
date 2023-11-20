import fib
import numpy as np


def print_first_ten_fib_numbers():
    print("The first ten fibonacci numbers are the following:")

    for i in range(10):
        print(f"fib({i}) = {fib.fib(i)}")
    
    print()


def run_linear_equation_sample():
    a = np.array([[1, 2], [3, 5]])
    b = np.array([1, 2])
    x = np.linalg.solve(a, b)

    print(f"Let A =\n {a} \nand b =\n {b}")
    print("Then an equation Ax=b has the following solution:")
    print(f"x = {x}.")

def main():
    print("Hello!", end='\n\n')
    
    print_first_ten_fib_numbers()
    run_linear_equation_sample()


if __name__ == "__main__":
    main()
