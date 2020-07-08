<?php

// https://www.codewars.com/kata/550498447451fbbd7600041c/train/php

function comp($a1, $a2)
{
    if ($a1 === null && $a2 === null) {
        return true;
    }
    if ($a1 === null || $a2 === null) {
        return false;
    }
    $tmp = array_map(function ($el) {
        return $el * $el;
    }, $a1);
    sort($tmp);
    sort($a2);
    return $tmp === $a2;
}
