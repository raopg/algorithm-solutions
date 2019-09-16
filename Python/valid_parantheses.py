''' The Problem: Given a string of parantheses, find out if it is a valid expression.
    Ex: ()(){} -> valid
        ()[ -> invalid
        ([]) -> valid
        ([)] -> invalid

'''

def is_valid(string: str):
    ''' We will use a stack to keep track of the parantheses seen so far'''
    brackets = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }

    stack = []

    for char in string:
        if char in brackets:
            top = stack.pop() if stack else '#'

            if brackets[char] != top:
                return False
        else:
            stack.append(char)
    return not stack


if __name__ == '__main__':
    string = input('Enter a string containing parantheses: ')
    print(is_valid(string))