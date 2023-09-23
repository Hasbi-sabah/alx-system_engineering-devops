# Set up server configuration with puppet
file_line{'Set alias name':
  path => '/etc/ssh/ssh_config',
  line => 'Host 54.210.89.176
    HostName 54.210.89.176
    User ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no',
}
