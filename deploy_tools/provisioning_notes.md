Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3
* Git
* pip
* virtualenv

eg, on Ubuntu:

	sudo apt-get install nginx git python3 python3-pip
	sudo pip3 install virtaualenv

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with actual sitename

## Upstart Job

* see gunicorn-upstart.template.conf
* replace SITENAME with actual sitename

## Folder Structure
Assume we have a user account at /home/username

/home/username
└── sites
    └── SITENAME
        ├── database
        ├── source
        ├── static
        └── virtualenv
