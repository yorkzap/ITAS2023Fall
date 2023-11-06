#!/bin/bash

# Create a variable for the CSV file
csv_file="./data.csv"

# Set up variables to initialize the starting user ID
year1_uid_start=1000
year2_uid_start=2000

#Test if the variable works (remove later)
cat "$csv_file"

while IFS=',' read -r firstname lastname dob year
do
    # Extract the username from the first name and last name, lowercase it
    username="${firstname:0:1}${lastname,,}"

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
        # Create the user with the home directory and set the user to the correct group
        sudo useradd -m -u "$userid" -d "/home/$username" -g "$groupname" "$username"
    fi

done < "$csv_file"
