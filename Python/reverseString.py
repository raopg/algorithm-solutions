def reverse_str(str):
    '''This implementation of reverse string function can be actually O(n^2), because strings are immutable in Python'''
    reversed = ''
    for character in str:
        reversed = character + reversed 
    return reversed   

def reverse_str2(str):
    '''Recursive implementation with string slicing'''
    if len(str) == 1:
        return str
    else:
        return reverse_str2(str[1:])+ str[0]

def reverse_str3(str):
    '''String slicing but uses third option'''

    return str[::-1]

if __name__ == "__main__":
    str = input('Enter a string to reverse: ')

    print('Reversed string using loop:',reverse_str(str))

    print('Reversed string using recursion:',reverse_str2(str))

    print('Reversed string using slicing 3rd option:',reverse_str3(str))
