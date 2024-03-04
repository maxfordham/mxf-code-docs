
# Standalone Development

- [Standalone Development](#standalone-development)
  - [Introduction](#introduction)
  - [Prerequisite](#prerequisite)
  - [Instructions](#instructions)
    - [Install Ubuntu on WSL](#install-ubuntu-on-wsl)
    - [Set Up SSH To Access Repositories on Max Fordham GitHub](#set-up-ssh-to-access-repositories-on-max-fordham-github)
    - [Install Conda Package Manager](#install-conda-package-manager)
    - [Install some handy CLI tools](#install-some-handy-cli-tools)
    - [Install Visual Studio Code](#install-visual-studio-code)

## Introduction

Below are instructions about how to configure a development machine. Ideally they should
be followed exactly, to ensure that tests etc. are reproducible across development team
members.

Given that the final resting place of standalone tools is the Linux JupyterHub server,
we try to make the development environment on the users machine as close to this as
it can be.

## Prerequisite

Hyper-V should already be enabled on your laptop but if you are having issues then follow this article:
- https://mashtips.com/enable-virtualization-windows-10/

## Installation

### Install Ubuntu on WSL

```cmd
wsl --install -d Ubuntu
```

Create the new user as `jovyan` and set the password to something sensible.

Ensure that the WSL version of the distribution is set to version 2

```cmd
wsl --set-version Ubuntu 2
```

### Set Up SSH To Access Repositories on Max Fordham GitHub

1. Create an SSH key pair using the following

    ```bash
    ssh-keygen
    ```
	
    This will create a public `id_rsa.pub` and private key `id_rsa` in `/home/jovyan/.ssh` by default.
        
2. Copy the public key onto GitHub user's SSH keys
	
    To show the public key:

    ```bash
    cat /home/jovyan/.ssh/id_rsa.pub
    ```
        
    Copy it from the command window to your clipboard by highlighting the whole key and pressing CTRL+C.

    - Then go to GitHub and click on your personal account. 
    - Under the "Access" section there is "SSH and GPG keys".
    - Click on that, add a name for the key, paste in the public key, and save.
    - Authorise the key for the `Max Fordham` organisation. You must be a member of the organisation to do this.

3. Optional: Permanently add SSH key to user agent

    This step is only required if the file name of the SSH is something other than `id_rsa` or the other default names.

    ```bash
    nano ~/.ssh/config
    Host github.com
        IdentityFile ~/.ssh/id_custom_name
    ```

4. Finally set up the git config by filling in email and name:

    ```bash
    git config --global user.email "you@example.com"
    ```

    ```bash
    git config --global user.name "Your Name"
    ```

    You should now be able to access the repositories on Max Fordham LLP, assuming that you are a member of the organisation.

### Install Conda Package Manager

We utilise the conda package manager functionality through the following software: [miniforge](https://github.com/conda-forge/miniforge) 

To install miniforge, run the folllowing in WSL

```bash
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh
```

Restart WSL for the miniforge installation to take effect.

### Install some handy CLI tools

Firstly, update the repository cache.

```bash
sudo apt update
```

Then run install commands

```bash
python -m pip install frogmouth
sudo apt-get install ripgrep
sudo apt install tree
```

```{note}
tree is useful for viewing directory structures in linux.
```

It is also useful to add windows explorer to your linux bash_aliases. This means you can `start fnm.txt` to open a file or `start .` to open the folder in explorer.

```bash
sudo nano ~/.bash_aliases
alias start='/mnt/c/windows/explorer.exe'
```

Restart WSL for the above changes to take effect.

### Install Visual Studio Code

Download Visual Studio Code: https://code.visualstudio.com/download

Install VS Code by opening the downloaded `.exe`.

Once in VS Code, install the recommended extensions:

- WSL
- Python
- Jupyter
- GitHub Copilot
- Gitmoji
- Black formatter ([Setup Black Formatter](https://code.visualstudio.com/docs/python/formatting))
- Spell Check ([Change to British English](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker-british-english#:~:text=Enable%20British%20English%20Dictionary,or%20in%20just%20the%20Workspace.))

You should be all set up and ready to start coding! 🚀