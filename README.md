
# Project README

## Overview

This project provides a Flask application that displays the number of files and their total size in a specified directory. It uses Docker for containerization and GitLab CI/CD for automated deployment.

## Prerequisites

Before deploying this project, ensure that the following software is installed on your machine:

1. **Python 3.10 or higher**
2. **Docker**
3. **Docker Compose**
4. **Ansible**
5. **gitlab-ci**
6. **gitlab runner**
### Installing Python 3.10 or Higher

To install Python 3.10 or higher on Ubuntu, follow these steps:

```bash
# Add the deadsnakes PPA
sudo add-apt-repository ppa:deadsnakes/ppa

# Update package list
sudo apt update

# Install Python 3.10
sudo apt install python3.10

# Verify installation
python3.10 --version
```

### Installing Docker

To install Docker on Ubuntu, use the following commands:

```bash
# Update package list and install prerequisites
sudo apt update
sudo apt install apt-transport-https ca-certificates curl gnupg-agent software-properties-common

# Add Docker’s official GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# Set up the Docker repository
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

# Update package list and install Docker
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io

# Verify Docker installation
sudo systemctl status docker
```

### Installing Docker Compose

To install Docker Compose, follow these steps:

```bash
# Download Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/$(curl -s https://api.github.com/repos/docker/compose/releases/latest | grep 'tag_name' | cut -d\" -f4)/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# Apply executable permissions
sudo chmod +x /usr/local/bin/docker-compose

# Verify Docker Compose installation
docker-compose --version
```

### Installing Ansible

To install Ansible on Ubuntu, use the following commands:

```bash
# Update package list
sudo apt update

# Install Ansible
sudo apt install ansible

# Verify Ansible installation
ansible --version
```

### Installing GitLab CI/CD

To install GitLab CI/CD using Docker Compose, create a `docker-compose.yml` file with the following content:

```yaml
version: '3.6'
services:
  gitlab:
    image: gitlab/gitlab-ee
    container_name: gitlab
    restart: always
    hostname: '192.168.200.54'
    environment:
      GITLAB_OMNIBUS_CONFIG: |
        external_url 'http://192.168.200.54:8929'
        gitlab_rails['gitlab_shell_ssh_port'] = 2424
    ports:
      - '8929:8929'
      - '443:443'
      - '2424:22'
    volumes:
      - '$GITLAB_HOME/config:/etc/gitlab'
      - '$GITLAB_HOME/logs:/var/log/gitlab'
      - '$GITLAB_HOME/data:/var/opt/gitlab'
    shm_size: '256m'
```

Run the following commands to start GitLab:

```bash
# Start GitLab using Docker Compose
docker-compose up -d
```

### Installing GitLab Runner

To install GitLab Runner, use the following commands:

```bash
# Add the GitLab Runner GPG key
curl -fsSL https://packages.gitlab.com/gitlab/gitlab-runner/gpgkey | gpg --dearmor -o /usr/share/keyrings/gitlab-archive-keyring.gpg

# Add the GitLab Runner repository
echo "deb [signed-by=/usr/share/keyrings/gitlab-archive-keyring.gpg] https://packages.gitlab.com/runner/gitlab-runner/debian/ stable main" | sudo tee /etc/apt/sources.list.d/runner_gitlab-runner.list

# Update package list and install GitLab Runner
sudo apt update
sudo apt install gitlab-runner
```

### Connecting GitLab Runner to GitLab CI

Register the GitLab Runner with your GitLab instance:

```bash
# Register the GitLab Runner
gitlab-runner register
```

Follow the prompts to provide your GitLab instance URL and registration token.

## Deployment Process

1. **Connect Git Remote**

   Make sure your GitLab repository is configured as a remote:

   ```bash
   git remote add origin http://192.168.200.54:8929/root/my-app-flask.git
   ```

   Replace the URL with your GitLab repository URL.


2. **Push Changes to GitLab**

   Ensure your GitLab repository is set up and push your changes using:

   ```bash
   git add .
   git commit -m "Added new client in playbook"
   git tag -a v1.0.0 -m "Initial release"
   git push origin main --tag
   ```


3. **GitLab CI/CD Pipeline**

   The pipeline will automatically build, test, and deploy your application based on the `.gitlab-ci.yml` configuration.

## Application Files

- `dir-size-flask.py`: Flask application for displaying directory info.
- `Dockerfile`: Dockerfile for building the Flask app image.
- `my_playbook.yml`: Ansible playbook for deployment.
- `webhook_listener.py`: Script for triggering GitLab pipelines via webhook.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to adjust the instructions and details according to your specific setup and requirements.
