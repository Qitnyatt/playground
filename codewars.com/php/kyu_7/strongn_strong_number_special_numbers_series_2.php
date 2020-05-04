<?php

// https://www.codewars.com/kata/5a4d303f880385399b000001/train/php

function strong($n)
{
    $factorial = function ($n) use (&$factorial) {
        return $n <= 1 ? 1 : $n * $factorial($n - 1);
    };
    $current = 0;
    foreach (array_map('intval', str_split(strval($n))) as $number) {
        $current += $factorial($number);
        if ($current > $n) {
            return "Not Strong !!";
        }
    }
    if ($current == $n) {
        return "STRONG!!!!";
    }
    return "Not Strong !!";
}
