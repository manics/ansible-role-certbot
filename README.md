# Ansible Role: Certbot (for Let's Encrypt)

[![Build Status](https://travis-ci.org/openmicroscopy/ansible-role-certbot.svg?branch=master)](https://travis-ci.org/openmicroscopy/ansible-role-certbot)

Installs and configures Certbot (for Let's Encrypt).


## Role Variables

### Auto-renewal

- `certbot_auto_renew`: Configure a daily cronjob to automatically renew certificates, default `True`
- `certbot_auto_renew_options`: default certbot renew arguments, don't change this unless you have to
- `certbot_auto_renew_args`: additional arguments appended to the default renew arguments

### Automatic Certificate Generation

- `certbot_create_if_missing`: Create a new certificate if necessary, default `yes`
- `certbot_admin_email`: Email, required if `certbot_create_if_missing: yes`
- `certbot_domains`: List of domains to acquire certificates for, required if `certbot_create_if_missing: yes`
- `certbot_create_command`: default certbot create arguments, don't change this unless you have to
- `certbot_create_args`: additional arguments appended to the default create arguments, default `--standalone`
- `certbot_create_standalone_stop_services`: List of services to stop before creating certificates, and to start again aferwards, default `[]`

Certbot requires a webserver to respond to the Let's Encrypt ACME challenge.
You can either use the standalone server built-in to certbot, or configure an existing server to publish `/.well-known/acme-challenge/` and pass the root file location to certbot by setting `certbot_create_args: --webroot --webroot-path /srv/www/`


## Dependencies

None.


## License

MIT / BSD


## Author Information

This role was created in 2016 by [Jeff Geerling](https://www.jeffgeerling.com/), author of [Ansible for DevOps](https://www.ansiblefordevops.com/).
