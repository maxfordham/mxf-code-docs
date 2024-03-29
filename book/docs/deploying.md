# Deploying

## JuptyerHub Server

The general development environment is a JupyterHub server (Linux Ubuntu 20.04) that is accessible to everyone and independent of any other software. Conda / Mamba is used for package management (see later) meaning there is robust version control and record of previous versions.

Refer to:
[jupyterhub-maxfordham](https://github.com/gunstonej/jupyterhub-maxfordham)
for the repo developed by QuantStack that automates processes on the JupyterHub server using ansible playbooks

### Accessing the Server

install putty.

you need the following credententials to SSH / Putty onto the StBarts server:

|           |                                   |
| --------- | --------------------------------- |
| host name | {{ servers.jupyterhub.hostname }} |
| port      | {{ servers.jupyterhub.port }}     |
| username  | {{ servers.jupyterhub.username }} |
| password  | {{ servers.jupyterhub.password }} |

these can be found in your secret _secret_config.toml file.

### Check server performance

```bash
htop #  for system monitoring information / server load
```

### Update if required

[ref](https://askubuntu.com/questions/196768/how-to-install-updates-via-command-line)

```bash
sudo apt update        # Fetches the list of available updates
sudo apt upgrade       # Installs some updates; does not remove packages
sudo apt full-upgrade  # Installs updates; may also remove some packages, if needed
sudo apt autoremove    # Removes any old packages that are no longer needed
```

## Building repo2docker apps that use internal (private) conda repository's

The jupyterhub is configured to use the repo2docker tool:
https://github.com/gunstonej/jupyterhub-maxfordham/blob/master/docs/environments.md

This creates a docker image with the required environment for the contents of the repo to run.
Generally, it downloads packages from conda-forge, but for internally developed private conda
packages we need to expose the packages to the server and repo2docker tool as it is building.

It's not possible to mount barbados onto stbarts and reference the channel in the conventional sense because it doesn't get exposed in the docker instances created when running repo2docker.
Instead the process is to start a local web server which the docker instances can access.

**To do this:**

### SSS/ Putty onto the StBarts server

### mount the conda-build folder on the server

this only needs to be done after the server has been switched off, otherwise the mount will persist.

```bash
mkdir /mnt/conda-bld
sudo mount -t cifs -o user={{ mf.user }},password={{ mf.password }} servers.mffileserver.FDIR_CONDA_BUILD /mnt/conda-bld
```

### Start the conda-channel server

Start the webserver on the conda channel - it's important that you do this on St Barts. Doing it from your local machine isn't sufficient.

```bash
cd /mnt/conda-bld
python3 -m http.server
```

Check that the conda file-server is exposed by visiting:
'''{{ servers.jupyterhub.ip }}''' and you should see the MF Conda Channel Index page.

### Build the repo2docker image

Then in your repo2docker repsitory binder/environment.yml add the reference to the MF Channel like so. 

```bash
channels:
  - defaults
  - conda-forge
  - {{ servers.mffileserver.IP_TEMP_CONDA_FILESERVER }}
dependencies:
  - my_really_cool_mf_conda_package
```

__note__. currently
​
Then build the image in the conventional way. Once this has complete you can then kill the local server running in conda-bld since it is only used during the installation process.