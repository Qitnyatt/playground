<?php

// https://www.codewars.com/kata/5a53a17bfd56cb9c14000003/train/php

function disariumNumber($n)
{
    $result = 0;
    foreach (array_map('intval', str_split(strval($n))) as $index => $item) {
        $result += $item ** ($index + 1);
    }
    return $n === $result ? "Disarium !!" : "Not !!";
}
