"""
Complete the method/function so that it converts dash/underscore delimited words 
into camel casing. The first word within the output should be capitalized only 
if the original word was capitalized (known as Upper Camel Case, also often 
                                      referred to as Pascal case).

Examples
to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"
"""

import unittest


def find_dash_or_underscore(input_text):
    
    for check_element in ["-", "_"]:
        if check_element in input_text:
            return input_text.find(check_element)
    
    return None


def change_first_letter_to_upper_case(input_text):
    
    return input_text[0].upper() + input_text[1:]


def to_camel_case(text):
    
    target_index = find_dash_or_underscore(text)
    while target_index is not None:
        text = text[:target_index] + \
               change_first_letter_to_upper_case(text[target_index + 1:])
        target_index = find_dash_or_underscore(text)
    
    return text
        

class Test(unittest.TestCase):
    
    def test(self):
        
        self.assertEqual(to_camel_case(''), '', "An empty string was provided but not returned")
        self.assertEqual(to_camel_case("the_stealth_warrior"), "theStealthWarrior", "to_camel_case('the_stealth_warrior') did not return correct value")
        self.assertEqual(to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior", "to_camel_case('The-Stealth-Warrior') did not return correct value")
        self.assertEqual(to_camel_case("A-B-C"), "ABC", "to_camel_case('A-B-C') did not return correct value")

if __name__ == "__main__":
    
    unittest.main()