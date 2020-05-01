<?php

// https://www.codewars.com/kata/5a4e3782880385ba68000018/train/php

function balancedNum($num)
{
    $length = count(str_split(strval($num)));
    $correction = 0;
    if ($length % 2 === 0) {
        $correction = -1;
    }
    $lhs = array_splice(str_split(strval($num)), 0, intdiv($length, 2) + $correction);
    $rhs = array_splice(str_split(strval($num)), intdiv($length, 2) + 1, $length);
    if (array_sum(array_map('intval', $lhs)) == array_sum(array_map('intval', $rhs))) {
        return "Balanced";
    }
    return "Not Balanced";
}
