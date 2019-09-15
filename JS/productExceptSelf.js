/* The problem: Given an array of N integers(N>1), return an array containing the products of the array except the number itself.
// Time complexity requirements: O(N)
// You CANNOT use DIVISION. Easiest solution is to reduce the list to a product and divide each number by it.
// Provide a O(1) space complexity solution if you can.
*/
// O(N), O(1) time, space complexity.
const solution = (nums) =>{
    var len = nums.length
    var answer = new Array(len).fill(1)


    for(var i = 1; i < len; i++){
        answer[i] = answer[i-1] * nums[i-1]
    }

    var R = 1
    for(var i = len-1; i>=0; i--){
        answer[i] = answer[i] * R
        R *= nums[i]
    }

    return answer

}