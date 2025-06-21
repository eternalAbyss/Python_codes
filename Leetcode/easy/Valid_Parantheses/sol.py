class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
        self.size += 1
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top # type: ignore
            self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        self.size -= 1
        popped_value = self.top.value
        self.top = self.top.next
        return popped_value

    def peek(self):
        if self.top is None:
            return None
        return self.top.value

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = Stack()
        brackets = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in brackets:  # It's a closing bracket
                if stack.peek() == brackets[char]:
                    stack.pop()
                else:
                    return False  # Mismatched or no opening bracket
            else:  # It's an opening bracket
                stack.push(char)

        # If the stack is empty, all brackets were matched
        # If not, there are unmatched brackets
        result = stack.size == 0
        return result

# Example usage:
if __name__ == "__main__":
    s = "({[]})"
    print(Solution().isValid(s))  # Output: True

    s = "({[})"
    print(Solution().isValid(s))  # Output: False