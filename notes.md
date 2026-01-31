

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
