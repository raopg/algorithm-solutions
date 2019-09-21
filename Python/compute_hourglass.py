# a b c
#   d
# e f g
## Is a definition of an hourglass. Given a 6 X 6 array, compute the value of the max hourglass.

def compute_hourglass_sum(i,j, arr):
    return arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j+2] + arr[i+2][j] + arr[i+2][j+1]
def hourglassSum(arr):
    result = []
    for i in range(6):
        for j in range(6):
            if i + 2 < 6 and j + 2 < 6:
                result.append(compute_hourglass_sum(i,j,arr))
    return max(result)

def generate_hourglass(encoding, arr):
    k,l = list(encoding)
    ret = []
    for i in range(int(k), int(k) + 2):
        r = []
        for j in range(int(l), int(l) + 2):
            r.append(arr[i],[j])
        ret.append(r)
    return ret
        

def biggest_hourglass(arr):
    hourglasses = dict()
    for i in range(6):
        for j in range(6):
            if i + 2 < 6 and j + 2 < 6:
                hourglasses[str(i) + str(j)] = compute_hourglass_sum(i,j,arr)
    
    ret = sorted(hourglasses, key= lambda x: x[1], reverse=True)[0][0] ## The key of the largest

    return generate_hourglass(ret, arr)
