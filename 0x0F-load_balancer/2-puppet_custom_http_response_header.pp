# Puppet installs nginx server.
# Configures it based on the requirements:
#	- listen to port 80
#	- add default response ("Hello World!")
#	- add custom 404 error page (content = "Ceci n'est pas une page")
#	- handle a single page redirection ("/redirect_me")
#	- add custom header X-Served-By set to 'hostname'.


# install latest nginx version
package {'nginx':
  ensure => 'latest',
}

# config nginx -- add index page
file {'/var/www/html/index.html':
  ensure  => 'present',
  content => 'Hello World!',
}

# config nginx -- add custom 404 error page
file {'/var/www/html/404.html':
  ensure  => 'present',
  content => "Ceci n'est pas une page",
}

# config nginx -- single page redirection (redirect_me)
$line = "server_name _;\\n\\trewrite ^\\/redirect_me https:\\/\\/mattfarley.ca permanent;"

exec {'redirect_me':
  command  => inline_template("sed -i 's/server_name _;/${line}/' /etc/nginx/sites-enabled/default"),
  provider => 'shell',
}

# config nginx -- redirect to custom 404 error page
$str = "listen 80 default_server;\\n\\terror_page 404 \\/404.html;\\n\\t\
location = \\/404.html{\\n\\t\\troot \\/var\\/www\\/html;\\n\\t\\tinternal;\\n\\t}"

exec {'redirect_404_page':
  command  => inline_template("sed -i 's/listen 80 default_server;/${str}/' /etc/nginx/sites-enabled/default"),
  provider => 'shell',
}

# config nginx -- add custom X-Served-By header
$new_line = "server_name _;\\n\\tadd_header X-Served-By ${hostname};"

exec {'add_custom_header':
  command  => "sed -i 's/server_name _;/${new_line}/' /etc/nginx/sites-enabled/default",
  provider => 'shell',
}

# start nginx to update changes
exec {'run':
  command  => 'sudo service nginx start',
  provider => 'shell',
}
