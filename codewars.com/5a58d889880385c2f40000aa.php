<?php

// https://www.codewars.com/kata/5a58d889880385c2f40000aa/train/php

function automorphic($n)
{
    if ((substr(strval($n * $n), -strlen(strval($n))) === strval($n))) {
        return "Automorphic";
    }
    return "Not!!";
}
