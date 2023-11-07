file_line { 'fix_typo':
        path  => '/var/www/html/wp-settings.php',
        line  => 'php',
        match => 'phpp',
}
