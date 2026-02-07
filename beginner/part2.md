# Linux Transition Guide Part 2: Installing Linux
## Intro
Now for the hardest part (but still pretty easy if you are patient): actually getting a system up and running. You will need a few things for this part, so get up and get them before you start.
## What this part will cover
- Getting a Linux ISO
- Installing Linux on your system
## What you will need
- A computer to install Linux on (this guide is for x86_64 devices)
- A USB drive (4 GB or bigger, 8 GB reccomended)
- An internet connection
## Getting the ISO
The ISO file is what we are going to be booting the target computer on to get into the live environment and install Linux. Now you have to make a descision. I will give you 2 distros to choose between, and the differences between them. Based on those differences, you are going to choose which distro you are going to use.
### Fedora
- Is always up to date
- Flatpak-first (Flatpaks are packages that work across any distro, and are often managed through a nice, understandable GUI)
- The package manager, DNF, is readable and friendly
- SELinux protects you from breaking stuff
- The installer is simple and straightforward

Perfect for:
- People coming from a different operating system
- People who want to learn Linux without being overwhelmed
### Debian
- The package manager, APT, is simple and predictable
- Structure is clean and logical
- You learn the difference between stable/testing/unstable
- You learn how to fix things when software is older

Perfect for:
- People who want to manage everything themselves
- People who want to deeply understand Linux while still having simple tools to do so
- People who want a very stable, long-term system
### Conclusion
Fedora is a very "welcome to Linux" experience, while Debian is a "teaching you to be a sysadmin" experience. Debian will give you a few "there is no reason that this should be broken" moments if you aren't careful, but it does give you a lot of learning experience in return, and once you get it working, it will most likely keep on working if you don't touch it.

This guide was originally written to be used with Linux Mint, but I have gone back on that after realizing that Mint is a very "temporary" distro that you will immediately want to switch off of once you try something else. However, if you *really* want to see the guide with Mint, you can go [here.](part2_mint.html)

And now this is the part where the Fedora and Debian paths will split. You can go to the [Fedora](part2_fedora.html) or [Debian](part2_debian.html) page to continue.