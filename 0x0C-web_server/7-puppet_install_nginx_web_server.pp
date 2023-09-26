# instal and configure nginx
package { 'nginx':
  ensure => 'installed',
}

file { '/var/www/html/index.nginx-debian.html':
  content => 'Hello World!',
}

file { '/etc/nginx/sites-enabled/default':
  ensure => file,
}

file_line { 'add redirect':
  path  => '/etc/nginx/sites-enabled/default',
  match => 'server_name _;',
  line  => '     location /redirect_me {return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;}',
}

exec { 'restart nginx':
  command     => '/usr/bin/sudo /usr/sbin/service nginx restart',
  refreshonly => true,
  subscribe   => File['/etc/nginx/sites-enabled/default'],
}
