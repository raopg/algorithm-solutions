# Question: Given a string, write a method to replace 
# all the spaces with a '%20'

def URLify(url_str):
    url_str = url_str.strip(' ')
    ## Strings are immutable in Python, so we have to convert to list
    ## Since, we're spiltting, might as well split by spaces.
    ## We can again join using '%20' as a delim (one line)
    return '%20'.join(url_str.split(' '))

print(URLify('Mr Prateek Rao'))
print(URLify('     my name    is something else'))

## Complexity analysis: O(n) time and O(n) space. Unfortunately, we
# cannot do better in Python, since strings are immutable
## In Java or C++, we can modify string in-place, with a simple O(n) 
# time solution.
###
##
# public char[] URLify(char[] str){
#     for(int i = 0; i < str.length; i++){
#         if(str[i] == ' '){
#             str[i] = '%20';
#         }
#     }
#     return str;
# }
