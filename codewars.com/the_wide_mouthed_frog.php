<?php

// https://www.codewars.com/kata/the-wide-mouthed-frog/train/php

function mouth_size($animal)
{
    if (mb_strtolower($animal) == 'alligator') {
        return 'small';
    }
    return 'wide';
}
