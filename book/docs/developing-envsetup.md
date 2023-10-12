
# Standalone Development

- [Standalone Development](#standalone-development)
  - [Introduction](#introduction)
  - [Instructions](#instructions)
    - [Hardare Config](#hardare-config)
    - [Install WSL2](#install-wsl2)
    - [Install Ubuntu2004](#install-ubuntu2004)
    - [Install an additional Linux subsystem (if required in future)](#install-an-additional-linux-subsystem-if-required-in-future)
    - [Install Miniconda](#install-miniconda)
    - [Mount mf internal conda channel](#mount-mf-internal-conda-channel)
    - [Mount J:\drive onto Linux WSL](#mount-jdrive-onto-linux-wsl)
    - [Mounting MF internal conda channel and J:\drive on startup](#mounting-mf-internal-conda-channel-and-jdrive-on-startup)
    - [create conda envs](#create-conda-envs)
    - [launch a juptyer lab session](#launch-a-juptyer-lab-session)
    - [launch a session with VS Code](#launch-a-session-with-vs-code)

## Introduction

Below are instructions about how to configure a development machine. Ideally they should
be followed exactly, to ensure that tests etc. are reproducible across development team
members.

Given that the final resting place of standalone tools is the Linux JupyterHub server,
we try to make the development environment on the users machine as close to this as
it can be.

## Instructions

__Notes__

- FDIR_SOFTWARE_REMOTE={{ servers.mffileserver.FDIR_SOFTWARE_REMOTE }} is where installer files for dev software is currently stored.
- WK = Windows Key
- install VSCode to the default install location

### Hardware Config

follow steps in this article:
- https://mashtips.com/enable-virtualization-windows-10/
and make sure Hyper-V is enabled. you don't have to mess with the BIOS settings.


### Install Ubuntu on wsl

```cmd
wsl --help  # view help
wsl --install -d Ubuntu  # install command
```

#### Creating new user in the distribution

setup new user as `jovyan`. 

### Setting Up SSH To Access Repositories on Max Fordham GitHub

1. Run

```bash
ssh-keygen
```
	
	This will create a public (id_rsa.pub) and private key (id_rsa) in `/home/jovyan/.ssh'
	
2. Copy the public key onto GitHub user's SSH keys

	Run
	
```bash
cat /home/jovyan/.ssh/id_rsa.pub
```
	
	to show the public key. Copy it from the command window.

	- Then go to GitHub and click on your personal account. 
	- Under the "Access" section there is "SSH and GPG keys".
	- Click on that, add a name for the key, paste in the public key, and save.

3. Permanently add SSH key to user agent

```bash
nano ~/.ssh/config
Host github.com
	IdentityFile ~/.ssh/id_rsa
```

4. Finally set up the git config by filling in email and name:

```bash
git config --global user.email "you@example.com"
```

```bash
git config --global user.name "Your Name"
```

You should now be able to access the repositories on Max Fordham LLP, assuming that you are a member of the organisation.

### Install Mambaforge

[micromamba-installation](https://mamba.readthedocs.io/en/latest/micromamba-installation.html#install-script)

```sh
"${SHELL}" <(curl -L micro.mamba.pm/install.sh)

# ^ press enter for default setup
```

add some bash aliases

```
nano .bash_aliases
# paste
alias start='mnt/c/windows/explorer.exe'
alias mamba='micromamba'
alias conda='micromamba'
# cntrl+X to leave
```

Restart wsl for the miniconda installation to take effect.

### Mount J:\drive onto Linux WSL - NO LONGER REQUIRED

WK wsl

```bash
sudo mkdir /home/jovyan/jobs
```

```bash
sudo mount -t drvfs '\\barbados\jobs' /home/jovyan/jobs
```

Note that the mounting will have to be performed each time on startup so we will add a mounting script in the next step.

### Mounting MF internal conda channel and J:\drive on startup - NO LONGER REQUIRED

We don't want to have to mount these two directories each time we boot up our system, so we will make it so these commands are run
automatically on start up.

1. Change directory to /etc/profile.d
    ```bash
    cd /etc/profile.d
    ```
2. Create a shell file
    ```bash
    sudo touch mount_folders.sh
    ```
3. Open up mount_folders.sh in the text editor 
    ```bash
    sudo nano mount_folders.sh
    ```
4. Now copy the code from below and paste into text editor by right clicking on the mouse.
    ```bash
	DIR_CONDA="/mnt/conda-bld/"
	FILE_CONDA="/mnt/conda-bld/linux-64"

	DIR_JOBS="/home/jovyan/jobs"
	FILE_JOBS="/home/jovyan/jobs/J4321"

	if [ ! -d "$FILE_CONDA" ]; then
	  # Take action if $FILE_CONDA does not exist. #
	  sudo mount -t drvfs '\\barbados\apps\conda\conda-bld' /mnt/conda-bld
	  echo "Mounting ${DIR_CONDA}."
	fi

	if [ ! -d "$FILE_JOBS" ]; then
	  # Take action if $FILE_JOBS does not exist. # 
	  sudo mount -t drvfs '\\barbados\jobs' /home/jovyan/jobs
	  echo "Mounting ${DIR_JOBS}."
	fi

	cd /mnt/c/engDev/git_mf
    ```
5. Press CTRL - X and you will be prompted with whether you want to save. Press Y to save and then click enter to confirm the file name to save as. 
Then this will exit out of the nano editor. 

6. Add windows explorer to your linux bash_aliases (this means you can `start fnm.txt` to open a file or `start .` to open the folder in explorer.
    ```bash
    sudo nano ~/.bash_aliases
	alias start='/mnt/c/windows/explorer.exe'
    ```

That's it! Now when you open WSL on start-up, it will prompt you for your password to mount both conda-bld and jobs (if they are not already mounted).

### create conda envs

best practice is that every package / repo should have an environment file that defines its own requirements. 
environments should be as small as they can be. 

### Install some handy CLI tools

Firstly, update the repository cache.

```bash
sudo apt update
```

Then run install commands

```bash
python -m pip install rich-cli
sudo apt-get install ripgrep
sudo apt install tree
```

```{note}
tree is useful for viewing directory structures in linux.
```

### launch a juptyer lab session


### launch a session with VS Code
