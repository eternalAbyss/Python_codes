class Solution:
    def isValid(self, s: str) -> bool:
        is_closed = False
        if len(s)%2!=0:
            pass
        else :
            brackets = {
                ')' : '(',
                '}' : '{',
                ']' : '['
            }
            brackets_order = list()
            try:
                for bracket in list(s):
                    if bracket in brackets.keys() and brackets[bracket] == brackets_order[-1]:
                        brackets_order.pop()
                    else:
                        brackets_order.append(bracket)
                if len(brackets_order) == 0:
                    is_closed = True
            except:
                is_closed = False
        return is_closed