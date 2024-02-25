#puppet ssh configuration

file { '~/.ssh/config':
  ensure  => file,
  mode    => '0600',
  content => "Host 511496-web-01\n\
              HostName 100.25.132.249\n\
              User ubuntu\n\
              IdentityFile ~/.ssh/school\n\
              PasswordAuthentication no\n",
}

