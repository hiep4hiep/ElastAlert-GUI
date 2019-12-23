#!/bin/sh
sudo apt-get update  # To get the latest package lists
sudo apt-get install python3.6 -y
sudo apt-get install python3-pip
cd /etc/
sudo git clone https://github.com/Yelp/elastalert.git
sudo cp /etc/elastalert/config.yaml.example /etc/elastalert/config.yaml
cd /etc/elastalert/
sudo pip3 install "setuptools>=11.3"
sudo python3 setup.py install
sudo pip3 install "elasticsearch>=7.0.0"
sudo pip3 install pyyaml
sudo pip3 install django
sudo pip3 install django-widget-tweaks
#etc.