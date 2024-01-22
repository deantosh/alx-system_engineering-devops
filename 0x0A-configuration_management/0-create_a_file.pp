# Ensure group exists
group{ 'www-data':
  ensure  => present,
}


# Ensure user 'www-data' exists 
user{ 'www-data':
  ensure     => present,
  managehome => true,
  gid        => 'www-data',
}


# Creates `/tmp/school`
file {'/tmp/school':
  ensure  => present,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => "I love puppet\n",
}
