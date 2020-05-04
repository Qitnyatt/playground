<?php

// https://www.codewars.com/kata/5a54e796b3bfa8932c0000ed/train/php

function jumpingNumber($n)
{
    $prev_number = -1;
    foreach (array_map('intval', str_split(strval($n))) as $number) {
        if ($prev_number == -1) {
            $prev_number = $number;
            continue;
        }
        if (($prev_number - 1 != $number) && ($prev_number + 1 != $number)) {
            return "Not!!";
        }
        $prev_number = $number;
    }
    return "Jumping!!";
}
