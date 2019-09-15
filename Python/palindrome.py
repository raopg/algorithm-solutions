import math

def palindrome_fastest(s):
    if(s == None or s == ''):
        return False
    mid = math.floor(len(s) / 2)
    for i in range(mid):
        if s[i] != s[len(s)-i-1] :
            return False
    return True


if __name__ == '__main__':
    while(True):
        s = input('Enter a string to check for palindrome: ')
        print(palindrome_fastest(s))



