# Linux Transition Guide Part 3: Learning the Terminal
## Intro
Don't panic after seeing that title; this part is going to be nice and easy. You are going to learn some nice, short commands, and learn how to install (and uninstall) packages.
## What this part will cover
- Essential commands
- Managing packages with a package manager
## Learning the terminal
### Moving around directories
What? What's a terminal? Calm down, you're only going to be typing like 20 letters total. You can almost always use GUI applications for everything that commands do, but it is always nice to know some of these just in case. Open up the popup menu in the bottom left, search for terminal, and open it. You should see a window come up that shows `username@hostname:~$`.

![Empty terminal](assets/term1.png)

> Note that I usually different terminal, a differnt window manager, and a different shell. I usually use the 'fish' shell, but I am using an online terminal emulator (terminux.live) for these examples that is almost identical to the one that you will be using.

 Now, type in `ls`. This lists all files and directories at the current directory, which is currently your home directory, as shown by the ~. You should see an output with some directories such as Documents, Downloads, Videos, Pictures, etc. 
 
 ![ls command](assets/term2.png)

 There should be some hidden directories, too. All hidden directories start with a period, such as `.local`. To view all files and directories including hidden ones, run `ls` with the -a flag: `ls -a`. To go in to one of these directories, use the `cd` command followed by the directory. Let's go into the Documents folder with `cd Documents`. Note that everything in Linux is case sensitive. If you ever want to get the full absolute path of where you are, use `pwd`, which prints the working directory, which in this case is `/home/user/Documents`. Note that `~` can be used instead of `/home/user`.

![cd and pwd command](assets/term3.png)

### Managing files
Now if you run `ls`, nothing should show up because your documents folder is empty. Let's change that. Use the command `touch` to make a file. Let's make one called `beans.txt`. If you think you can figure out how to make the file, go ahead. If you're stumped, the command is `touch beans.txt`. Easy, right? 

Type `cd ..` to go up a directory, back to ~. Now, try `cat Documents/beans.txt`. The `cat` command basically spits out the contents of the file. In this case, it will output nothing. `Documents/beans.txt` is using a relative path. Now let's try using an absolute path. Go back into Documents with `cd Documents`, then make a new file in the Downloads directory with `~/Downloads/beans2.txt`. If you were to run `cat Downloads/beans2.txt` (without the ~), that would be a relative path and would try to read the file in `~/Documents/Downloads/beans3.txt`. Now to edit one of these files, you can use the editor built into the Linux kernel called nano. Make sure that you are in `~/Documents` first, then type in `nano beans.txt`. It should open up an editor window. Type in anything you want, I did "Hello World!". Hit ctrl+o then enter to save, and ctrl+x to exit. Now if you do `cat beans.txt`, you should see something like this:

```bash
[user@bean-machine Documents]$ cat beans.txt
Hello, World!
```

Now to remove the file, use the `rm` command. Be careful with this one!

```bash
[user@bean-machine test]$ ls
beans.txt
[user@bean-machine test]$ rm beans.txt
[user@bean-machine test]$ ls
[user@bean-machine test]$ 
```

To make a directory (what is otherwise called a folder), use the `mkdir` command.

```bash
[user@bean-machine Downloads]$ mkdir test
[user@bean-machine Downloads]$ cd test
[user@bean-machine test]$ ls
[user@bean-machine test]$ mkdir test-subfolder
[user@bean-machine test]$ ls
test-subfolder
[user@bean-machine test]$ rm test-subfolder
rm: cannot remove 'test-subfolder': Is a directory
[user@bean-machine test]$ rm -rf test-subfolder
```

To remove a directory, use the `rm` command with the -rf flag. Again, be **very** careful with this! Some people try to troll noobs by telling you to run `sudo rm -rf ~/`, which deletes your entire home directory. **NEVER RUN THAT COMMAND!**

### Other commands
To execute a script, use `./path-to-script.sh`.

```bash
[user@bean-machine test]$ ./install.sh
```

To make a script executable, use the `chmod` command with +x.

```bash
[user@bean-machine test]$ chmod +x install.sh
```

### About the superuser
You should almost always be logged in to your session with a normal user, which has permission to change anything in that user's home directory (anything under `/home/user` or `~/`). The superuser or root user can modify anything. You should never run your session as the superuser, as it can introduce many security risks. Besides, most distros don't even expose the option to do so by default anyway. If you need to run a command as a superuser to, for example, edit a file that is outside of your home directory or install a package using your package manager, you can grant elevated permissions to a command by prefixing it with `sudo`. For example, if you do not have permission to edit `/etc/example/config.json`, you would need to use `sudo nano /etc/example/config.json`. Remember to use sudo wisely and understand the commands that you are running!

Lastly, if you are ever stumped about what a command does, prefix it with `man`, short for manual. You may need to install the man package manually, but it is a helpful tool if your web browser is too slow to look stuff up.

## Installing your first package
Now to make your system actually useful. First, we will install a package using `apt`, then you will open the GUI store to get one in a more simple and easy manner.

Open your terminal once again and type in `sudo apt install fastfetch`.