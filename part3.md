# Linux Transition Guide Part 3: Learning the Terminal
## Intro
Don't panic after seeing that title; this part is going to be nice and easy. You are going to learn some nice, short commands, and learn how to install (and uninstall) packages.
## What this part will cover
- Essential commands
- Managing packages with a package manager
## Learning the terminal
### Moving around directories
What? What's a terminal? Calm down, you're only going to be typing like 20 letters total. Open up the popup menu in the bottom left, search for terminal, and open it. You should see a window come up that shows `username@hostname:~$`.

![Empty terminal](assets/term1.png)

> Note that I usually different terminal, a differnt window manager, and a different shell. I usually use the 'fish' shell, but I am using an online terminal emulator (terminux.live) for these examples that is almost identical to the one that you will be using.

 Now, type in `ls`. This lists all files and directories at the current directory, which is currently your home directory, as shown by the ~. You should see an output with some directories such as Documents, Downloads, Videos, Pictures, etc. 
 
 ![ls command](assets/term2.png)

 There should be some hidden directories, too. All hidden directories start with a period, such as `.local`. To view all files and directories including hidden ones, run `ls` with the -a flag: `ls -a`. To go in to one of these directories, use the `cd` command followed by the directory. Let's go into the Documents folder with `cd Documents`. Note that everything in Linux is case sensitive. If you ever want to get the full absolute path of where you are, use `pwd`, which prints the working directory, which in this case is `/home/user/Documents`. Note that `~` can be used instead of `/home/user`.

![cd and pwd command](assets/term3.png)

### Managing files
Now if you run `ls`, nothing should show up because your documents folder is empty. Let's change that. Use the command `touch` to make a file. Let's make one called `beans.txt`. If you think you can figure out how to make the file, go ahead. If you're stumped, the command is `touch beans.txt`. Easy, right? 



Type `cd ..` to go up a directory, back to ~. Now, try `cat Documents/beans.txt`. This is using a relative path. Now let's try using an absolute path. Go back into Documents with `cd Documents`, then make a new file in the Downloads directory with `~/Downloads/beans3.txt`. If you were to run `/Downloads/beans3.txt` (without the ~), that would be a relative path and would try to make the file in `~/Documents/Downloads/beans3.txt`. Now to edit one of these files, use the editor built into the Linux kernel, nano. Make sure that you are in `~/Documents`