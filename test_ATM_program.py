from unittest import mock
from unittest import TestCase, main
from Nanodegree.Session_9_Testing.ATM_program import verify_pin, run_atm

class TestVerifyPIN(TestCase):
    def test_correct_PIN(self):
        expected = True
        result  = verify_pin(pin='1234')
        self.assertEqual(expected, result)

    def test_incorrect_PIN(self):
        expected = True
        result = verify_pin(pin = '3946')
        self.assertNotEqual(expected, result)


class test_Run_ATM(TestCase):
    def test_High_Withdrawel_with_correct_PIN(self):
        if verify_pin(True):
            expected = ValueError
            result = run_atm(150)
            self.assertNotEqual(expected , result)
    def test_low_withdrawal_with_correct_PIN(self):
        if verify_pin(True):
            expected = 25
            result = run_atm(75)
            self.assertEqual(expected,result)
    def test_incorrect_PIN(self):
        if verify_pin(False):
            expected = 100
            result = run_atm(100)
            self.assertEqual(expected,result)



if __name__ == '__main__':
    main()
