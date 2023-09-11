# Web App Production - ReadMe

## Overview

This repository contains a production plan for running web apps in the ITAS 181 class. It emphasizes the use of Long-Term Release (LTR) operating systems and software versions to ensure stability and reliability.

## Key Points/Notes for class

## Table of Contents for CompTIA Linux and LPIC-1: Guide to Linux Certification

- Chapter 1
- Chapter 2

### Chapter 1

### Chapter 2

- [Select LTR Operating System](#select-ltr-operating-system): Always bet on LTR software for avoiding mess ups. Always LTR in production unnecessary.
- Custom OS Installation Guide (Fedora):

  1. Boot from installation media.
  2. Select custom/manual installation.
  3. Create, edit, and assign partitions.
  4. Review settings and confirm.
  5. Complete installation and configure post-installation.

#### Note:

For macOS and SCSI systems, use SATA for Linux installation storage to ensure compatibility.

- Two partitions get created when installing Linux. This is for security purposes.
  1. root (All OS files)
  2. boot (Needed for boot files)
  3. swap (Partition used for virtual memory for when RAM runs out)

- **Command Cheat Sheet for Linux:**

  - `pwd`: Print working directory.
  - `ls`: List files and directories.
    - `ls -l`: List in long format (permissions, owner, size, etc.).
    - `ls -a`: List hidden files (those starting with a dot).
  - `cd`: Change directory.
    - `cd ~` or `cd`: Go to the home directory.
    - `cd ..`: Go up one directory.
  - `mkdir [directory_name]`: Create a new directory.
  - `rmdir [directory_name]`: Remove an empty directory.
  - `touch [file_name]`: Create an empty file.
  - `cp [source] [destination]`: Copy files or directories.
  - `mv [source] [destination]`: Move or rename files or directories.
  - `rm [file_name]`: Remove (delete) a file.
    - `rm -r [directory_name]`: Remove a directory and its contents recursively (use with caution).
  - `cat [file_name]`: Display the contents of a file.
  - `nano [file_name]` or `vim [file_name]`: Edit a text file in the terminal.
  - `find [directory] -name [file_name]`: Search for files by name.
  - `grep [pattern] [file_name]`: Search for a text pattern in a file.
    - `grep -r [pattern] [directory]`: Recursively search for a text pattern in files within a directory.
  - `shutdown -P +4`: Powers off your system in 4 minutes.
  - `reboot` : Reboots your system immediately.