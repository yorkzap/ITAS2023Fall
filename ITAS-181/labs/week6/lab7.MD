# Discovery Exercises

## 7-1
- **A.** `alias mm="mount | grep 'type ext4'"`
- **B.** `export NEWHOME=$HOME`
- **C.** `grep -r host /etc > file1 2>&1`
- **D.** `set | grep "bash" | sort`
- **E.** `cat /etc/passwd | awk -F: '{print $1}' > users`

## 7-2
- **A.** The command `cp /etc/hosts ~` copies the `/etc/hosts` file into the user's home directory, with `~` representing the home directory.
- **B.** The command `cd` will change the current directory to the user's home directory.
- **C.** The command `tr a A <hosts | sort –r | pr –d >hosts` does:
    - `tr a A <hosts`: Transforms all lowercase "a" characters to uppercase "A" in the hosts file.
    - `sort –r`: Sorts the lines in reverse order.
    - `pr –d`: Outputs the result in a potentially double-spaced format (depending on the system).
    - `>hosts`: Overwrites the hosts file in the home directory with the processed content.
    
The hosts file in the user's home directory now has lowercase "a" characters changed to uppercase "A", lines sorted in reverse order, and a double-spaced format.

## 7-3
    ls /etc/hosts /etc/h 2>&1 | tr h H

## 7-4
- **A.** 
    if [ -r /etc/hosts ]; then
        echo "You have read permission"
    else
        echo "No read permission"
    fi
- **B.**
    if [ -r /etc ] && [ -x /etc ]; then
        echo "You have read and execute permissions to /etc directory."
    else
        echo "You do not have read and/or execute permissions to /etc directory."
    fi
- **C.**
    if [$TEST == "success"]; then
        echo "'success' is included in the TEST variable"
    else
        echo "'success' is not included in the TEST variable"
    fi
- **D.**
    if [ "$TEST" -eq "$RESULT" ]; then
        echo "The variable TEST is numerically equal to the variable RESULT."
    else
        echo "The variable TEST is not numerically equal to the variable RESULT."
    fi
- **E.**
    if [ "$TEST" = "success" ] && [ -e /etc/hosts ]; then
        echo "The variable TEST contains the string 'success' and /etc/hosts exists."
    else
        echo "Either TEST variable does not include 'success' or /etc/hosts file does not exist"
    fi

## 7-5

- **.bash_profile:** A comment labeling the file.
- **Get the aliases and functions:** Comment indicating the purpose of the next lines.
- **if [ -f ~/.bashrc ]; then:** Checks if .bashrc exists in the user's home directory.
- **. ~/.bashrc:** If .bashrc exists, then its contents are executed.
- **fi:** Ends the if statement.
- **User specific environment...:** Yet another comment about the upcoming lines.
- **PATH=$PATH:$HOME/bin:** Appends the user's bin directory to PATH.
- **BASH_ENV=$HOME/.bashrc:** Changes BASH_ENV to point to .bashrc.
- **USERNAME="root":** Changes the USERNAME variable to "root".
- **export USERNAME BASH_ENV PATH:** Exports the three variables, making them available to child processes or processes spawned from this shell.

## 7-6

- **#!/bin/bash:** Execute using the bash shell.

- **echo –e "This program copies a file to the /stuff directory.\n":** Displays a string to the user; all that is between the quotes in the command.

- **echo –e "Which file would you like to copy? --> \c":** Displays a string to the user and then prompts the user to input a file name. Lastly, the \c ensures the cursor stays on the same line after the prompt.

- **read FILENAME:** This reads the user's input and stores it in the FILENAME variable.

- **mkdir /stuff || echo "The /stuff directory could not be created.":** Create a directory named /stuff. If there is an error, then display the error contained in the string between quote marks.

- **cp –f $FILENAME /stuff && echo "$FILENAME was successfully copied to /stuff":** Copy the file forcefully (overwrite if the file exists). If the file is copied successfully, then it displays the string message.

## 7-7

- **#!/bin/bash:** Execute using the bash shell.

- **#This script backs up the Oracle DB:** A comment describing the purpose of the script.

- **rm -f /SAN/backup-oracle*:** Delete forcefully (no warnings or confirmations) all files in the /SAN directory that start with backup-oracle.

- **if tar -zcvf /SAN/backup-oracle-'date +%F'.tar.gz /oracledb/*:** IF POSSIBLE compress all files from the '/oracledb' directory and save the result as a tarball in the '/SAN' directory with a filename that includes the current date.

- **then:** If the tar command succeeded, then execute the next commands.

- **echo "Oracle backup completed on 'date'" >>/var/log/oraclelog:** Append string to the file /var/log/oraclelog, to display that the backup is successful. It will replace 'date' with the current date and time.

- **else:** If the tar command does not work for any reason, then execute the following commands.

- **echo "Oracle backup failed on 'date'" >>/var/log/oraclelog:** Append string to the file /var/log/oraclelog, to mention that the backup failed. It will also replace 'date' with the current date and time.

- **mail -s ALERT jason.eckert@trios.com </var/log/oraclelog:** Send an email with subject "ALERT" to jason.eckert@trios.com with all the body of the /var/log/oraclelog file.

- **fi:** Ends the if statement.
