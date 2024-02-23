file { 'school':
  path    => '/tmp/school',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}

file { '/tmp':
  ensure => 'directory',
  mode   => '1777',
}
