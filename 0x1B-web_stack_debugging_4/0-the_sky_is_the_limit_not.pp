# fix bug

exec { 'nginx_fix':
  command => 'sed -i "s/15/4024/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'restart':
  command => 'sudo nginx restart',
  path    => '/etc/init.d/'
}
