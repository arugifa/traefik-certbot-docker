#!/usr/bin/env python3

import asyncio
import configparser
import docker
import logging
import re

# Certbot
CERTBOT_CONFIG_DIR = Path('/etc/letsencrypt')
CERTBOT_CONFIG_FILENAME = 'cli.ini'

client = docker.from_env()
logger = logging.getLogger(__name__)


def get_hostname_from_labels(event):
    for attr, value in event['Attributes'].items():
        if re.match(r'traefik\.http\.routers\..+\.rule', attr):
            return re.match(r'Host\(`(.+)`\)', value).group(1)


def add_domain(domain):
    config = configparser.ConfigParser()
    config.read(CERTBOT_CONFIG_DIR / CERTBOT_CONFIG_FILENAME)

    config.

    with (CERTBOT_CONFIG_DIR / CERTBOT_CONFIG_FILENAME).open('w') as f:




def main(certbot_config):
    config = configparser.ConfigParser()

    try:
        config.read_file(open(CERTBOT_CONFIG_DIR / CERTBOT_CONFIG_FILENAME))
    except FileNotFoundError:


    for event in client.events(decode=True):
        if event['Type'] == 'container' and event['Action'] == 'create':
            if hostname := get_hostname_from_labels(event):
                add_domain(hostname)
                generate_tls_certificates()

        elif event['Type'] == 'container' and event['Action'] == 'destroy':
            if hostname := get_hostname_from_labels(event):
                remove_domain(hostname)


if __name__ == '__main__':
    main()
