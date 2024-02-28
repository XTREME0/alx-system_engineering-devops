#setup nginx with puppet

exec {'commands':
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx; echo "Hello World!" | sudo dd status=none of=/var/www/html/index.html; sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \/redirect_me {\\n\\t\\treturn 301 https:\/\/boulderbugle.com\/bHVw8SFV\/;\\n\\t}/" /etc/nginx/sites-available/default; sudo service nginx restart',
  provider => shell,
}
