// The in operator in JavaScript is O(1). However, you use Objects here instead of Set or Map, simply because of faster implementation.

const containsDuplicate = (nums) =>{
    seen = Object(null)

    for(let n of nums){
        if(n in seen){
            return true
        }
        seen[n] = true
    }
    return false
}

console.log(containsDuplicate([1,2,3,4,1]))
console.log(containsDuplicate([2,3,4,6,5]))