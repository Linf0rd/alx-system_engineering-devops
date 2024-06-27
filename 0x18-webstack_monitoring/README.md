
# 0x18. Webstack Monitoring 📈

Welcome to this project of the ALX System Engineering DevOps curriculum! This repository contains tasks focused on monitoring web stacks. Each task here serves a specific purpose to help understand how to monitor various components of a web infrastructure.

## Table of Contents

-   [Tasks](#tasks)
    -   [0. Sign up for Datadog and install the agent](#0-sign-up-for-datadog-and-install-the-agent)
    -   [1. Monitor some metrics](#1-monitor-some-metrics)
    -   [2. Create a dashboard](#2-create-a-dashboard)
-   [How to Run](#how-to-run)
-   [Dependencies](#dependencies)
-   [Author](#author)

## Tasks

### 0. Sign up for Datadog and install the agent

🔧 **Task:** Sign up for Datadog and install the Datadog agent on your web-01 and web-02 servers.

### 1. Monitor some metrics

📊 **Task:** Set up monitoring for specific metrics such as CPU usage, memory usage, and disk usage using Datadog.

### 2. Create a dashboard

📉 **Task:** Create a dashboard in Datadog to visualize the monitored metrics.

## How to Run

1.  **Clone the repository:**
    
    `git clone https://github.com/Linf0rd/alx-system_engineering-devops.git`
    
    `cd alx-system_engineering-devops/0x18-webstack_monitoring` 
    
2.  **Follow the task instructions:**
    
    -   Sign up for Datadog, install the agent, and set up the monitoring as described in the task files and README.

## Dependencies

-   **Datadog:**  Ensure you have a Datadog account and the Datadog agent installed.
    
    `DD_AGENT_MAJOR_VERSION=7 DD_API_KEY=<YOUR_API_KEY> DD_SITE="datadoghq.com" bash -c "$(curl -L https://s3.amazonaws.com/dd-agent/scripts/install_script.sh)"` 
    

## Author

👨‍💻 **Linf0rd**