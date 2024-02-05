# Puppet manifest to fix Apache 500 error
# and automate the fix

exec { '/var/www/html/wp-setting.php':
  command => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
}
