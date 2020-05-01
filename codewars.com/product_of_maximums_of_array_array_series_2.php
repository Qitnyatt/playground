<?php

// https://www.codewars.com/kata/5a63948acadebff56f000018/train/php

function maxProduct($arr, $size)
{
    rsort($arr);
    return array_product(array_slice($arr, 0, $size));
}
