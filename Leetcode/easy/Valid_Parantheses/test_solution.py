import unittest
from sol import Solution

class TestValidParentheses(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_valid_parentheses(self):
        # Test valid cases
        self.assertTrue(self.solution.isValid("()"))
        self.assertTrue(self.solution.isValid("()[]{}"))
        self.assertTrue(self.solution.isValid("({[]})"))
        self.assertTrue(self.solution.isValid(""))
        
        # Test invalid cases
        self.assertFalse(self.solution.isValid("(]"))
        self.assertFalse(self.solution.isValid("([)]"))
        self.assertFalse(self.solution.isValid("(("))
        self.assertFalse(self.solution.isValid("))"))
        self.assertFalse(self.solution.isValid("{"))
        self.assertFalse(self.solution.isValid("}"))

# Test with assert statements for validation
def test_with_assert():
    solution = Solution()
    
    # Valid parentheses test cases
    assert solution.isValid("()") == True, "Simple parentheses should be valid"
    assert solution.isValid("()[]{}") == True, "Multiple bracket types should be valid"
    assert solution.isValid("({[]})") == True, "Nested brackets should be valid"
    assert solution.isValid("") == True, "Empty string should be valid"
    assert solution.isValid("(({}))") == True, "Nested parentheses should be valid"
    assert solution.isValid("[{()}]") == True, "Complex nesting should be valid"
    
    # Invalid parentheses test cases
    assert solution.isValid("(]") == False, "Mismatched brackets should be invalid"
    assert solution.isValid("([)]") == False, "Incorrectly nested brackets should be invalid"
    assert solution.isValid("((") == False, "Unclosed parentheses should be invalid"
    assert solution.isValid("))") == False, "Extra closing parentheses should be invalid"
    assert solution.isValid("{") == False, "Single opening brace should be invalid"
    assert solution.isValid("}") == False, "Single closing brace should be invalid"
    assert solution.isValid("(()") == False, "Unmatched opening parentheses should be invalid"
    assert solution.isValid("())") == False, "Extra closing parentheses should be invalid"
    assert solution.isValid("(((") == False, "Multiple unmatched opening should be invalid"
    assert solution.isValid(")))") == False, "Multiple unmatched closing should be invalid"
    
    print("All assert tests passed! ✅")

if __name__ == "__main__":
    # Run assert tests first
    test_with_assert()
    
    # Run unittest tests
    unittest.main()