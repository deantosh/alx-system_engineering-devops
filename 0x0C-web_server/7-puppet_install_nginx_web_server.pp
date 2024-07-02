# Script to install and configure nginx using puppet

package {'nginx':
  ensure => present,
}

exec {'install_nginx':
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
  provider => shell,

}

exec {'hello_world':
  command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html > /dev/null',
  provider => shell,
}

exec {'update_nginx_config':
  command  => 'sudo sed -i "s/server_name _;/server_name _;\\n\\trewrite ^\\/redirect_me https:\\/\\/mattfarley.ca permanent;/" /etc/nginx/sites-enabled/default',
  provider => shell,
}

exec {'run':
  command  => 'sudo service nginx restart',
  provider => shell,
}