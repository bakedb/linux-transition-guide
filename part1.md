# Linux Transition Guide Part 1: Introducing You to Linux
## Intro
This guide is meant to be as un-scary as possible, avoiding things like extensive use of the terminal and complicated UEFI/BIOS settings. Also, I wrote this guide for people who were transitioning from Windows, but I would say that everything in this guide will work on a non-Apple Silicon Mac. The only thing I could see being different is getting the live OS image to boot. If you are on anything but an Intel Mac (from around 2005-2020) or a computer currently running Windows, this guide is not for you.
## Why You Should Trust Me
I have used Linux since 2021 starting with a Raspberry Pi 3B (not the fastest computer ever) running Raspbian or what was called Raspberry Pi OS at the time. **FACTCHECK** Since then, I switched away from Windows completely and have not looked back. I shouldn't be your number one resource for everything Linux related (you can look at the sources document to see some good ones), but I think I have used it enough to teach someone the basics.
## A Quick History Lesson
Don't worry, this will be quick.

Linux was created by a dude named Linus Torvalds back in the 90s. It was based off of UNIX and the GNU Project, so many people refer to it as GNU/Linux. One of the first widespread distributions (or distros) of Linux was Slackware. Today there are many popular distros such as Debian, Ubuntu, Arch, OpenSUSE, and more.

See, I told you it would be quick.
## Why Linux?
Linux is:

- Yours (you control everything)
- Free
- Open Source (you can freely look at, modify, and distribute the code)
- Often faster than Windows
- Could run on a toaster
- Community built and quality tested (any bugs can be patched out by anyone)
- Choose when you update

Windows is:

- Not yours (you have very little control over the OS; for example, you can't easily control what telemetry data Microsoft can see)
- Not free
- Proprietary (you cannot legally modify or distribute the code)
- Often slower than Linux due to unstoppable background processes, unnecesary telemetry data, etc.
- Very strict hardware requirements (such as required TPM2, which not even some modern computers have)
- AI coded slop that breaks after every update (Microsoft is proud to say that 30% of their codebase was made by AI as of a few weeks ago)
- Forces updates
## What Uses Linux?
- Your TV
- Your Android Phone
- Your Mac (uses BSD, which is kind of like Linux but a bit different)
- Your car
- The computers in North Korea (they use a custom made Linux distro called RedStar OS)
- 5% of consumer machines worldwide
## Explaining Distributions
**GRAB GRAPHIC FROM WIKIPEDIA FOR DISTROS**
Linux comes in many different distributions, most often called distros. The most common is probably Debian. If you have ever heard about Linux, you have also probably heard about Ubuntu, which is based on Debian. Other distros based on Debain include Kali, Mint, and Linux Lite. Another common one is Fedora. Linus Torvalds himself uses Fedora. There aren't many distros based on it, especially compared to Debian, although the gaming-focused distro Bazzite is based on Fedora. Lastly, Arch Linux is a pretty common distro, and my personal favorite. Normal Arch Linux is very confusing to set up for inexperienced users, as the ISO just puts you in a command prompt with nothing but some info at the top of the screen and a "Welcome to Arch Linux!" message. However, distros such as Manjaro, Garuda, and CachyOS are based on Arch and have the normal GUI setup that most are used to. The standout feature of Arch Linux and its derivitaves is that it is rolling release, which means that there isn't an "Arch Linux version 19.04" or "version 2025.10.02" release; everything that the system relies on is updated when it needs an update. All you need to do is a quick  `sudo pacman -Syu` to fully update the system, and you can restart your computer whenever you want.