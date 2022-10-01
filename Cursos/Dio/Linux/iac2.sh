#!/bin/bash

apt update -y
apt upgrade -y
apt install apache2 -y
apt install unzip
cd /tmp
wget https://github.com/denilsonbonatti/linux-site-dio/archive/refs/heads/main.zip
unzip main.zip
cp linux-site-dio-main/* -r /var/www/html/
