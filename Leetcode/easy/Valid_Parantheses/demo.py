#!/usr/bin/env python3
"""
Demo script for the Valid Parentheses solution.
Shows the solution in action with various test cases.
"""

from sol import Solution

def demo():
    """Demonstrate the Valid Parentheses solution."""
    print("🔥 Valid Parentheses Solution Demo 🔥")
    print("=" * 40)
    
    solution = Solution()
    
    # Test cases with expected results
    test_cases = [
        # Valid cases
        ("()", True, "Simple parentheses"),
        ("[]", True, "Simple square brackets"),
        ("{}", True, "Simple curly braces"),
        ("", True, "Empty string"),
        ("()[]{}", True, "Multiple bracket types"),
        ("({[]})", True, "Nested brackets"),
        ("((()))", True, "Multiple nested parentheses"),
        ("({[(){}]})", True, "Complex nested structure"),
        
        # Invalid cases
        ("(]", False, "Mismatched brackets"),
        ("([)]", False, "Incorrectly nested"),
        ("((", False, "Unclosed parentheses"),
        ("))", False, "Extra closing parentheses"),
        ("(", False, "Single opening parenthesis"),
        (")", False, "Single closing parenthesis"),
        ("(())", True, "Nested parentheses"),
        ("())", False, "Extra closing parenthesis"),
        ("({[}])", False, "Wrong nesting order"),
    ]
    
    print(f"{'Input':<15} | {'Expected':<8} | {'Result':<8} | {'Status':<6} | Description")
    print("-" * 80)
    
    all_passed = True
    for test_input, expected, description in test_cases:
        result = solution.isValid(test_input)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        if result != expected:
            all_passed = False
        
        # Format the input for display
        display_input = f'"{test_input}"' if test_input else '""'
        
        print(f"{display_input:<15} | {str(expected):<8} | {str(result):<8} | {status:<6} | {description}")
    
    print("-" * 80)
    if all_passed:
        print("🎉 All test cases passed! The solution is working correctly! 🎉")
    else:
        print("❌ Some test cases failed. Please check the implementation.")
    
    print(f"\n📊 Summary:")
    print(f"   • Total test cases: {len(test_cases)}")
    print(f"   • Valid cases: {sum(1 for _, expected, _ in test_cases if expected)}")
    print(f"   • Invalid cases: {sum(1 for _, expected, _ in test_cases if not expected)}")
    print(f"   • All tests passed: {'Yes' if all_passed else 'No'}")

if __name__ == "__main__":
    demo()
