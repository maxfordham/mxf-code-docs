
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
and make sure Hyper-V is enabled.


### Install WSL2

Step4 from this guide:
- https://docs.microsoft.com/en-us/windows/wsl/install-win10#manual-installation-steps

For the current install files, create a folder `C:\engDev\wsl_install`, and use the following bat script:


`wsl_update.bat`  

```cmd
@echo off

:: EDIT 
:: ||||||||||||||||||||||||||||||||||||||||||||||
set SOFTWARE_FILENAME=wsl_update_x64.msi
:: ||||||||||||||||||||||||||||||||||||||||||||||

REM ----------SET-------------
set FDIR_SOFTWARE_REMOTE= {{ servers.mffileserver.FDIR_SOFTWARE_REMOTE }}
set FDIR_SOFTWARE_LOCAL=%~dp0
set SRC=%FDIR_SOFTWARE_REMOTE%\%SOFTWARE_FILENAME%
set DSTN=%FDIR_SOFTWARE_LOCAL%\%SOFTWARE_FILENAME%
:: ---------------------------

echo ---------VERIFY-----------
echo FDIR_SOFTWARE_REMOTE: %FDIR_SOFTWARE_REMOTE%
echo FDIR_SOFTWARE_LOCAL: %FDIR_SOFTWARE_LOCAL%
echo SOFTWARE_FILENAME: %SOFTWARE_FILENAME%
echo SRC: %SRC%
echo DSTN: %DSTN%
echo ---------------------------

REM ----------RUN---------------
if not exist %DSTN% call xcopy %SRC% %DSTN%*
pause
```

### Install Ubuntu2004

Ubuntu_2004.2020.424.0_x64.appx

For the current install files use the following bat script:

`get_ubuntu.bat`  

```cmd
@echo off
:: EDIT 
:: ||||||||||||||||||||||||||||||||||||||||||||||
set SOFTWARE_FILENAME=Ubuntu_2004.2020.424.0_x64.appx
:: ||||||||||||||||||||||||||||||||||||||||||||||

REM ----------SET-------------
set FDIR_SOFTWARE_REMOTE={{ servers.mffileserver.FDIR_SOFTWARE_REMOTE }}
set FDIR_SOFTWARE_LOCAL=%~dp0
set SRC=%FDIR_SOFTWARE_REMOTE%\%SOFTWARE_FILENAME%
set DSTN=%FDIR_SOFTWARE_LOCAL%\%SOFTWARE_FILENAME%
:: ---------------------------

echo ---------VERIFY-----------
echo FDIR_SOFTWARE_REMOTE: %FDIR_SOFTWARE_REMOTE%
echo FDIR_SOFTWARE_LOCAL: %FDIR_SOFTWARE_LOCAL%
echo SOFTWARE_FILENAME: %SOFTWARE_FILENAME%
echo SRC: %SRC%
echo DSTN: %DSTN%
echo ---------------------------

REM ----------RUN---------------
if not exist %DSTN% call xcopy %SRC% %DSTN%*
pause
```

unzip wtih 7zip (or rename .appx --> .zip) and run the .exe inside.
when asked to set-up a username, call it "jovyan" (jovyan being a resident of Jupyter!).
This is the default username used by JupyterHub; and there the docker images that are built
on the JupyterHub server, so using this username means that the filepaths are the same on the
user environment as they are on the server.

### Install an additional Linux subsystem (if required in future)

`build_ubuntu.bat`  

```cmd
:: assumes unzipped Ubuntu installer is saved in C:\engDev\wsl_install
set LINUX_IMAGE_DIR=C:\engDev\wsl_install
set UBUNTU_INSTALLER_FPTH=C:\engDev\wsl_install\Ubuntu_2004.2020.424.0_x64\install.tar.gz
wsl --import ubuntu_2004_jovyan %LINUX_IMAGE_DIR% %UBUNTU_INSTALLER_FPTH% --version 2
```

#### Set new distribution (ubuntu_2004_jovyan) as default distribution

To set ubuntu_2004_jovyan as the default distribution when launching wsl, run this command:

```cmd
wsl -s ubuntu_2004_jovyan
```

Note that we can check this by listing the existing distributions:

```cmd
wsl -l
```


#### Creating new user in the distribution

Firstly, we must run the specified distribution using:

```cmd
wsl -d ubuntu_2004_jovyan
```

We are now in the distribution as the user "root".

To add a user we will run:

```bash
adduser jovyan
```

Go through the steps of adding a password and any information you wish (can leave it blank if you want). 
Then say that the information is correct... well if it is correct.

Now we need to enable sudoer privileges for our new user, jovyan:

```bash
adduser jovyan sudo
```

When we launch wsl, we want to have jovyan as the default user. We do this by adding the default to the wsl config file:

```bash
tee /etc/wsl.conf <<_EOF
[user]
default=jovyan
_EOF
```

Finally, logout of wsl with the bash:

```bash
logout
```

And then use the wsl shutdown command so that the changes take effect:

```cmd
wsl --shutdown ubuntu_2004_jovyan
```

That's it! Next time wsl is launched, the ubuntu_2004_jovyan distribution should be the default distribution, 
and jovyan should be the default user with all the required permissions.

### Install Miniconda

Run WSL again

```bash
wsl
```

cd to home
```bash
cd /home
```

Get Miniconda shell script
```bash
sudo wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

Change access permissions to shell script so we can install.
```bash
sudo chmod +x Miniconda3-latest-Linux-x86_64.sh
```

Install Miniconda
```bash
./Miniconda3-latest-Linux-x86_64.sh
# note. should install here: /home/jovyan/miniconda3
# note. when prompted: Do you wish the installer to initialize Miniconda3, by running conda init? [yes|no]
# $yes
```

Restart wsl for the miniconda installation to take effect.

### Mount mf internal conda channel

WK wsl

```bash
sudo mkdir /mnt/conda-bld
```

```bash
sudo mount -t drvfs '\\barbados\apps\conda\conda-bld' /mnt/conda-bld
```

Adding channels:

```bash
conda config --add channels file:///mnt/conda-bld
```

```bash
conda config --add channels conda-forge
```

### Mount J:\drive onto Linux WSL

WK wsl

```bash
sudo mkdir /home/jovyan/jobs
```

```bash
sudo mount -t drvfs '\\barbados\jobs' /home/jovyan/jobs
```

Note that the mounting will have to be performed each time on startup so we will add a mounting script in the next step.

### Mounting MF internal conda channel and J:\drive on startup

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

As a default env, it is suggested to setup "jlaunch" below - this is a lightweight jupyter environement that has nb_conda_kernels
installed, allowing any other conda environment to run from a single jupyter instance. Any jupyter extension that contains built code 
must be installed into the jlaunch environment. 

WK wsl

```bash
#  install mamba
conda install mamba -n base -c conda-forge -y
#  create env for launching jupyterlab. 
#  install anything that requires a built jupyterlab extension into this environment
mamba create -n jlaunch -c conda-forge "python>3.8,<3.10" "jupyterlab>3.1" jupyterlab-spellchecker voila ipywidgets ipydatagrid ipyvuetify watchdog plotly matplotlib altair nb_black jupytext jupyterlab-lsp python-lsp-server theme-darcula
conda activate
mamba install -n jlaunch nb_conda_kernels #  this allows any conda env to be run from jlaunch
#  activate 
conda activate jlaunch
```

### Install some handy CLI tools

```bash
python -m pip install rich-cli
sudo apt-get install ripgrep
sudo apt install tree
```

tree is useful for viewing directory structures in linux.

### launch a juptyer lab session

WK wsl

```bash
cd /mnt/c/engDev/git_mf
# ^note. maybe should move over to the linux mount...
jupyter lab
```

copy the ip into a browser for a Jupyter Lab session.

### launch a session with VS Code
