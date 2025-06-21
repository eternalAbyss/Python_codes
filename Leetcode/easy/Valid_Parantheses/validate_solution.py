#!/usr/bin/env python3
"""
Comprehensive validation script for the Valid Parentheses solution.
This script uses assert statements to validate the correctness of the solution.
"""

from sol import Solution

def main():
    """Main validation function using assert statements."""
    print("🔍 Starting comprehensive validation of Valid Parentheses solution...")
    
    # Initialize solution
    solution = Solution()
    
    # Test Case 1: Basic valid cases
    print("\n✅ Testing basic valid cases...")
    assert solution.isValid("()") == True, "Test failed: '()' should be valid"
    assert solution.isValid("[]") == True, "Test failed: '[]' should be valid"
    assert solution.isValid("{}") == True, "Test failed: '{}' should be valid"
    print("   ✓ All basic valid cases passed!")
    
    # Test Case 2: Empty string
    print("\n✅ Testing empty string...")
    assert solution.isValid("") == True, "Test failed: Empty string should be valid"
    print("   ✓ Empty string test passed!")
    
    # Test Case 3: Multiple bracket types
    print("\n✅ Testing multiple bracket types...")
    assert solution.isValid("()[]{}") == True, "Test failed: '()[]{}' should be valid"
    assert solution.isValid("({[]})") == True, "Test failed: '({[]})' should be valid"
    assert solution.isValid("[{()}]") == True, "Test failed: '[{()}]' should be valid"
    print("   ✓ All multiple bracket type tests passed!")
    
    # Test Case 4: Nested brackets
    print("\n✅ Testing nested brackets...")
    assert solution.isValid("((()))") == True, "Test failed: '((()))' should be valid"
    assert solution.isValid("[[[]]]") == True, "Test failed: '[[[]]]' should be valid"
    assert solution.isValid("{{{}}}") == True, "Test failed: '{{{}}}' should be valid"
    assert solution.isValid("(({}))") == True, "Test failed: '(({}))' should be valid"
    print("   ✓ All nested bracket tests passed!")
    
    # Test Case 5: Basic invalid cases
    print("\n❌ Testing basic invalid cases...")
    assert solution.isValid("(]") == False, "Test failed: '(]' should be invalid"
    assert solution.isValid("([)]") == False, "Test failed: '([)]' should be invalid"
    assert solution.isValid("((") == False, "Test failed: '((' should be invalid"
    assert solution.isValid("))") == False, "Test failed: '))' should be invalid"
    print("   ✓ All basic invalid case tests passed!")
    
    # Test Case 6: Single brackets
    print("\n❌ Testing single brackets...")
    assert solution.isValid("(") == False, "Test failed: '(' should be invalid"
    assert solution.isValid(")") == False, "Test failed: ')' should be invalid"
    assert solution.isValid("[") == False, "Test failed: '[' should be invalid"
    assert solution.isValid("]") == False, "Test failed: ']' should be invalid"
    assert solution.isValid("{") == False, "Test failed: '{' should be invalid"
    assert solution.isValid("}") == False, "Test failed: '}' should be invalid"
    print("   ✓ All single bracket tests passed!")
    
    # Test Case 7: Unmatched brackets
    print("\n❌ Testing unmatched brackets...")
    assert solution.isValid("(()") == False, "Test failed: '(()' should be invalid"
    assert solution.isValid("())") == False, "Test failed: '())' should be invalid"
    assert solution.isValid("(((") == False, "Test failed: '(((' should be invalid"
    assert solution.isValid(")))") == False, "Test failed: ')))' should be invalid"
    assert solution.isValid("([{}") == False, "Test failed: '([{}' should be invalid"
    assert solution.isValid("([}])") == False, "Test failed: '([}])' should be invalid"
    print("   ✓ All unmatched bracket tests passed!")
    
    # Test Case 8: Complex valid cases
    print("\n✅ Testing complex valid cases...")
    assert solution.isValid("()()()") == True, "Test failed: '()()()' should be valid"
    assert solution.isValid("[]{}()") == True, "Test failed: '[]{}()' should be valid"
    assert solution.isValid("({[(){}]})") == True, "Test failed: '({[(){}]})' should be valid"
    assert solution.isValid("(((())))") == True, "Test failed: '(((())))' should be valid"
    print("   ✓ All complex valid case tests passed!")
    
    # Test Case 9: Complex invalid cases
    print("\n❌ Testing complex invalid cases...")
    assert solution.isValid("([)]") == False, "Test failed: '([)]' should be invalid"
    assert solution.isValid("(({})") == False, "Test failed: '(({})' should be invalid"
    assert solution.isValid("(({})))") == False, "Test failed: '(({})))' should be invalid"
    assert solution.isValid("({[}])") == False, "Test failed: '({[}])' should be invalid"
    print("   ✓ All complex invalid case tests passed!")
    
    # Test Case 10: Edge cases from problem examples
    print("\n✅ Testing problem statement examples...")
    assert solution.isValid("()") == True, "Test failed: Example 1 - '()' should be valid"
    assert solution.isValid("()[]{}") == True, "Test failed: Example 2 - '()[]{}' should be valid"
    assert solution.isValid("(]") == False, "Test failed: Example 3 - '(]' should be invalid"
    print("   ✓ All problem statement examples passed!")
    
    print("\n🎉 ALL VALIDATION TESTS PASSED! 🎉")
    print("✅ The Valid Parentheses solution is working correctly!")
    print("✅ Solution handles all edge cases properly!")
    print("✅ Time complexity: O(n) where n is the length of the string")
    print("✅ Space complexity: O(n) in the worst case for the stack")

if __name__ == "__main__":
    main()
