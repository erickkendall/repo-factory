# Repo Factory

![GitHub last commit](https://img.shields.io/github/last-commit/erickkendall/repo-factory)
![GitHub issues](https://img.shields.io/github/issues/erickkendall/repo-factory)
![GitHub pull requests](https://img.shields.io/github/issues-pr/erickkendall/repo-factory)
![License](https://img.shields.io/github/license/erickkendall/repo-factory)

Repo Factory is a Terraform-based tool for automating the creation and management of GitHub repositories. It streamlines the process of setting up new projects with predefined structures, environments, and secrets.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- Automated creation of GitHub repositories
- Setup of development and production environments
- Management of repository secrets
- Consistent repository structure across projects
- Version-controlled infrastructure as code

## Prerequisites

- [Terraform](https://www.terraform.io/downloads.html) (v1.0.0+)
- [Git](https://git-scm.com/downloads)
- GitHub account with personal access token

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/erickkendall/repo-factory.git
   cd repo-factory
   ```

2. Initialize Terraform:
   ```
   terraform init
   ```

3. Create a `terraform.tfvars` file with 