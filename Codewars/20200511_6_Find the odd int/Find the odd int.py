"""
Given an array, find the integer that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
"""

import unittest

# def find_it(seq):
    
#     count_dict = {}
#     for element in seq:
#         if count_dict.get(element, None) is None:
#             count_dict[element] = 1
#         else:
#             count_dict[element] += 1
    
#     for num, count in count_dict.items():
#         if count % 2 == 1:
#             return num


def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i


class Test(unittest.TestCase):
    
    def test(self):
        
        self.assertEqual(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
        self.assertEqual(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]), -1)
        self.assertEqual(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]), 5)
        self.assertEqual(find_it([10]), 10)
        self.assertEqual(find_it([1,1,1,1,1,1,10,1,1,1,1]), 10)
        self.assertEqual(find_it([5,4,3,2,1,5,4,3,2,10,10]), 1)

if __name__ == "__main__":
    
    unittest.main()