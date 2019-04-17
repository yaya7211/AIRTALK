<?php
$my_file = 'messagefeed.txt'; 
$handle = fopen($my_file, 'a') or die('Cannot open file:  '.$my_file); 
$data = $_GET['u']."\n"; 
?>