# Creates a manifest that kills a process named killmenow.
exec { 'kill_process':
    command => 'pkill -f killmenow',
    path    => ['/usr/bin', '/usr/local/bin'],
}
