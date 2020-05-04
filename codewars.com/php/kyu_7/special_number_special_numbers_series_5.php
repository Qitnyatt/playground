<?php

// https://www.codewars.com/kata/5a55f04be6be383a50000187/train/php

function specialNumber($n)
{
    foreach (array_map('intval', str_split(strval($n))) as $number) {
        if (!(0 <= $number && $number <= 5)) {
            return "NOT!!";
        }
    }
    return "Special!!";
}
