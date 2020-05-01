// https://www.codewars.com/kata/sum-of-positive/train/javascript


const positiveSum = (arr) => arr.reduce((a, v) => v > 0 ? a + v : a, 0);
