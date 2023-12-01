# Installs flask

exec { 'install flask 2.1.0':
  command => 'pip3 install flask==2.1.0',
  path    => ['/usr/bin'],
}
