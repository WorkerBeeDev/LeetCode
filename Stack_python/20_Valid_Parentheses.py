class Solution:
    def isValid(self, s: str) -> bool:

        d = {'(': ')', '{': '}', '[': ']'}

        stack = []

        for i in s:
            if i in d:
                stack.append(i)
            else:
                # edge case
                if len(stack) == 0:
                    return False
                # the close parenthese should match
                if d[stack.pop()] != i:
                    return False
        # edge case: if everything match but there still something remains 
        return not stack
