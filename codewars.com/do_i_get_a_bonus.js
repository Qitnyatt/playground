// https://www.codewars.com/kata/do-i-get-a-bonus/train/javascript


function bonusTime(salary, bonus) {
    if (bonus) {
        return '£' + salary * 10;
    }
    else {
        return '£' + salary;
    }
}
