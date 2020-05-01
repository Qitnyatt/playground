<?php

// https://www.codewars.com/kata/5b39e3772ae7545f650000fc/train/php

function removeDuplicateWords($s) {
    return join(" ", array_unique(explode(" ", $s)));
}
