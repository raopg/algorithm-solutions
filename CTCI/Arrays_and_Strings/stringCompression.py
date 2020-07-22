## Problem: Implement a method to perform basic string compression using counts of
## repeated characters. For example - aabcccccaaa will become a2b1c5a3
## If the compressed string is not smaller than the original string, then return the original string.

## Solution:
## Iterate through the list. Have a counter within the loop that counts the number of consecutive recurring characters
## When we encounter a character that is not the previous character, then we simply add the previous character
## and current count as a string, into a list.
## We can then set the prev character to this new character, and set the count = 1
## Additionally, if len(list of compressed strings) * 2 >= len(original string) => return original string.

def stringCompression(input_str):

    if input_str == '':
        return ''
    
    if len(input_str) == 1:
        return input_str
    
    counter = 1
    compressedStrings = []
    prev = input_str[0]

    for i in range(1, len(input_str)):
        if input_str[i] == prev:
            counter += 1
            continue
        else:
            compressedStrings.append(prev+str(counter))
            if len(compressedStrings) * 2 >= len(input_str):
                return input_str
            prev = input_str[i]
            counter = 1
    compressedStrings.append(prev + str(counter))
    if len(compressedStrings) * 2 >= len(input_str):
        return input_str
    return ''.join(compressedStrings)


def stringCompressionNext(input_str):
    if input_str == '':
        return ''
    
    if len(input_str) == 1:
        return input_str

    counter = 0
    compressedStrings = []

    for i in range(len(input_str)):
        counter += 1
        if i + 1 >= len(input_str) or input_str[i] != input_str[i+1]:
            compressedStrings.append(input_str[i] + str(counter))
            counter = 0
    return (''.join(compressedStrings)) if len(compressedStrings) * 2 < len(input_str) else input_str

print(stringCompressionNext('aabcccccaaa'))
print(stringCompression('aaaabbbc'))
    

