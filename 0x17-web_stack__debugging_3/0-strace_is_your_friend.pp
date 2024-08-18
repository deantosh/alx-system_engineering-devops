file_line { 'fix_class_wp_locale_extension':
  path  => '/var/www/html/wp-settings.php',
  line  => 'require_once( ABSPATH . WPINC . \'/class-wp-locale.php\' );',
  match => '^require_once\( ABSPATH \. WPINC \. \'/class-wp-locale.phpp\' \);',
}