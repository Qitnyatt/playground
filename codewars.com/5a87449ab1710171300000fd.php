<?php

// https://www.codewars.com/kata/5a87449ab1710171300000fd/train/php

function tidyNumber($n)
{
    $prev_number = -1;
    foreach (array_map('intval', str_split(strval($n))) as $number) {
        if ($prev_number == -1) {
            $prev_number = $number;
            continue;
        }
        if ($prev_number > $number) {
            return false;
        }
        $prev_number = $number;
    }
    return true;
}
