import math

def real_roots(a, b, c):
    """Solves the quadratic if roots are real."""
    q = -(b + sign(b) * math.sqrt(calc_discriminant(a, b, c)))/(2) 

    root1 = q / a
    root2 = c / q

    return root1, root2

def complex_roots(a, b, c):
    """Solves the quadratic if roots are complex."""
    real = -b/(2 * a)
    imaginary = (math.sqrt(abs(b**2 - 4 * a * c)))/(2 * a)

    root1 = complex(real, imaginary)
    root2 = root1.conjugate()

    return root1, root2

def print_real_roots(solutions):
    """Prints the real roots of the quadratic."""
    if solutions[0] == solutions[1]:
        print('\nThe quadratic has one real root.')
        print(solutions[0])
    else:
        print('\nThe quadratic has two real roots.')
        print(solutions[0])
        print(solutions[1])

def print_complex_roots(solutions):
    """Prints the complex roots of the quadratic."""
    print('\nThe quadratic has complex roots.')

    if solutions[0].real == 0:
        print(f'{solutions[0].imag}j')
        print(f'{solutions[1].imag}j')
    else:
        print(solutions[0])
        print(solutions[1])

def calc_discriminant(a, b, c):
    """Calculates the discriminant of the quadratic."""
    discriminant = b**2 - 4 * a * c
    return discriminant

def sign(number):
    """Determines the sign of a number.""" 
    if number == 0:
        return 0
    elif number < 0:
        return -1
    elif number > 0:
        return 1

if __name__ == '__main__':

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
    
    discriminant = calc_discriminant(a, b, c)

    if discriminant >= 0:
        solutions = real_roots(a, b, c)
        print_real_roots(solutions)
    else:
        solutions = complex_roots(a, b, c)
        print_complex_roots(solutions)
