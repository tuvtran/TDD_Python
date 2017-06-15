Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3.6
* virtualenv + pip
* Git

eg, on Ubuntu:

```bash
sudo add-apt-repository ppa:fkrull/deadsnakes
sudo apt-get install nginx git python3.6 python3.6-venv
```

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, e.g., staging.example.com

## Systemd service

* see gunicorn-systemd.template.service
* replace SITENAME with, e.g., staging.example.com
* replace SERKIT with email password

## Folder structure:
Assume we have a user account at /home/username

```
/home/username
└── sites
    └── SITENAME
         ├── database
         ├── source
         ├── static
         └── virtualenv
```