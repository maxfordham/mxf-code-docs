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

### Hardare Config

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
set UBUNTU_INSTALLER_FPTH=C:\engDev\Ubuntu_2004.2020.424.0_x64\install.tar.gz
wsl --import ubuntu_2004_jovyan %LINUX_IMAGE_DIR% %UBUNTU_INSTALLER_FPTH%
```

### Install Miniconda

WK wsl

```bash
$cd /home
$sudo wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
$chmod +x Miniconda3-latest-Linux-x86_64.sh
$./Miniconda3-latest-Linux-x86_64.sh
# note. should install here: /home/jovyan/miniconda3
# note. when prompted: Do you wish the installer to initialize Miniconda3, by running conda init? [yes|no]
# $yes
```

### Mount mf internal conda channel

WK wsl

```bash
mkdir /mnt/conda-bld
sudo mount -t drvfs '{{ servers.mffileserver.FDIR_CONDA_BUILD }}' /mnt/conda-bld
# ^ note. this currently doesnt persist between session so you have to do it everytime
conda config --add channels file:///mnt/conda-bld
conda config --add channels conda-forge
```

### Mount J:\drive onto Linux WSL

WK wsl

```bash
mkdir /home/jovyan/jobs
sudo mount -t drvfs '{{ servers.mffileserver.FDIR_JDRIVE }}' /home/jovyan/jobs
# ^ note. this currently doesnt persist between session so you have to do it everytime
```

### create conda envs

WK wsl

```bash
#  install mamba
conda install mamba -n base -c conda-forge -y
#  create env
mamba create -n mf_base -c conda-forge jupyterlab voila xeus-python pandas numpy markdown pydantic dacite ipysheet ipyfilechooser xmltodict plotly altair altair_saver halo pyyaml jupytext click nodejs openpyxl tabulate watchdog xlsxwriter pip xlsxtemplater mf_file_utilities mfom -y
#  activate 
conda activate mf_base
#  add pip only installs
pip install ipyaggrid mydocstring pipreqs
```

### launch a juptyer lab session

WK wsl

```bash
cd /mnt/c/engDev/git_mf
# ^note. maybe should move over to the linux mount...
jupyter lab
```

copy the ip into a browser for a Jupyter Lab session.

### launch a session with VS Code
