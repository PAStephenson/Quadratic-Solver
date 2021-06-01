import math
import numpy as np

def real_roots(a, b, c):
    """Solves the quadratic if roots are real."""
    q = -(b + np.sign(b) * math.sqrt(calc_discriminant(a, b, c)))/(2) 

    root1 = q / a
    root2 = c / q

    print_real_roots(root1, root2)

def complex_roots(a, b, c):
    """Solves the quadratic if roots are complex."""
    real = -b/(2 * a)
    imaginary = (math.sqrt(abs(b**2 - 4 * a * c)))/(2 * a)

    root1 = complex(real, imaginary)
    root2 = root1.conjugate()

    print_complex_roots(root1, root2)

def print_real_roots(root1, root2):
    """Prints the real roots of the quadratic."""
    if root1 == root2:
        print('\nThe quadratic has one real root.')
        print(root1)
    else:
        print('\nThe quadratic has two real roots.')
        print(root1)
        print(root2)

def print_complex_roots(root1, root2):
    """Prints the complex roots of the quadratic."""
    print('\nThe quadratic has complex roots.')

    if root1.real == 0:
        print(f'{root1.imag}j')
        print(f'{root2.imag}j')
    else:
        print(root1)
        print(root2)

def calc_discriminant(a, b, c):
    """Calculates the discriminant of the quadratic."""
    discriminant = b**2 - 4 * a * c
    return discriminant

def check_solutions(a, b, c):
    """Checks the number and type of solutions of the quadratic."""
    discriminant = calc_discriminant(a, b, c)

    if discriminant >= 0:
        real_roots(a, b, c)
    else:
        complex_roots(a, b, c)

while True:
    a = input('Please insert the coefficient of the x^2 term: ')
    b = input('Please insert the coefficient of the x term: ')
    c = input('Please insert the coefficient of the constant term: ')

    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        print('Please enter numbers only.\n')
    else:
        break

check_solutions(a, b, c)
