
# 0x05. Processes and Signals 📶

Welcome to this project of the ALX System Engineering DevOps curriculum! This repository contains tasks focused on processes and signals in Unix-like systems. Each script here serves a specific purpose to help understand how to manage and interact with processes and signals.

## Table of Contents

-   [Tasks](#tasks)
    -   [0. What is my PID](#0-what-is-my-pid)
    -   [1. List your processes](#1-list-your-processes)
    -   [2. Show your Bash PID](#2-show-your-bash-pid)
    -   [3. Show your Bash PID made easy](#3-show-your-bash-pid-made-easy)
    -   [4. To infinity and beyond](#4-to-infinity-and-beyond)
    -   [5. Don't stop me now!](#5-dont-stop-me-now)
    -   [6. Stop me if you can](#6-stop-me-if-you-can)
    -   [7. Highlander](#7-highlander)
    -   [8. Beheaded process](#8-beheaded-process)
    -   [9. Process and PID file](#9-process-and-pid-file)
    -   [10. Manage my process](#10-manage-my-process)
    -   [11. Zombie](#11-zombie)
    -   [12. Screencast](#12-screencast)
-   [How to Run](#how-to-run)
-   [Dependencies](#dependencies)
-   [Author](#author)

## Tasks

### 0. What is my PID

🔢 **Task:** A Bash script that displays its own PID.

### 1. List your processes

🔍 **Task:** A Bash script that displays a list of currently running processes.

### 2. Show your Bash PID

🔍 **Task:** A Bash script that displays lines containing the `bash` word, thus allowing the user to see their PID.

### 3. Show your Bash PID made easy

🔍 **Task:** A Bash script that displays the PID, along with the process name, of processes whose name contains the word `bash`.

### 4. To infinity and beyond

🔄 **Task:** A Bash script that displays `To infinity and beyond` indefinitely, with a `sleep 2` interval between each iteration.

### 5. Don't stop me now!

✋ **Task:** A Bash script that stops the `4-to_infinity_and_beyond` process.

### 6. Stop me if you can

✋ **Task:** A Bash script that stops `4-to_infinity_and_beyond` process using its PID.

### 7. Highlander

👑 **Task:** A Bash script that displays `To infinity and beyond` indefinitely with a `sleep 2` interval, but stops itself if it receives a `SIGTERM` signal.

### 8. Beheaded process

✂️ **Task:** A Bash script that kills the process `7-highlander`.

### 9. Process and PID file

📝 **Task:** A Bash script that creates a file containing its PID and checks for that file before creating it.

### 10. Manage my process

🛠️ **Task:** A Bash script that manages `4-to_infinity_and_beyond`, creating it, stopping it, and restarting it as needed.

### 11. Zombie

🧟 **Task:** A C program that creates 5 zombie processes.

### 12. Screencast

📹 **Task:** Create a screencast showing that your Bash script `10-manage_my_process` works as expected.

## How to Run

1.  **Clone the repository:**
    
    `git clone https://github.com/Linf0rd/alx-system_engineering-devops.git`
    
    `cd alx-system_engineering-devops/0x05-processes_and_signals` 
    
2.  **Run the scripts:**
    
    `chmod +x <script_name>`
    
    `./<script_name>` 
    

## Dependencies

-   **Shell:**  Ensure you have a Unix-like shell environment.

## Author

👨‍💻 **Linf0rd**