
# 0x0B. SSH 🔒

Welcome to this project of the ALX System Engineering DevOps curriculum! This repository contains tasks focused on understanding and using SSH (Secure Shell) for secure communication between systems. Each task here serves a specific purpose to help understand how to configure and use SSH.

## Table of Contents

-   [Tasks](#tasks)
    -   [0. Use a private key](#0-use-a-private-key)
    -   [1. Create an SSH key pair](#1-create-an-ssh-key-pair)
    -   [2. Client configuration file](#2-client-configuration-file)
    -   [3. Let me in!](#3-let-me-in)
    -   [4. Client configuration file (w/ Puppet)](#4-client-configuration-file-w-puppet)
-   [How to Run](#how-to-run)
-   [Dependencies](#dependencies)
-   [Author](#author)

## Tasks

### 0. Use a private key

🔑 **Task:** Write a Bash script that uses `ssh` to connect to your server using a private key.

### 1. Create an SSH key pair

🔐 **Task:** Create an RSA key pair and set up authentication using this key pair.

### 2. Client configuration file

📝 **Task:** Write a SSH client configuration file to simplify and customize SSH connections.

### 3. Let me in!

🔓 **Task:** Add your SSH public key to the server so you can log in without a password.

### 4. Client configuration file (w/ Puppet)

🛠️ **Task:** Use Puppet to set up your client SSH configuration file so that you can connect to a server without typing a password.

## **Requirements:**

-   Your SSH client configuration must be configured to use the private key  `~/.ssh/school`
-   Your SSH client configuration must be configured to refuse to authenticate using a password

## How to Run

1.  **Clone the repository:**
       
    `git clone https://github.com/Linf0rd/alx-system_engineering-devops.git`
    
    `cd alx-system_engineering-devops/0x0B-ssh` 
    
2.  **Run the scripts:**
    
    `chmod +x <script_name>
    ./<script_name>` 
    

## Dependencies

-   **SSH:**  Ensure you have SSH installed.
    
    `sudo apt-get install openssh-client` 
    

## Author

👨‍💻 **Linf0rd**