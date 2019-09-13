const solution = (number) => {
    for(i = 1; i<=number; i++){
        result = ''
        if(i % 3 === 0){
            result += 'fizz'
        }
        if(i % 5 === 0){
            result += 'buzz'
        }

        console.log(result === '' ? i : result)
    }
}

solution(15)
