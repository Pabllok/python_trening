import unittest


def addition(a, b):
    return a+b


class AdditionTestCase(unittest.TestCase):

    def test_additionTwoInt(self):
        result = addition(3, 2)
        assert result == 5

    def notatest(self):
        pass

class MySecondTestCase(unittest.TestCase):
    def test_two(self):
        pass

    def test_two_part2(self):
        pass


if __name__ == '__main__':
    unittest.main()