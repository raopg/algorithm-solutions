## Given a string containing opening and closing parantheses, determine whether
## the order of parantheses is valid. A valid sequence is defined as one where - 
## 1. Open brackets are closed by the same type of bracket
## 2. Open brackets must be closed in the right order.

def valid_parantheses(s):
    ## Declare a brackets dict.
    brackets = {
        "]":"[",
        ")":"(",
        "}": "{"
    }

    stack = []

    for char in s:
        if char in brackets:
            top = stack.pop() if stack else "#"

            if top != brackets[char]:
                return False
        else:
            stack.append(char)
    
    return not stack