# Manifest fixes apache2 internal server error:500

$file_name = '/var/www/html/wp-settings.php'

exec { 'fix_class_wp_locale_extension':
  command => "sed -i 's/phpp/php/g' ${file_name}",
  path    => ['/bin', '/usr/bin']
}
