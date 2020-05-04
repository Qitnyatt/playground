<?php

// https://www.codewars.com/kata/5949481f86420f59480000e7/train/php

function odd_or_even(array $a): string
{
    if (abs(array_sum($a)) % 2 == 1) {
        return "odd";
    }
    return "even";
}

