<?php

// https://www.codewars.com/kata/sum-mixed-array/train/php

function sum_mix($a)
{
    return array_reduce($a, function ($carry, $item) {
        return $carry + intval($item);
    }, 0);
}
