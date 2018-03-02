import unittest

from find_max_subarray import find_max_subarray


class TestFindMaxSubarray(unittest.TestCase):

    def test_find_max_subbarray(self):
        a = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
        b, c, d = find_max_subarray(a, 0, len(a) - 1)
        print('aaaaaaaaaa')
        print("first_idx: {},  last_index: {},   sum: {}\n".format(b, c, d))


if __name__ == '__main__':
    unittest.main()
