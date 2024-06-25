
# 0x02. Shell, I/O Redirections and Filters 🔄

Welcome to this project of the ALX System Engineering DevOps curriculum! This repository contains tasks that focus on input/output redirection and filtering in shell scripts. Each script here serves a specific purpose to help understand how to manage data streams and manipulate text using shell commands.

## Table of Contents

-   [Tasks](#tasks)
    -   [0. Hello World](#0-hello-world)
    -   [1. Confused smiley](#1-confused-smiley)
    -   [2. Let's display a file](#2-lets-display-a-file)
    -   [3. What about 2?](#3-what-about-2)
    -   [4. Last lines of a file](#4-last-lines-of-a-file)
    -   [5. I'd prefer the first ones actually](#5-id-prefer-the-first-ones-actually)
    -   [6. Line #2](#6-line-2)
    -   [7. It is a good file that cuts iron without making a noise](#7-it-is-a-good-file-that-cuts-iron-without-making-a-noise)
    -   [8. Save current state of directory](#8-save-current-state-of-directory)
    -   [9. Duplicate last line](#9-duplicate-last-line)
    -   [10. No more javascript](#10-no-more-javascript)
    -   [11. Don't just count your directories, make your directories count](#11-dont-just-count-your-directories-make-your-directories-count)
    -   [12. What’s new](#12-whats-new)
    -   [13. Being unique is better than being perfect](#13-being-unique-is-better-than-being-perfect)
    -   [14. It must be in that file](#14-it-must-be-in-that-file)
    -   [15. Count that word](#15-count-that-word)
    -   [16. What's next?](#16-whats-next)
    -   [17. I hate bins](#17-i-hate-bins)
    -   [18. Letters only please](#18-letters-only-please)
    -   [19. A to Z](#19-a-to-z)
    -   [20. Without C, you would live in hiago](#20-without-c-you-would-live-in-hiago)
    -   [21. esreveR](#21-esrever)
    -   [22. DJ Cut Killer](#22-dj-cut-killer)
    -   [23. Empty casks make the most noise](#23-empty-casks-make-the-most-noise)
    -   [24. A gif is worth ten thousand words](#24-a-gif-is-worth-ten-thousand-words)
    -   [25. Acrostic](#25-acrostic)
    -   [26. The biggest fan](#26-the-biggest-fan)
-   [How to Run](#how-to-run)
-   [Dependencies](#dependencies)
-   [Author](#author)

## Tasks

### 0. Hello World

🔧 **Task:** A script that prints "Hello, World", followed by a new line to the standard output.

### 1. Confused smiley

😕 **Task:** A script that displays a confused smiley "(Ôo)'".

### 2. Let's display a file

📂 **Task:** A script that displays the content of the `/etc/passwd` file.

### 3. What about 2?

📂 **Task:** A script that displays the content of `/etc/passwd` and `/etc/hosts`.

### 4. Last lines of a file

📜 **Task:** A script that displays the last 10 lines of `/etc/passwd`.

### 5. I'd prefer the first ones actually

📜 **Task:** A script that displays the first 10 lines of `/etc/passwd`.

### 6. Line #2

📜 **Task:** A script that displays the third line of the file `iacta`.

### 7. It is a good file that cuts iron without making a noise

✂️ **Task:** A script that creates a file named exactly `\*\\'"Best School"\'\\*$\?\*\*\*\*\*:)` containing the text `Best School`.

### 8. Save current state of directory

💾 **Task:** A script that writes into the file `ls_cwd_content` the result of the command `ls -la`.

### 9. Duplicate last line

📄 **Task:** A script that duplicates the last line of the file `iacta`.

### 10. No more javascript

🗑️ **Task:** A script that deletes all the regular files (not directories) with a `.js` extension in the current directory and its subfolders.

### 11. Don't just count your directories, make your directories count

📁 **Task:** A script that counts the number of directories and sub-directories in the current directory.

### 12. What’s new

🆕 **Task:** A script that displays the 10 newest files in the current directory.

### 13. Being unique is better than being perfect

📝 **Task:** A script that takes a list of words as input and prints only words that appear exactly once.

### 14. It must be in that file

🔍 **Task:** A script that displays lines containing the pattern “root” from the file `/etc/passwd`.

### 15. Count that word

🔢 **Task:** A script that displays the number of lines that contain the pattern “bin” in the file `/etc/passwd`.

### 16. What's next?

🔎 **Task:** A script that displays lines containing the pattern “root” and 3 lines after them in the file `/etc/passwd`.

### 17. I hate bins

🚫 **Task:** A script that displays all the lines in the file `/etc/passwd` that do not contain the pattern “bin”.

### 18. Letters only please

🔠 **Task:** A script that displays all lines of the file `/etc/ssh/sshd_config` starting with a letter.

### 19. A to Z

🔄 **Task:** A script that replaces all characters `A` and `c` from input to `Z` and `e` respectively.

### 20. Without C, you would live in hiago

🚫 **Task:** A script that removes all letters `c` and `C` from input.

### 21. esreveR

🔄 **Task:** A script that reverses its input.

### 22. DJ Cut Killer

🎶 **Task:** A script that displays all users and their home directories, sorted by users.

### 23. Empty casks make the most noise

🔎 **Task:** A script that finds all empty files and directories in the current directory and all sub-directories.

### 24. A gif is worth ten thousand words

🖼️ **Task:** A script that lists all the files with a .gif extension in the current directory and all its sub-directories.

### 25. Acrostic

🔠 **Task:** A script that decodes acrostics that use the first letter of each line.

### 26. The biggest fan

📊 **Task:** A script that parses web servers logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests.

## How to Run

1.  **Clone the repository:**
    
    `git clone https://github.com/Linf0rd/alx-system_engineering-devops.git`
    
    `cd alx-system_engineering-devops/0x02-shell_redirections` 
    
2.  **Run the scripts:**
    
    `chmod +x <script_name>`
    
	   `./<script_name>` 
    

## Dependencies

-   **Shell:**  Ensure you have a Unix-like shell environment.

## Author

👨‍💻 **Linf0rd**