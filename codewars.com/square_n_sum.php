<?php

// https://www.codewars.com/kata/square-n-sum/train/php

function square_sum($numbers): int
{
    return array_sum(array_map(function ($x) {
        return $x * $x ;
    }, $numbers));
}
