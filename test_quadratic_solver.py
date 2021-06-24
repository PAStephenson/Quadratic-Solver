import unittest
from quadratic_solver import real_roots, complex_roots

class QuadraticSolverTestCase(unittest.TestCase):
    """Tests for 'quadratic_solver.py'."""

    def test_two_real_solutions(self):
        """Test with 3 non zero coefficient and 2 real solutions."""
        solutions = real_roots(1, 1, -6)
        self.assertEqual(solutions, (-3, 2))


    def test_one_real_solution(self):
        """Test with 3 non zero coefficient and 1 real solution."""
        solution = real_roots(1, -6, 9)
        self.assertEqual(solution, (3, 3))


    def test_complex_solutions(self):
        """Test with 3 non zero coefficient and complex solutions."""
        solutions = complex_roots(1, 6, 34)
        self.assertEqual(solutions, ((-3 + 5j), (-3 -5j)))


if __name__ == '__main__':
    unittest.main()
