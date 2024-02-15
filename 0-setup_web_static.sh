#!/usr/bin/env bash
# script that sets up web servers for the deployment of web_static

sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html > /dev/null

sudo rm -rf /data/web_static/current

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/
sudo chmod -R 755 /data

echo -e "server {
    listen 80;
    server_name localhost;

    error_page 404 /custom_error;

    add_header X-Served-By \$hostname;

    location / {
        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
    }

    location /redirect_me {
        return 301 https://github.com/MarwaAshraf1812/;
    }

    location = /custom_error {
        internal;
        return 200 \"Ceci n'est pas une page\";
    }

    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html 103-index.html my_index.html;
    }
}" | sudo tee /etc/nginx/sites-available/default > /dev/null

# Create symbolic link to enable the configuration
sudo ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/ > /dev/null

sudo service nginx restart

exit 0