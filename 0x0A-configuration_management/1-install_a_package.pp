# Installs flask

exec { 'Flask 2.1.0':
  command => '/usr/bin/apt-get -y install flask -v 2.1.0',
}
