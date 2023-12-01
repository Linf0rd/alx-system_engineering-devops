# Installs flask

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3'],
}
