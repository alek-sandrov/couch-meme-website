# Meme Website Deployment Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Setting Up the Development Environment](#setting-up-the-development-environment)
4. [Flask Application Setup](#flask-application-setup)
5. [Nginx Configuration](#nginx-configuration)
6. [Obtaining a Free Domain with DuckDNS](#obtaining-a-free-domain-with-duckdns)
7. [SSL Certificate with Let's Encrypt](#ssl-certificate-with-lets-encrypt)
8. [Auto-Renewal of SSL Certificates](#auto-renewal-of-ssl-certificates)
9. [Troubleshooting](#troubleshooting)
10. [Conclusion](#conclusion)

## Introduction
This documentation aims to guide you through the process of deploying a meme website. The website uses Flask to serve memes fetched from Reddit and is secured with Nginx and Let's Encrypt.

## Prerequisites
- An Ubuntu VM
- Basic understanding of Python, Flask, and Linux commands

## Setting Up the Development Environment

### Update and Upgrade
First, let's update and upgrade the package lists and installed packages.

```bash
sudo apt update -y
sudo apt upgrade -y
```

### Installing Required Packages
Install Python3, pip3, and other required packages.

```bash
sudo apt install python3 python3-pip
```

## Flask Application Setup

### Install Flask and Requests
Install Flask and the Requests library.

```bash
pip3 install Flask
pip3 install requests
```

### Create Project Directory
Create a directory to house your Flask project and navigate into it.

```bash
mkdir meme_flask
cd meme_flask
```

### Flask App Code
Create a Python file (`meme_flask.py`) and write your Flask application code. The code should fetch memes from Reddit and display them.

### Run Flask App
Run the Flask application to make sure it's working as expected.

```bash
python3 meme_flask.py
```

## Nginx Configuration

### Install Nginx
```bash
sudo apt install nginx
```

### Start and Enable Nginx
```bash
sudo systemctl start nginx
sudo systemctl enable nginx
```

### Nginx Configuration for Flask
Edit the Nginx configuration file to include settings that reverse proxy to your Flask app. Make sure to specify the correct port where your Flask app is running.

### Test Configuration and Reload
After editing, test to make sure there are no syntax errors and reload Nginx.

```bash
sudo nginx -t
sudo systemctl reload nginx
```

## Obtaining a Free Domain with DuckDNS
Go to [DuckDNS](https://www.duckdns.org/) and follow the steps to create a free domain. Update the domain to point to your Ubuntu VM's IP address.

## SSL Certificate with Let's Encrypt

### Install Certbot
```bash
sudo apt install certbot python3-certbot-nginx
```

### Obtain Certificate
Run the following command, replacing `your_domain` with your actual domain.

```bash
sudo certbot --nginx -d your_domain
```

### Automatic Redirection
Choose to automatically redirect HTTP to HTTPS when prompted by Certbot.

## Auto-Renewal of SSL Certificates

### Test Auto-Renewal
```bash
sudo certbot renew --dry-run
```

This will simulate the auto-renewal of your SSL certificate.

## Troubleshooting
For any issues that arise, check system logs and test configurations for clues. For example, use `journalctl` to check Nginx logs.

## Conclusion
