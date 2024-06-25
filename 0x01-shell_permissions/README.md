
# 0x01. Shell, Permissions 🛡️

Welcome to this project of the ALX System Engineering DevOps curriculum! This repository contains tasks that explore file permissions and ownership in a Unix system. Each script here serves a specific purpose that helped me understand how to manage file and directory permissions.

## Table of Contents

-   [Tasks](#tasks)
    -   [0. My name is Betty](#0-my-name-is-betty)
    -   [1. Who am I](#1-who-am-i)
    -   [2. Groups](#2-groups)
    -   [3. New owner](#3-new-owner)
    -   [4. Empty!](#4-empty)
    -   [5. Execute](#5-execute)
    -   [6. Multiple permissions](#6-multiple-permissions)
    -   [7. Everybody!](#7-everybody)
    -   [8. James Bond](#8-james-bond)
    -   [9. John Doe](#9-john-doe)
    -   [10. Look in the mirror](#10-look-in-the-mirror)
    -   [11. Directories](#11-directories)
    -   [12. More directories](#12-more-directories)
    -   [13. Change group](#13-change-group)
    -   [14. Owner and group](#14-owner-and-group)
    -   [15. Symbolic links](#15-symbolic-links)
    -   [16. If only](#16-if-only)
    -   [17. Star Wars](#17-star-wars)
-   [How to Run](#how-to-run)
-   [Dependencies](#dependencies)
-   [Author](#author)

## Tasks

### 0. My name is Betty

🔧 **Task:** A script that changes the current user to the user `betty`.

### 1. Who am I

🛠️ **Task:** A script that prints the effective username of the current user.

### 2. Groups

👥 **Task:** A script that prints all the groups the current user is part of.

### 3. New owner

🔄 **Task:** A script that changes the owner of the file `hello` to the user `betty`.

### 4. Empty!

📂 **Task:** A script that creates an empty file called `hello`.

### 5. Execute

⚙️ **Task:** A script that adds execute permission to the owner of the file `hello`.

### 6. Multiple permissions

🔒 **Task:** A script that adds execute permission to the owner and the group owner, and read permission to other users, to the file `hello`.

### 7. Everybody!

🌍 **Task:** A script that adds execution permission to the owner, the group owner and the other users, to the file `hello`.

### 8. James Bond

🕵️ **Task:** A script that sets the permission to the file `hello` as follows: Owner: no permission at all, Group: no permission at all, Other users: all the permissions.

### 9. John Doe

👨 **Task:** A script that sets the mode of the file `hello` to `-rwxr-x-wx 1 root root 0 Jul 23 00:00 hello`.

### 10. Look in the mirror

🔍 **Task:** A script that sets the mode of the file `hello` the same as `olleh`'s mode.

### 11. Directories

📁 **Task:** A script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed.

### 12. More directories

📂 **Task:** A script that creates a directory called `my_dir` with permissions 751 in the working directory.

### 13. Change group

🔧 **Task:** A script that changes the group owner to `school` for the file `hello`.

### 14. Owner and group

🛠️ **Task:** A script that changes the owner to `vincent` and the group owner to `staff` for all the files and directories in the working directory.

### 15. Symbolic links

🔗 **Task:** A script that changes the owner and the group owner of `_hello` to `vincent` and `staff` respectively.

### 16. If only

✨ **Task:** A script that changes the owner of the file `hello` to `betty` only if it is owned by the user `guillaume`.

### 17. Star Wars

🌟 **Task:** A script that will play the Star Wars IV episode in the terminal.

## How to Run

1.  **Clone the repository:**
    
    `git clone https://github.com/Linf0rd/alx-system_engineering-devops.git`
    
	   ` cd alx-system_engineering-devops/0x01-shell_permissions` 
    
2.  **Run the scripts:**
    
   
    `chmod +x <script_name>`
    
    `./<script_name>` 
    

## Dependencies

-   **Shell:**  Ensure you have a Unix-like shell environment.

## Author

👨‍💻 **Linf0rd**