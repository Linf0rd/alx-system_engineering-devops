# Install flask

package { 'Flask':
  ensure   => present,
  version  => '2.1.0',
  provider => pip3,
}
