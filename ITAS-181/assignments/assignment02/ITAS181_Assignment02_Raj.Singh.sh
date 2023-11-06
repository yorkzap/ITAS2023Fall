#!/bin/bash

# Create a variable for the CSV file
csv_file="./data.csv"

# Set up variables to initialize the starting user ID
year1_uid_start=1000
year2_uid_start=2000

# Reading the CSV and creating users with the full name in the comment field
while IFS=',' read -r firstname lastname dob year
do
    # Extract the username from the first name and last name, lowercase it
    username="${firstname:0:1}${lastname,,}"

    # Capitalize the first letter of first and last name, and then join them with a comma and space
    proper_lastname="${lastname^}"
    proper_firstname="${firstname^}"
    full_name="$proper_lastname, $proper_firstname"

    # Determine the group based on the year
    groupname=""
    if [ "$year" = "Year 1" ]; then
        groupname="ITAS_YR1"
        userid=$year1_uid_start
        # Increment the UID for the next Year 1 student
        ((year1_uid_start++))
    elif [ "$year" = "Year 2" ]; then
        groupname="ITAS_YR2"
        userid=$year2_uid_start
        #Increment the UID for the next Year 2 student
        ((year2_uid_start++))
    fi

    # Check if groupname is not empty
    if [ ! -z "$groupname" ]; then
        # Create the user with the home directory, set the user to the correct group,
        # and add the full name in the 'Lastname, Firstname' format to the comment field
        sudo useradd -m -u "$userid" -c "$full_name" -d "/home/$username" -g "$groupname" "$username"
        # Set directory permissions to 700
        sudo chmod 700 "/home/$username"
        # Format DOB from mm/dd/yy to yymmdd
        IFS='/' read -r mm dd yy <<< "$dob"
        password="${firstname:0:1}${lastname:0:1}$yy$mm$dd"
        # Change password to the correct format
        echo "$username:$password" | sudo chpasswd
        echo "User created: $username with password: $password"
    fi

done < "$csv_file"
