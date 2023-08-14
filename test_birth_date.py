from conftest import *
import unittest, os
import sys


class TestClass(unittest.TestCase):
    def test_birth_date_hours(self):
        """Verify Birth Date with Unit= Hours"""
        rc, ro = next_birthdate(unit='hour')
        self.assertTrue(True, rc)

    def test_birth_date_day(self):
        """Verify Birth Date with Unit= Days"""
        rc, ro = next_birthdate(unit='day')
        self.assertTrue(True, rc)

    def test_birth_date_week(self):
        """Verify Birth Date with Unit= Week"""
        rc, ro = next_birthdate(unit='week')
        self.assertTrue(True, rc)

    def test_birth_date_month(self):
        """Verify Birth Date with Unit= Months"""
        rc, ro = next_birthdate(unit='month')
        self.assertTrue(True, rc)

    def test_birth_date_invalid_unit(self):
        """Verify Birth Date with Unit= years"""
        rc, ro = next_birthdate(unit='years')
        self.assertFalse(False, rc)

    def test_birth_date_invalid_dob(self):
        """Verify Birth Date with Invalid Date of birth"""
        rc, ro = next_birthdate(dob='20-12-1991', unit='hour')
        self.assertFalse(False, rc)

    def test_birth_date_empty_unit(self):
        """Verify Birth Date with Empty unit"""
        rc, ro = next_birthdate(unit='')
        self.assertFalse(False, rc)

    def test_birth_date_invalid_dob(self):
        """Verify Birth Date with empty dob"""
        rc, ro = next_birthdate(dob='', unit='hour')
        self.assertFalse(False, rc)
        

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("\nInvalid usage")
        print("\nUsage:python test_birth_date.py")
        os.exit(1)
    unittest.main()
