//Simplest solution would be call reverse on a string and check if the result === original string.

const reverse = (str) =>{
    reversed = ''
    for(let char of str){
        reversed = char + reversed
    }

    return reversed
}

const palindrome = (str) =>{
    if (str === ''){
        return false
    }
    reversed = reverse(str)

    return reversed === str
}

//Fastest Solution => Because the above solution is O(n) time and space.
//This one is O(n/2) time and O(1) space

const palindromeFastest = (str) =>{
    if (str === undefined || str === ''){
        return false
    }
    var mid = Math.floor(str.length / 2)

    for(var i = 0; i < mid; i++) {
        //IMPORANT: Its i STRICTLY less than len
        if(str[i] !== str[str.length - i - 1]){
            return false
        }
    }
    return true
}

var testStrings = ['abc', 'abba', 'lol', 'aBc', 'MOM', 'DAD']

for(let string of testStrings){
    console.log(string + ' (palidrome with reverse): ' + palindrome(string))
    console.log(string + ' (palidrome fastest): ' + palindromeFastest(string))
    
}

