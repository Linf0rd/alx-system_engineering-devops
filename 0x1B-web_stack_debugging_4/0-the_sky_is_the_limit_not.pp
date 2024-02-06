# Increase the amount of traffic the server (Nginx) can take on.

exec { 'fix--for-nginx':
  command => '/bin/sed -i \'s/ULIMIT="-n 15"/ULIMIT="-n 4096"/\' /etc/default/nginx',
}

exec { 'nginx-restart':
  command => '/usr/sbin/service nginx restart',
}
