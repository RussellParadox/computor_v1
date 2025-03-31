import unittest
import subprocess

class TestsFromSubject(unittest.TestCase):
    def test_1(self):
        '''Test 1'''
        process = subprocess.run(["python", "computor.py", "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"], capture_output=True)
        self.assertEqual(process.stdout.decode("utf-8"), "Reduced form: 4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0\nPolynomial degree: 2\nDiscriminant is strictly positive, the two solutions are:\n0.905239\n-0.475131\n\n")

    def test_2(self):
        '''Test 2'''
        process = subprocess.run(["python", "computor.py", "5 * X^0 + 4 * X^1 = 4 * X^0"], capture_output=True)
        self.assertEqual(process.stdout.decode("utf-8"), "Reduced form: 1 * X^0 + 4 * X^1 = 0\nPolynomial degree: 1\nThe solution is:\n-0.25\n\n")

    def test_3(self):
        '''Test 3'''
        process = subprocess.run(["python", "computor.py", "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"], capture_output=True)
        self.assertEqual(process.stdout.decode("utf-8"), "Reduced form: 5 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 0\nPolynomial degree: 3\nThe polynomial degree is strictly greater than 2, I can't solve.\n\n")

    def test_4(self):
        '''Test 4'''
        process = subprocess.run(["python", "computor.py", "6 * X^0 = 6 * X^0"], capture_output=True)
        self.assertEqual(process.stdout.decode("utf-8"), "Reduced form: 0 * X^0 = 0\nAny real number is a solution.\n\n")

    def test_5(self):
        '''Test 5'''
        process = subprocess.run(["python", "computor.py", "10 * X^0 = 15 * X^0"], capture_output=True)
        self.assertEqual(process.stdout.decode("utf-8"), "Reduced form: -5 * X^0 = 0\nNo solution.\n\n")

    def test_6(self):
        '''Test 6'''
        process = subprocess.run(["python", "computor.py", "1 * X^0 + 2 * X^1 + 5 * X^2 = 0"], capture_output=True)
        self.assertEqual(process.stdout.decode("utf-8"), "Reduced form: 1 * X^0 + 2 * X^1 + 5 * X^2 = 0\nPolynomial degree: 2\nDiscriminant is strictly negative, the two complex solutions are:\n-1/5 + 2i/5\n-1/5 - 2i/5\n\n")

if __name__ == "__main__":
    unittest.main()
