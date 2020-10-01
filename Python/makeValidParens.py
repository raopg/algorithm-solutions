def make_valid(S):
    '''
    Given a string containing parantheses,
    your task is to remove invalid parantheses and return
    the resulting array.
    
    Solution:
    Count -> number of unbalanced parantheses
    Take each character:
        If it is a closing parantheses:
            Add it on if, parantheses are unbalanced
        Else if its an opening parantheses and count > unbalanced:
            Add it on
        else:
            add it on
            
    a)(b)cd((
    a(b)c(def))
    
    First pass -> number of unbalanced.
    
    '''
    stack = []
    
    opening, closing = S.count('('), S.count(')') 
    
    count = 0
    
    for char in S:
        if char == ')':
            closing -= 1
            if count > 0:
                stack.append(char)
                count -= 1
        elif char == '(':
            opening -= 1 
            if closing != 0:
                stack.append(char)
                count += 1
        else:
            stack.append(char)
    
    
    return ''.join(stack)

print(make_valid("lee(t(c)o)de)"))
print(make_valid("a)b(c)d"))
print(make_valid("))(( # ))a("))
print(make_valid("(a(b(c)d)"))

        
            
     
    
    