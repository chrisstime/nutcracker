import unittest
import re
import app.password_generator as password_generator


class TestPasswordGenerator(unittest.TestCase):

    def test__format_password(self):
        """Test password is formatted as expected"""
        generated_password_array = ['2', '$', 's', 'A', '^', 'q']
        self.assertEqual(password_generator._format_password(generated_password_array), '2$sA^q')

    def test__shuffle_characters(self):
        """Test character shuffling method"""
        self.assertFalse(password_generator._shuffle_characters(symbols=False, letters=False, numbers=False))

    def test_generate_password(self):
        """Test password generator options"""
        # minimum pwd length we allow from the GUI is 8 so we don't have to worry about setting it to 0
        password_length = 8
        self.assertFalse(
            password_generator.generate_password(
                symbols=False,
                letters=False,
                numbers=False,
                password_length=password_length
            )
        )

        # with symbols only
        # its hard to regex match crazy symbols so the best way is to check that none of them are digits
        # or letters and the string length is correct
        generated_pwd = password_generator.generate_password(
                symbols=True,
                letters=False,
                numbers=False,
                password_length=password_length
            )
        self.assertFalse(generated_pwd.isalpha())
        self.assertFalse(generated_pwd.isdigit())
        self.assertTrue(len(generated_pwd), 8)

        # with letters only
        generated_pwd = password_generator.generate_password(
            symbols=False,
            letters=True,
            numbers=False,
            password_length=password_length
        )
        self.assertTrue(generated_pwd.isalpha())
        self.assertTrue(len(generated_pwd), 8)

        # with digits only
        generated_pwd = password_generator.generate_password(
            symbols=False,
            letters=False,
            numbers=True,
            password_length=password_length
        )
        self.assertTrue(generated_pwd.isdigit())
        self.assertTrue(len(generated_pwd), 8)

        # with all digits, letters and symbols
        generated_pwd = password_generator.generate_password(
            symbols=True,
            letters=False,
            numbers=False,
            password_length=password_length
        )
        self.assertTrue(re.search("\W", generated_pwd))
        self.assertTrue(len(generated_pwd), 8)



