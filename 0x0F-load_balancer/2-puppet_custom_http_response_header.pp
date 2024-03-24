# Puppet installs nginx server.
# Configures it based on the requirements:
#	- add custom header X-Served-By set to 'hostname'

# update apt-get
exec {'update':
  command => '/usr/bin/apt-get update',
}
-> package {'nginx':
  ensure => 'present',
}
-> file_line {'add_custom_header':
  path  => '/etc/nginx/nginx.conf',
  match => 'http {',
  line  => "http {\n\tadd_header X-Served-By ${hostname}",
}
-> exec {'run':
  command => '/usr/sbin/service nginx restart',
}
