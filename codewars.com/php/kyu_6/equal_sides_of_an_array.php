<?php

// https://www.codewars.com/kata/5679aa472b8f57fb8c000047/train/php

function find_even_index($arr)
{
    for ($i = 0; $i < count($arr); $i++) {
        $lhs = array_slice($arr, 0, $i);
        $rhs = array_slice($arr, $i + 1);
        if (array_sum($lhs) === array_sum($rhs)) {
            return $i;
        }
    }
    return -1;
}
