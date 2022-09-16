# execute the command to kill the process killmenow

exec { 'pkill killmenow':
  path  =>  'usr/bin:/usr/sin/:/bin'
}
