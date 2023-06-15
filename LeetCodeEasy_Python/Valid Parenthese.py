class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # create a stack for storing opening parenthesis
        stack = []
        # make a dictionaries with open and closing parenthesis
        closing = dict(('()','{}','[]'))
        
        # Traverse each character in string
        for idx in s:
            # if open parenthesis then store in stack
            if idx in '({[':
                stack.append(idx)
            # check stack is empty or stack top same opening bracket is present or not
            elif len(stack) == 0 or idx != closing[stack.pop()]:
                return False
        # finaly if stack is empty then return True
        return len(stack) == 0
    
        