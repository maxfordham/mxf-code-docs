
# Standalone Development

- [Standalone Development](#standalone-development)
  - [Introduction](#introduction)
  - [Prerequisite](#prerequisite)
  - [Instructions](#instructions)
    - [Install Ubuntu on WSL](#install-ubuntu-on-wsl)
    - [Set Up SSH To Access Repositories on Max Fordham GitHub](#set-up-ssh-to-access-repositories-on-max-fordham-github)
    - [Install Conda Package Manager](#install-mamba-package-manager)
    - [Install some handy CLI tools](#install-some-handy-cli-tools)
    - [Install Visual Studio Code](#install-visual-studio-code)

## Introduction

Below are instructions about how to configure a development machine. Ideally they should
be followed exactly, to ensure that tests etc. are reproducible across development team
members.

Given that the final resting place of standalone tools is the Linux JupyterHub server,
we try to make the development environment on the users machine as close to this as
it can be.

```{note}
A couple of steps below indicate "requires admin p/w". All other steps are to be done by the user.
```

## Prerequisite (requires admin p/w)

Hyper-V should already be enabled on your laptop but if you are having issues then follow this article:

- https://mashtips.com/enable-virtualization-windows-10/

## Installation

### Install Ubuntu on WSL (requires admin p/w)

```{danger}
couldn't get wsl working on a fresh install. 
to fix: https://github.com/microsoft/WSL/issues/9521#issuecomment-2385289848
```

```cmd
wsl --install -d Ubuntu
```

Create the new user as `jovyan` and set the password to something sensible you won't forget.

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

### Install [`pixi`](https://pixi.sh/latest/#installation) 

- [install](https://pixi.sh/latest/#installation)
  - `curl -fsSL https://pixi.sh/install.sh | bash` <-- check still current on install guide
- [enable autocomplete](https://pixi.sh/latest/#autocompletion)
  - `echo 'eval "$(pixi completion --shell bash)"' >> ~/.bashrc` <-- check still current on install guide


### Install other CLI tools

can also use [pixi](https://pixi.sh/latest/basic_usage/#use-pixi-as-a-global-installation-tool) to globally install useful tools.

```bash
pixi global install micromamba  # micromamba package manager
pixi global install gh  # github CLI
pixi global install starship  # shell autocompletion
pixi global install ripgrep  # searching text in files
pixi global install tree  # viewing directory structures in linux
pixi global install rich-cli  # pretty terminal file viewer
pixi global install harlequin  # terminal based sql workbench
pixi global install tiptip  # prettier `htop` system usage log
```

also note that there are many ways to do this. the most standard way it to use apt-get. 
e.g.

```bash
sudo apt update
sudo apt-get install ripgrep
sudo apt install tree
"${SHELL}" <(curl -L micro.mamba.pm/install.sh)  # micromamba
```

### apt update

run these periodically to stay up-to-date
```bash
sudo apt update
sudo apt upgrade
```

### setup repos for development

```bash
gh auth # follow authentification workflow
gh repo list maxfordham
gh repo clone maxfordham/digital-schedules

cd digital-schedules
gh issue list  --assignee "@me"  # view your issues
```

### Setup bash_aliases

It is also useful to add windows explorer to your linux bash_aliases. This means you can `start fnm.txt` to open a file or `start .` to open the folder in explorer.

```bash
sudo nano ~/.bash_aliases
alias start='/mnt/c/windows/explorer.exe'
alias mamba='micromamba'
```

Restart WSL for the above changes to take effect.

### Install Notepad ++

[notepad++](developing-notepadplusplus.md)

#### Customise

- https://github.com/Edditoria/markdown-plus-plus
- https://github.com/nea/MarkdownViewerPlusPlus

### Install Visual Studio Code

[vscode](developing-vscode.md) (install as user)
