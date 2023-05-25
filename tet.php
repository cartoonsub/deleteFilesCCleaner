<?php

$path = 'delete.txt';
if (!is_file($path)) {
    echo 'File not found!';
    exit;
}

$mime = mime_content_type($path);
$filename = pathinfo($path, PATHINFO_BASENAME);
$size = filesize($path);
echo 'mime: ' . $mime . PHP_EOL;

$content = file_get_contents($path);
$content = mb_convert_encoding($content, 'UTF-8', 'UTF-16');
file_put_contents($path, $content);
$encoding = mb_detect_encoding($content);
echo 'encoding: ' . $encoding . PHP_EOL;
$rows = file($path);
foreach ($rows as $row) {
    echo $row . PHP_EOL;
    echo 'encoding: ' . mb_detect_encoding($row) . PHP_EOL;
    echo $row . PHP_EOL;
    sleep(1);
}
