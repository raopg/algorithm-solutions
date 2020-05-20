# Question: Given a string, design an algorithm to find out if it 
# is a permutation of a palindrome

## Idea: What makes a palindrome a palindrome? We should be able to
## write it backwards and forwards. Hence, almost all chars must appear
## an even number of times. Only one character can appear an odd 
# number of times.

## Algo:
## Find the frequency dict of the word. Going through all of them, if
## more than one value (in the dict) is not divisble by 2, return False
## Return True if we make a full pass of the dict.

from collections import Counter

def permutation_of_palindrome(string):
    freq = Counter(string)
    found_odd = False
    for char, count in freq.items():
        if count % 2 == 0:
            continue
        if found_odd:
            return False
        found_odd = True
    return True

# print(permutation_of_palindrome('abab'))
# print(permutation_of_palindrome('mmo'))
# print(permutation_of_palindrome('dada'))
# print(permutation_of_palindrome('bro'))
# print(permutation_of_palindrome('heyo'))
