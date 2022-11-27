import unittest

from impl import calc_greedy_schedule, calc_bruteforce_schedule
from math import ceil
from random import random
from time import time


class TestStringMethods(unittest.TestCase):

    def test_simple_2(self):
        self.assertEqual(calc_bruteforce_schedule([1, 2, 3, 4, 5], 2),
                         calc_greedy_schedule([1, 2, 3, 4, 5], 2))

    def test_simple_3(self):
        self.assertEqual(calc_bruteforce_schedule([1, 2, 3, 4, 5], 3),
                         calc_greedy_schedule([1, 2, 3, 4, 5], 3))

    def test_medium(self):
        tasks = [int(100 * random()) + 1 for i in range(10)]
        num_of_processors = 3
        self.assertGreaterEqual(ceil((4 / 3) * calc_bruteforce_schedule(tasks, num_of_processors)),
                                calc_greedy_schedule(tasks, num_of_processors))

    def test_stress(self):
        tasks = [int(100 * random()) + 1 for i in range(1000000)]
        num_of_processors = 15
        start_time = time()
        calc_greedy_schedule(tasks, num_of_processors)
        end_time = time()
        self.assertLessEqual(end_time - start_time, 1)


if __name__ == '__main__':
    unittest.main()
