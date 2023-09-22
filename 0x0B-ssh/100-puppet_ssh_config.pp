file_line{'Set alias name':
  path => '/etc/ssh/ssh_config',
  line => 'Host 54.210.89.176',
}
file_line{'Set host name':
  path => '/etc/ssh/ssh_config',
  line => '    HostName 54.210.89.176',
}
file_line{'Set user name':
  path => '/etc/ssh/ssh_config',
  line => '    User ubuntu',
}
file_line{'Set identity file':
  path => '/etc/ssh/ssh_config',
  line => '    IdentityFile ~/.ssh/school',
}
file_line{'Turn off passwd auth':
  path => '/etc/ssh/ssh_config',
  line => '    PasswordAuthentication no',
}
