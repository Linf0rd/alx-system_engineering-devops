# Installs flask

exec { 'Flask 2.1.0':
  command => 'pip3 install flask -v 2.1.0',
  path => ['/usr/bin'],
}
