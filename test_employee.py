import unittest
from employee import Employee
from unittest.mock import patch

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('\nsetUpClass')
    
    @classmethod
    def tearDownClass(cls):
        print('tearDownClass\n')

    def setUp(self):
        print('\nsetUp')
        self.emp1 = Employee('John', 'Molley', 50000)
        self.emp2 = Employee('Pamela', 'Tarte', 40000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp1.email, 'John.Molley@gmail.com')
        self.assertEqual(self.emp2.email, 'Pamela.Tarte@gmail.com')

        self.emp1.fname = 'Pamela'
        self.emp2.fname = 'John'

        self.assertEqual(self.emp1.email, 'Pamela.Molley@gmail.com')
        self.assertEqual(self.emp2.email, 'John.Tarte@gmail.com')

    def test_full_name(self):
        print('test_full_name')
        self.assertEqual(self.emp1.fullname, 'John Molley')
        self.assertEqual(self.emp2.fullname, 'Pamela Tarte')

        self.emp1.fname = 'Pamela'
        self.emp2.fname = 'John'

        self.assertEqual(self.emp1.fullname, 'Pamela Molley')
        self.assertEqual(self.emp2.fullname, 'John Tarte')

    def test_pay_raise(self):
        print('test_pay_raise')
        self.emp1.apply_raise()
        self.emp2.apply_raise()

        self.assertEqual(self.emp1.pay, 52500)
        self.assertEqual(self.emp2.pay, 42000)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp1.monthly_schedule('May')
            mocked_get.assert_called_with('https://company.com/Molley/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp1.monthly_schedule('June')
            mocked_get.assert_called_with('https://company.com/Molley/June')
            self.assertEqual(schedule, 'Bad Response!')

if __name__ == '__main__':
    unittest.main()




