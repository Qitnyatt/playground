<?php

// https://www.codewars.com/kata/century-from-year/train/php

function centuryFromYear($year)
{
    return intval(($year - 1) / 100 + 1);
}
