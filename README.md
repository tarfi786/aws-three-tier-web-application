# Three-Tier Web Application Deployment on AWS

## Overview

This project demonstrates the deployment of a production-style three-tier web application on AWS using a secure and scalable architecture.

## Architecture

* **Web Tier:** Nginx (EC2 – Public Subnet)
* **Application Tier:** Flask + Gunicorn (EC2 – Private Subnet)
* **Database Tier:** MySQL (EC2 – Private Subnet)

## AWS Services Used

* Amazon EC2
* Amazon VPC
* Internet Gateway
* NAT Gateway
* Route Tables
* Security Groups
* IAM

## Tech Stack

* Python
* Flask
* Gunicorn
* Nginx
* MySQL
* Docker
* Linux (Ubuntu)

## Features

* View Employees
* Add Employee
* Delete Employee

## Deployment Highlights

* Designed and deployed a secure three-tier AWS architecture.
* Configured public and private subnets with Internet Gateway and NAT Gateway.
* Deployed Nginx as a reverse proxy on the Web Server.
* Hosted the Flask application with Gunicorn on the Application Server.
* Connected the application to a MySQL database hosted on a private EC2 instance.
* Configured Security Groups for secure communication between all tiers.
* Containerized the application using Docker for consistent deployment.

## Project Status

Deployment completed successfully.
