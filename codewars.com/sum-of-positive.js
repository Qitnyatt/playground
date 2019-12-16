// https://www.codewars.com/kata/sum-of-positive/train/javascript


function positiveSum(arr) {
    let accumulator = 0;
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] > 0) {
            accumulator += arr[i];
        }
    }
    return accumulator;
}
