#!/bin/bash

# Script to create users from a CSV file

# Create a variable for the CSV file
csv_file="./data.csv"

# Set up variables to initialize the starting user ID
year1_uid_start=1000
year2_uid_start=2000

# Ensure the groups exist
echo "Checking if groups exist..."
if ! sudo getent group ITAS_YR1 > /dev/null 2>&1; then
  sudo groupadd ITAS_YR1
  echo "Group ITAS_YR1 created."
fi
if ! sudo getent group ITAS_YR2 > /dev/null 2>&1; then
  sudo groupadd ITAS_YR2
  echo "Group ITAS_YR2 created."
fi
echo "Groups checked."

# User creation iteration counter
user_count=1

# Reading the CSV and creating users with the full name in the comment field
while IFS=',' read -r firstname lastname dob year
do
    echo "Processing user #${user_count}..."

    # Extract the username from the first name and last name, lowercase it
    username="${firstname:0:1}${lastname}"
    username="${username,,}"

    # Capitalize the first letter of first and last name, and then join them with a comma and space
    proper_lastname="${lastname^}"
    proper_firstname="${firstname^}"
    full_name="$proper_lastname, $proper_firstname"

    # Determine the group based on the year
    groupname=""
    if [ "$year" = "Year 1" ]; then
        groupname="ITAS_YR1"
        userid=$year1_uid_start
        ((year1_uid_start++)) # Increment the UID for the next Year 1 student
    elif [ "$year" = "Year 2" ]; then
        groupname="ITAS_YR2"
        userid=$year2_uid_start
        ((year2_uid_start++)) # Increment the UID for the next Year 2 student
    fi

    # Check if groupname is not empty
    if [ ! -z "$groupname" ]; then
        # Create the user with the home directory, set the user to the correct group,
        # and add the full name in the 'Lastname, Firstname' format to the comment field
        echo "Creating user $username..."
        sudo useradd -m -u "$userid" -c "$full_name" -d "/home/$username" -g "$groupname" -s "/bin/bash" "$username"
        if [ $? -eq 0 ]; then
            # Set directory permissions to 700
            echo "Setting directory permissions for /home/$username..."
            sudo chmod 700 "/home/$username"
            
            # Format DOB from mm/dd/yy to yymmdd and initials to lowercase for the password
            IFS='/' read -r mm dd yy <<< "$dob"
            mm=$(printf "%02d" $mm) # Add leading zeroes if missing
            dd=$(printf "%02d" $dd)

            # Extract the first letter of the first name and last name, lowercase it
            first_initial="${firstname:0:1}"
            last_initial="${lastname:0:1}"
            first_initial="${first_initial,,}"
            last_initial="${last_initial,,}"

            # Combine them with the date of birth for the password
            password="${first_initial}${last_initial}$yy$mm$dd"
            
            # Change password to the correct format
            echo "Updating password for $username..."
            echo "$username:$password" | sudo chpasswd
            echo "User created: $username with password: $password"
        else
            echo "Failed to create user: $username"
        fi
    else
        echo "Groupname for $username is empty, skipping user creation."
    fi

    # Increment the user creation counter
    ((user_count++))

    echo "User #${user_count} processed."

done < "$csv_file"

echo "Script completed. Processed $user_count users."
