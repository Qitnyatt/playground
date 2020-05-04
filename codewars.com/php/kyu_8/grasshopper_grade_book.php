<?php

// https://www.codewars.com/kata/grasshopper-grade-book/train/php

function getGrade($a, $b, $c)
{
    $score = intval(($a + $b + $c) / 3);
    if (90 <= $score && $score <= 100) {
        return 'A';
    } elseif (80 <= $score && $score < 90) {
        return 'B';
    } elseif (70 <= $score && $score < 80) {
        return 'C';
    } elseif (60 <= $score && $score < 70) {
        return 'D';
    } elseif (0 <= $score && $score < 60) {
        return 'F';
    } else {
        return '?';
    }
}
