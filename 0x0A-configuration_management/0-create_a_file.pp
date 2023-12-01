# Creates a file named 'school' in the '/tmp' directory
file { '/tmp/school':
  ensure => present,
  owner => 'www-data',
  group => 'www-data',
  mode => '0744',
  content => 'I love Puppet',
}
