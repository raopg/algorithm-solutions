const solution  = (nums) =>{
    if (nums.length === 1){
        return nums[0]
    }

    for(var i = 1; i < nums.length; i++){
        nums[i] =  Math.max(nums[i], nums[i-1] + nums[i])
    }

    return Math.max(...nums)
}

// Takeaway -  The max function in JavaScript does not take iterables. You need to use object expansion (...) provided by ES6+.
