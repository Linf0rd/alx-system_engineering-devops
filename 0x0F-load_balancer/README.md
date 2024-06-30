
# 0x0F. Load Balancer ⚖️

Welcome to this project of the ALX System Engineering DevOps curriculum! This repository contains tasks focused on understanding and implementing load balancing to distribute workloads across multiple computing resources. Each task here serves a specific purpose to help understand various aspects of load balancing configuration and management.

## Table of Contents

-   [Tasks](#tasks)
    -   [0. Double the number of webservers](#0-double-the-number-of-webservers)
    -   [1. Install your load balancer](#1-install-your-load-balancer)
    -   [2. Add a custom HTTP header with Puppet](#2-add-a-custom-http-header-with-puppet)
-   [How to Run](#how-to-run)
-   [Dependencies](#dependencies)
-   [Author](#author)

## Tasks

### 0. Double the number of webservers

🔄 **Task:** Configure your web-02 server as a mirror of your web-01 server. Ensure that both servers have the same content.

### 1. Install your load balancer

💻 **Task:** Install and configure HAProxy on your lb-01 server to distribute requests between web-01 and web-02.

### 2. Add a custom HTTP header with Puppet

🛠️ **Task:** Use Puppet to automate the configuration of HAProxy to add a custom HTTP header to all responses.

## How to Run

1.  **Clone the repository:**
  
    `git clone https://github.com/Linf0rd/alx-system_engineering-devops.git`
    
    `cd alx-system_engineering-devops/0x0F-load_balancer` 
    
3.  **Run the Puppet manifest:**
        
    `puppet apply <manifest_name>.pp` 
    

## Dependencies

-   **HAProxy:**  Ensure you have HAProxy installed.
        
    `sudo apt-get install haproxy` 
    
-   **Puppet:**  Ensure you have Puppet installed.
    
    `sudo apt-get install puppet` 
    

## Author

👨‍💻 **Linf0rd**