#Filename: create_a_file.pp
#Ensure the file is created with the specified attributes.

file {'/tmp/school':
  ensure => 'file',		#ensure the file is present
  content => 'I love Puppet',	#content of the file.
  mode => '0744',		#file permission.
  owner => 'www-data',		#File owner
  group => 'www-data',		#File group
 }
