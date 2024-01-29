# Using 'Puppet' to make changes to configuration file

# Include the stdlib module
include stdlib

# Update or Add 'PasswordAuthentication on'
file_line { 'turn_off_password':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '   PasswordAuthentication on',
}

# Update or add 'private key'
file_line { 'Declare file identity':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '   IdentityFile ~/.ssh/school',
}
