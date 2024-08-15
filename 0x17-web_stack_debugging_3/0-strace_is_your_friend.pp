# A puppet script to replace a line in a file on a server

$file_to_edit = '/var/www/html/wp-settings.php'

# Replace line containg 'phpp' with 'php'

exec { 'replace_phpp_with_php':
  command => "sed -i 's/phpp/php/g' ${file_to_edit}",
  path    => ['/bin', '/usr/bin'],
  onlyif  => "grep 'phpp' ${file_to_edit}",
}
