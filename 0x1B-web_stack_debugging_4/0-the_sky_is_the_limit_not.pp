# fix bug

exec { '/usr/bin/env sed -i s/15/5000/ /etc/default/nginx': }
-> exec { '/usr/bin/env service nginx restart': }
