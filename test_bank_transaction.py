import unittest
from bank_transaction import Bank_Account 

class Test_Bank_Account(unittest.TestCase):

    def setUp(self):
        self.acc1 = Bank_Account('Dave Eddison', 5000)
        self.acc2 = Bank_Account('Daryl Mitchell', 6000)

    def tearDown(self):
        pass

    def test_deposit(self):
        self.acc1.deposit(2000)
        self.acc2.deposit(4000)

        self.assertEqual(self.acc1.balance, 7000)
        self.assertEqual(self.acc2.balance, 10000)

    def test_withdraw(self):
        self.acc1.withdraw(1000)
        self.acc2.withdraw(2000)

        self.assertEqual(self.acc1.balance, 4000)
        self.assertEqual(self.acc2.balance, 4000)

        self.acc1.withdraw(1000)
        self.acc2.withdraw(2000)

        self.assertEqual(self.acc1.balance, 3000)
        self.assertEqual(self.acc2.balance, 2000)

        self.acc1.withdraw(1000)
        
        self.assertEqual(self.acc1.balance, 2000)

        #Should raise ValueError when withdrawing 3000 when balance is 2000
        with self.assertRaises(ValueError):
            self.acc2.withdraw(3000)


if __name__ == '__main__':
    unittest.main()


    

