

#  Linux basics


# Linux commands:

' pwd '  -> shows the current directory
 'cd'    -> change directory
 'ls'   -> shows the list of files and directories
 'ls -l' -> shows indetail with modification time and date
 'touch' -> to create a new file
 'nano'  -> to create and edit new file
 'cat'   -> to show the content in the given file
 'mkdir' -> to create a new directory
 'which' -> used to check whether the command is installed or not
 'cp'    -> used to copy the file feom one place to another
 'diff'  -> used to check the difference between 2 files
 'rm'    -> used to remove a file
 'rm -r' -> used to remove a directory this command is followed by the directory name
 'ls .'  -> same as ls -l
 'mv'    -> used to move a file from one directory to another
 'mv *'  -> this is a command used to move particular type of files that hase same letters in the end like mv *.txt all the files that ends with .txt will be moved
 'mv'    -> can also be used to rename a file 
 'mv' .. -> mv followed ny file name and 2 dots will send back the file to the previous directory like mv test2.txt .. 
 'ls -a' -> shows all the hidden files 
 'l -a'  -> dos the same work mentioned above


# Bash scripts that is used to make alias

 'to open we use : nano .bashrc'
 'we have an other way too: nano /etc/skel/.bashrc (where no changes can be made)'
 'after typing the alias in the teminal we come to home and reload '
 'to reload :source ~/.bashrc'
 'now if we type the alias it will work properly' 


# Setting Permission to Acess the files and directories
 'r - read mode'
 'w - write mode'
 'x - execute mode' 

# For directory you will be having 4 parts. 'd - directory'
 '1st rwx - for user' 
 '2nd rwx - for group'
 '3rd rwx - for aka that is world' 
 # the command we use is"chmod that means change mode"
 * 'for example chmod +x file name' to undo changes we use - instead of + in the same comand again

'For files u will be having the same but there will be no d that is directory present in it '
'you will have to enter code . in  vs code terminal if u want that to be seen in a file form '

#  Commands used to check the memory spaces
'free - used for seeing how much emory is used,free,available,swap'
'free -m it does the same work but in a efficient way'
'df - it is used to dee disk free spaces'
'df -h - same but in shows in a very efficient way that h is human understandable'
'df -i - which is used to see the toatal number of inodes , free inodes ,etc'
'/bin/df - works same as df '
'/bin/df -i - wprks same as df -i'
'htop - which is used to check memory space again, cpu 's,how long the system is on, number of tasks done etc'
'uptime - which tells how long the system is on ,pending tasks that need the help of cpu is shown'

# commands for installing and removing packages

'sudo apt upgrade'- to upgrade any packages
'apt search ____' - which package u want to search u can search through this command
'sudo apt install ____'- to install packages 
'sudo apt dist-upgrade'- if u missed any update in upgrade command this command will update the remaining
'sudo apt remove ____'- used to remove packages
'sudo apt autoremove'- used to remove packagges and the supported packages (should check the packages before accepting)
'sudo reboot'- to reboot the system for some security purposes

# commands for system mangement
'systemctl status________'- this tells that the package is active or not
'sudo systemctl status_______'- does the same but in detail
'systemctl disable_______'- this directely does not stop the running package 
'sudo systemctl stop _______'- this stops the working of the packge
'sudo systemctl start _____'- this one agains reload or starts the package 
'sudo systemctl enable ______' - this command does not directly start the dead package 
'sudo systemctl restart ________'- this command tells from how long it is n or working

* this commmands above are mainly used to know or check about the servers , browsers ,etc working in background

# commands to view logs

'path - cat /var/log/syslog'





# commands for managing users

'cat /etc/passwd'- to view the users and user id
'cat /etc/shadow'- where the password is stored
'sudo !!' - we can use this to use the previous command
'sudo adduser _____' - used to create a new user
'passwd _____' - used to change the password
'sudo passwd _______' - used to change the password without previously assigned password
'sudo su - ' - to login as a root user
'sudo userdel -r _____' - to remove the user
'sudo groupadd _______' - to add the group
'sudo usermod -aG _______ the ______(orginal group name)' - to move the new group into existing group
'sudo gpasswd -d ____ _____(the new group added)' - used to remove the added group from the maingroup
'sudo groupdel _______' - to delete the entire group
'tail /etc/group' - to view how many groups exists in last 10

# History commands

'history' - shows previously used commands
'!____(34 numbers assigned for commands)' - this will show which command was there in that numeric value
' sudo apt update' - the space before the command means this command will notbe stored in history


# Commands to redirect the output
'ls -l > file.txt' - creates a new file and overwrites the existing file
'ls -l >> file.txt' - does not over write but appends the file
'cat file.txt | sort | uniq' - sorts number of lines 
'cat ls -l | grep file'
'cat file.txt | grep -v file.txt'
'cat file.txt | grep -v file.txt > ______(new_file.txt)'
'ls -l | wc - 1'
'ls -l | wc'
'ls -l /etc | wc -1'
