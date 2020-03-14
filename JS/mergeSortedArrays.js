const solution = (arr1, arr2) => {
    n1 = arr1.length
    n2 = arr2.length

    ret = []
    i = 0
    j = 0
    while(i <n1 || j <n2){
        if(i == n1){
            ret.push(arr2[j])
            j++
            continue
        }
        if(j == n2){
            ret.push(arr1[i])
            i++
            continue
        }
        if(arr1[i] <= arr2[j]){
            ret.push(arr1[i])
            i++
        }
        else{
            ret.push(arr2[j])
            j++
        }
    }

    return ret
}

console.log(solution([1,3,4], [2,5,7]))
