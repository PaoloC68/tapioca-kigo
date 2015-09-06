# coding: utf-8

import unittest

from tapioca_kigo import Kigo


class TestTapiocaKigo(unittest.TestCase):

    def setUp(self):
        self.wrapper = Kigo()


if __name__ == '__main__':
    unittest.main()
