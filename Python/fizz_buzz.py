def solution(value):
    '''We do not use strings like in the JS solution because in Python, strings are immutable'''
    for i in range(1,value+1): 
        if i % 15 == 0:
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)


if __name__ == '__main__':
    val = int(input('Enter a value to fizzbuzz till: '))
    solution(val)
        