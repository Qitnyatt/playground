<?php

// https://www.codewars.com/kata/volume-of-a-cuboid/train/php

$kata = new class
{
    public function get_volume_of_cuboid($length, $width, $height)
    {
        return $length * $width * $height;
    }
};
