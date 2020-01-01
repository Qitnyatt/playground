<?php

// https://www.codewars.com/kata/beginner-lost-without-a-map/train/php

function maps($x)
{
    return array_map(function ($a) {
        return $a * 2;
    }, $x);
}
