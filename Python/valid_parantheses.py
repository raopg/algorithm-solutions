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
        if char in brackets: # Since the keys of the brackets dict are closing brackets, this will check if the character is a closing bracket.
            top = stack.pop() if stack else '#' # Pop the stack.

            if brackets[char] != top: #If the popped variable is not the opening bracket for the current closing bracket, it means that one or more brackets aren't being closed.
                return False # Since they arent being closed, its obviously an invalid parantheses string.
        else:
            stack.append(char)
    return not stack


if __name__ == '__main__':
    string = input('Enter a string containing parantheses: ')
    print(is_valid(string))