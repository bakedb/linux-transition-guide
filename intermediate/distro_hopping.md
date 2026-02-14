# Linux Transition Guide: Distro Hopping
No matter if you picked Debian or Fedora (or Mint for whatever reason, I won't judge... okay, maybe I will), you can always change distributions with little to no trouble. As long as you set seperate root (/) and home partitions when you were installing, switching should be a breeze.
## What this part will cover
- Preparing for a distro switch
- Switching distros
- A large list of distros and what they provide
## Preparing for your switch
Assuming that you have a seperate home directory, switching should just be as simple as installing the new distro on your root partition overwriting the old one, and assigning your home partition during installation. Note that not all distro installation processes allow you to set seperate home and root partitions or link in existing ones, but most do.

If you did not set a seperate home partiton, just back everything up to a USB drive or something and put it back after your are done installing.

> **Backups are important!** No matter if you set up a seperate home partition or not, if you have data that you care about, back it up! Better safe than sorry.

## What transfers across distros?
Assuming you transfered your home directory:
- Files (Documents, Downloads, Videos, etc.)
- Applications installed in the home partition (most are not by default)
- Configurations and other data for apps that were previously installed

For example, Firefox normally stores its configuration in `~/.var/app/org.mozilla.firefox/.mozilla` when installed as a Flatpak, and this location should be in your home partition. So, if you were to hop distros and install the Firefox Flatpak on your new installation, your config should transfer and you will have your old extensions, bookmarks, history, etc.

What does not transfer:
- Applications (but most data is saved. You just need to reinstall the application)
- Anything saved to root (/)

## A big list of distros
Below is a big list of Linux distributions that I think you might be interested in. The name is listed, then what it is based off of, the default DE, my short description of it, its use case, and my "should you try it", or SYTI, ranking (which assumes that your knowledge of Linux is as extensive as what was covered in the beginner section of the guide).
> If you want to look into more yourself, go to [https://distrowatch.com/](https://distrowatch.com/). There is a massive list of distributions there. Some that you have definitely heard of, and some that only like 2 people have probably ever used. It's a pretty interesting resource.

These are taken from some of the top entries of the Year 2025 Page Hit Ranking on DistroWatch.

### CachyOS
Base: Arch

Default DE: Multiple (you choose during installation)

Distro built for speed and hardware optimizations. Has a modified Linux kernel for maximum performance.

SYTI: Yes

### Linux Mint
Base: Ubuntu (Debian)

Default DE: Cinnamon

Other available flavors: Linux Mint Debian Edition (Debian-based instead of Ubuntu), MATE Edition, Xfce Edition

Made for beginners. Structured to be easy to understand. Some may consider it bloated (but pales in comparison to Windows bloat) with a lot of preinstalled stuff. Against Snap packages and the Snap Store.

SYTI: No, unless you are an absolute beginner (and there are still places that are just as good to start at)

### MX Linux
Base: antiX (Debian)

Default DE: Fluxbox, KDE Plasma, Xfce

Made with slower systems and systems like the Raspberry Pi in mind.

SYTI: Yes, if you have a less performant system

### Debian
Base: None

Default DE: You choose during setup, but GNOME is checked by default

Older distro that many others are based on. Known for being very stable. No extra bells or whistles.

SYTI: Yes, if you need a very stable system.

### EndeavourOS
Base: Arch

Default DE: Multiple (you choose during setup). Offline installer chooses KDE Plasma by default.

Other available flavors: Community spins with other window managers.

Terminal-centric with Nvidia drivers baked in.

SYTI: Yes, if you have an Nvidia GPU and want an Arch-based system that works out of the box.

This list is pretty incomplete. If you want to help it, you can PR additions at [Codeberg](https://codeberg.org/bkd/linux-transition-guide/src/branch/main/intermediate/distro_hopping.md) or [GitHub](https://github.com/bakedb/linux-transition-guide/blob/main/intermediate/distro_hopping.md).

<!--
Todo:
https://distrowatch.com/table.php?distribution=popos
https://distrowatch.com/table.php?distribution=manjaro
https://distrowatch.com/table.php?distribution=ubuntu
https://distrowatch.com/table.php?distribution=fedora
https://distrowatch.com/table.php?distribution=zorin
https://distrowatch.com/table.php?distribution=opensuse
https://distrowatch.com/table.php?distribution=elementary
https://distrowatch.com/table.php?distribution=nixos
https://distrowatch.com/table.php?distribution=garuda
https://distrowatch.com/table.php?distribution=kali
https://distrowatch.com/table.php?distribution=arch
-->