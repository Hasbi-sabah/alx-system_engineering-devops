# instal and configure nginx
exec { 'apt-update':
  command     => 'apt-get -y update',
  path        => '/usr/bin:/bin',
  refreshonly => true,
}
package { 'nginx':
  ensure => 'installed',
  require => Exec['apt-update'],
} ->

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

service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/sites-enabled/default'],
  notify    => Exec['restart_nginx'],
}

exec { 'restart_nginx':
  command     => '/usr/bin/sudo /usr/sbin/service nginx restart',
  refreshonly => true,
}
