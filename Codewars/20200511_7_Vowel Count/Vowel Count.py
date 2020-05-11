"""
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, and u as vowels for this Kata.

The input string will only consist of lower case letters and/or spaces.
"""

import unittest

def getCount(inputStr):
    
    return len([ element for element in inputStr.lower() if element in "aeiou" ])


class Test(unittest.TestCase):
    
    def test(self):
        
        self.assertEqual(getCount("abracadabra"), 5)

if __name__ == "__main__":
    
    unittest.main()