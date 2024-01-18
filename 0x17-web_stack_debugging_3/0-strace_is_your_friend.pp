# Puppet manifest to fix Apache 500 error
# and automate the fix

# Install strace package
package { 'strace':
  ensure => installed,
}

# Define a Puppet exec resource to run strace on Apache process
exec { 'strace_apache':
  command     => 'strace -f -e trace=write -p $(pgrep -o apache2)',
  path        => '/usr/bin',
  refreshonly => true,
  logoutput   => true,
  notify      => Exec['fix_apache'],
}

# Define a Puppet exec resource to fix Apache
exec { 'fix_apache':
  command     => 'service apache2 restart',
  path        => '/usr/sbin:/usr/bin:/sbin:/bin',
  refreshonly => true,
  logoutput   => true,
}

# Trigger strace and fix Apache on demand
exec { 'trigger_strace_and_fix':
  command   => '/bin/true',
  path      => '/bin:/usr/bin',
  require   => [Package['strace'], Exec['strace_apache']],
  subscribe => Exec['fix_apache'],
}
