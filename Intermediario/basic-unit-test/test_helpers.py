# Author: Jonatas Freitas (https://github.com/jonatasfreitasv)
# Código do artigo
# https://jonatasfreiitas.wordpress.com/2015/02/02/python-unit-test-teste-unitario/

import unittest

from helpers import Helpers


class Helpers_Test(unittest.TestCase):

    def test_sum(self):
        result = Helpers.sum(10, 10)
        self.assertEqual(result, 20)

if __name__ == '__main__':
    unittest.main()
