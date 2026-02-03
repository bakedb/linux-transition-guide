# Linux Transition Guide Part 2: Installing Linux
## Intro
Now for the hardest part (but still pretty easy if you are patient): actually getting a system up and running. You will need a few things for this part, so get up and get them real quick right now before you start.
## What this part will cover
- Getting an ISO of Linux Mint
- Installing Linux Mint on your system
## What you will need
- A computer to install Linux Mint on (this guide is for x86_64 devices)
- A USB drive (4 GB or bigger)
- An internet connection
## Getting the ISO
The ISO file is what we are going to be booting the target computer on to get into the Mint live environment and install Linux. First, go to https://www.linuxmint.com/ and click on the "Download" button. ![Linux Mint download page](assets/linuxmintwebsite.png)
You are going to want to choose the top option, the Cinnamon Edition. ![Edition page](assets/cinnamonedition.png)
Then, scroll down and pick any one of the download mirrors. Any one of them is fine. Then, wait a few minutes for the file to download. While you are waiting, go to https://etcher.balena.io/ to download the tool that we will use to flash the USB drive to make it bootable. Just download the version for your system. ![Balena Etcher](assets/balenaetcher.png)

> I use something called Ventoy to boot multiple ISO files on a single USB stick, and I find it very convenient. If this sounds like something you would find useful, take a look at the docs here: https://www.ventoy.net/en/index.html

Now once you have both your flashing tool and the ISO downloaded, you can flash your USB stick. **Note that this will erase everything on it**, so don't blame me for any data loss. You have been warned.

![Balena Etcher Screen](assets/balenascreen.png)

Now all you have to do is insert your USB, open up Etcher, select the ISO file, select your USB drive, and flash it! It should just take a few minutes. Once it is done, we are ready to move on to the next step: booting into the live environment.