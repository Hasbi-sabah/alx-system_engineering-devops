# increase max open files for holberton user
file_line { 'replace_hard_limit':
  path  => '/etc/security/limits.conf',
  line  => 'holberton hard nofile 5000',
  match => '^holberton hard',
}
file_line { 'replace_soft_limit':
  path  => '/etc/security/limits.conf',
  line  => 'holberton soft nofile 4000',
  match => '^holberton soft',
}
