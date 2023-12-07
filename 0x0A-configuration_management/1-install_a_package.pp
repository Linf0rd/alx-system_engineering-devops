# Installs flask version 2.1.0 using pip3

# Ensure the package is installed
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# End of Puppet manifest
