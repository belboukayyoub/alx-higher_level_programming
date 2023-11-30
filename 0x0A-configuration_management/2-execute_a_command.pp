# manifest that kills a process named killmenow.
exec { 'pkill':
  command => 'pkill  killmenow',
  path    => '/bin/'
}
