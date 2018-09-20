Creating a shell based on Python:
Obj:
You should write your shell in C or Python. We strongly recommend you write your shell in Python 3.

You do not have write a tokenizer from scratch for this lab. 

Your shell must terminate when it reaches an EOF, otherwise it will hang in the test script. To manually send one, you can use Ctrl+D to send an EOF to your shell. C-c C-d will most likely work in Emacs as well.

If the PS1 environment variable is set, your shell should use its value as its prompt instead of "$ ".



This program works by starting a while loop, begins a prompt for the user '$ '.
The user will enter a command:
'$ '
'$ ls' -will display contents in current directory
'$ CTRL-D' - the EOF that will exit the program: CTRL-D is the EOF
'$ exit' - The initial while loop asking for the prompts will find this with the list and just exit immediately
'$ wc osShell.py > text.txt' - will redirect the word count into a file called text.txt, if it already exists then it will continue writing

that will be evauluated for 3 different functions

cmd_1:
	Will create a fork first the check if it worked correctly then attempt exec the program
	from user input as a list then go into a loop to check directories to attempt to run the program
	This function does all the simple commands such as ls, sort, pwd and tell the user what the process is doing at the moment.
cmd_2::
	Similar to cmd_1 but with the option of '>' redirect, this will redirct the output to a file that the user will enter. The program removes the '>' and then try the redirect.
	The redirect creates a fork, then opens our file for 'w'. Then attempt to run the program to write.

cmd_pipe:
	This program gave me the most trouble, the program is suppose to pipe for read and write then fork. The child then runs a cmd_1 that opens another fork that returns the command that was inputted into the program. I had issues with a bad file descriptor, it would run the first command but not the pipe, and then exclude my prompt. I was not able to have this program work properly and am still confused on how this works.

change_dir:
	This program was made to help change directories, the cmd_1 could not change directories so I read the man on the changdir and online sources.It tries to find the path and returns and error if the the path was not found.
	
	\
I'm pretty sure I could have combined the all three of my main functions into one, I was not able to finish the piping correctly. I think it works by adding additional if statements. Those statements would be deciding if an file needed to be open or if the list from the commands needed to be doing a sinlge command or a pipe.
