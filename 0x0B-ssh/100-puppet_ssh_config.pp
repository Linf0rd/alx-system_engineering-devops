# Setting up client config file

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => template('ssh_config.erb'),
}
