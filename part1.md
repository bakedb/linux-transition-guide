# Linux Transition Guide Part 1: Introducing You to Linux
## Intro
This guide is meant to be as un-scary as possible, avoiding things like extensive use of the terminal and complicated UEFI/BIOS settings. Also, I wrote this guide for people who were transitioning from Windows, but I would say that everything in this guide will work on a non-Apple Silicon Mac. The only thing I could see being different is getting the live OS image to boot. If you are on anything but an Intel Mac (from around 2005-2020) or a computer currently running Windows, this guide is not for you.
## What this part will cover
- A bit of history
- Why you should use Linux
- Where you can find Linux in the wild
- Distributions
- Desktop Environments
## Why You Should Trust Me
I have used Linux since 2021 starting with a Raspberry Pi 3B (not the fastest computer ever) running Raspbian, or what had just been renamed to Raspberry Pi OS. Since then, I switched away from Windows completely and have not looked back. I shouldn't be your number one resource for everything Linux related (you can look at the sources document to see some good ones), but I think I have used it enough to teach someone the basics.
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
![Massive tree of Linux Distributions](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Linux_Distribution_Timeline.svg/500px-Linux_Distribution_Timeline.svg.png)
> By Andreas Lundqvist (initially), Muhammad Herdiansyah (continued), Fabio Loli (continued) - http://futurist.se/gldt/ (initially), https://github.com/konimex/linuxtimeline (continued), https://github.com/FabioLolix/LinuxTimeline (continued), GFDL 1.3, https://commons.wikimedia.org/w/index.php?curid=2556373

Linux comes in many different distributions, most often called distros.

<img src=https://www.debian.org/logos/openlogo.svg width=200 height=200>
<img src=https://assets.ubuntu.com/v1/a7e3c509-Canonical%20Ubuntu.svg width=200 height=200>
<img src=https://upload.wikimedia.org/wikipedia/commons/2/2b/Kali-dragon-icon.svg width=200 height=200>
<img src=assets/linuxlite.svg width=200 height=200>

> From left to right: Debian, Ubuntu, Kali, and Linux Lite.

The most common is probably Debian. If you have ever heard about Linux, you have also probably heard about Ubuntu, which is based on Debian. Other distros based on Debain include Kali, Mint, and Linux Lite. 

<img src=https://upload.wikimedia.org/wikipedia/commons/3/3f/Fedora_logo.svg width=200 height=200>
<img src=https://upload.wikimedia.org/wikipedia/commons/a/a7/Bazzite_Logo.svg width=200 height=200>

> From left to right: Fedora, Bazzie.

Another common one is Fedora. Linus Torvalds himself uses Fedora. There aren't many distros based on it, especially compared to Debian, although the gaming-focused distro Bazzite is based on Fedora. 

<img src=https://raw.githubusercontent.com/JotaRandom/archlinux-artwork/refs/heads/master/icons/archlinux-icon-crystal-128.svg width=200 height=200>
<img src=https://upload.wikimedia.org/wikipedia/commons/3/3e/Manjaro-logo.svg width=200 height=200>
<img src=https://cdn.jsdelivr.net/gh/homarr-labs/dashboard-icons/svg/garuda-linux.svg width=200 height=200>
<img src=https://upload.wikimedia.org/wikipedia/commons/b/b8/CachyOS_Logo.svg width=200 height=200>

> From left to right: Arch, Manjaro, Garuda, CachyOS

Lastly, Arch Linux is a pretty common distro, and my personal favorite. Normal Arch Linux is very confusing to set up for inexperienced users, as the ISO just puts you in a command prompt with nothing but some info at the top of the screen and a "Welcome to Arch Linux!" message. However, distros such as Manjaro, Garuda, and CachyOS are based on Arch and have the normal GUI setup that most are used to. The standout feature of Arch Linux and its derivitaves is that it is rolling release, which means that there isn't an "Arch Linux version 19.04" or "version 2025.10.02" release; everything that the system relies on is updated when it needs an update. All you need to do is a quick `sudo pacman -Syu` to fully update the system, and you can restart your computer whenever you want.

For simpliity and ease of use, this guide will show you how to use Fedora, which is derived from Ubuntu with Snap packages disabled (the most controvertial part of Ubuntu, as the Snap Store infrastructure is closed-source).

## What is a desktop environment?

Think of your Windows taskbar, macOS dock, notification center, settings menu, or menu bar as part of the desktop environment. I think Wikipedia describes it a bit better than me: 

> In computing, a desktop environment (DE) is an implementation of the desktop metaphor made of a bundle of programs running on top of a computer operating system that share a common graphical user interface (GUI), sometimes described as a graphical shell. 
>> (https://en.wikipedia.org/wiki/Desktop_environment)

Some of the most common desktop environments, commonly referred to as DEs, are KDE Plasma (my personal favorite), Cinnamon, GNOME, Xfce, LXQt, MATE, and Unity. A short explination of some of these will be given below. Note that this is in no way a comprehensive list. There are many, many DEs out there, just like there are distros. Also, even though a distro may come packaged with a certain DE (Ubuntu with GNOME and previously Unity, Mint with Cinnamon, Pop!_OS with COSMIC, etc.), that does not mean that you need to use a different distro to use another DE. DEs are packages, just like every other application on the system, and can be installed and uninstalled through the package manager.

### KDE Plasma
Plasma by default is pretty close to what you might be used to on Windows, with a popup menu in the bottom left, pinned applications on the taskbar, and a few widgets on the right. However, everything can be flipped on its head with the wide customizability. You can make Plasma look like macOS if you wanted to.

![KDE Plasma](https://upload.wikimedia.org/wikipedia/commons/5/52/KDE_Plasma_6.4.5_Dark.png)

Customizability: ★★★★

Ease of use: ★★★★

Stability: ★★★★

### Cinnamon
Cinnamon is the default DE on Linux Mint, and is quite comparable to KDE Plasma. It has a very gentle learning curve and is, again, quite similar to Windows.

![Cinnamon DE](https://upload.wikimedia.org/wikipedia/commons/a/ac/LinuxMint22-Wilma-English.png)

Customizability: ★★

Ease of use: ★★★★★

Stability: ★★★

### GNOME
GNOME is quite different compared to most of these; it does not use the normal taskbar layout by default. Instead, it has a dock at the bottom and a menu that comes up with a search bar at the top, the dock, and an application drawer if you scroll down if you press the meta key (the Windows key on most keyboards).

![GNOME](https://upload.wikimedia.org/wikipedia/commons/9/97/GNOME_Shell.png)
![GNOME](https://upload.wikimedia.org/wikipedia/commons/e/e0/GNOME_48.0_on_GNOME_OS.png)

Customizability: ★★

Ease of use: ★★★★★

Stability: ★★★

### Xfce, MATE, and LXQt
These three are pretty similar, but with some slight differences: Xfce is made to be lightweight and customizable, MATE is made as a continuation of the old GNOME 2 desktop, and LXQt is meant to be efficient and modern-looking, but is not as versatile as Xfce.

![Xfce](https://upload.wikimedia.org/wikipedia/commons/e/ed/XFCE_4.20.png)
![MATE](https://mate-desktop.org/gallery/1.26/english/mate-1.26_7.png)
![LXQt](https://upload.wikimedia.org/wikipedia/commons/2/29/LXQt_2.0.0_Ambiance_screenshot.png)

Customizability: ★★ - ★★★★

Ease of use: ★★★ - ★★★★

Stability: ★★ - ★★★★★

As you can see, desktop environments vary quite a lot in functionality and visuals. You will be using Cinnamon for now, but feel free to install another one later.

> **A note about getting GNOME'd:** A common thing that happens to people is installing a package that requires the GNOME shell (such as GDM, the GNOME greeter meant to replace SDDM or LightDM; we'll talk about greeters in part 2). This is especially a problem on Linux Mint and other Ubuntu-based distros, because when you install the GNOME shell on an Ubuntu-based system using apt (the Debian package manager), it pulls in the entire Ubuntu session, which is even more unnecesary stuff that you do not need. So if you ever find yourself in GNOME after a restart when you least expect it, this is probably what has happened. To reverse this, just uninstall the GNOME shell.

## Outro
Congrats, you have finished part 1! You now know the basics of Linux: a bit of history, distros, and desktop environments. You are now ready to move on to part 2 and get installing :3