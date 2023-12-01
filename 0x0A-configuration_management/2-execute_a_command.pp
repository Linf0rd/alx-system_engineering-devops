# This manifest kills the process named "killmenow"

exec { 'killmenow':
  command => 'pkill -f killmenow',
}
