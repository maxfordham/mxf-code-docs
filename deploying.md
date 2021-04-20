# Deploying

## JuptyerHub Server

The general development environment is a JupyterHub server (Linux Ubuntu 20.04) that is accessible to everyone and independent of any other software. Conda / Mamba is used for package management (see later) meaning there is robust version control and record of previous versions.

Refer to:
[jupyterhub-maxfordham](https://github.com/gunstonej/jupyterhub-maxfordham)
for the repo developed by QuantStack that automates processes on the JupyterHub server using ansible playbooks

## Building repo2docker apps that use internal (private) conda repository's

The jupyterhub is configured to use the repo2docker tool:
https://github.com/gunstonej/jupyterhub-maxfordham/blob/master/docs/environments.md

This creates a docker image with the required environment for the contents of the repo to run.
Generally, it downloads packages from conda-forge to do this, but for internally developed private
conda pacakges we need to expose the packages to the server and repo2docker tool as it is building.

It's not possible to mount barbados onto stbarts and reference the channel in the conventional sense because it doesn't get exposed in the docker instances created when running repo2docker. Instead the process is to start a local web server which the docker instances can access. 

**To do this:**

**Start the conda-channel server**

SSH into StBarts using your preferred method (Putty or SSH)

Mount the network location

```
mkdir /mnt/conda-bld
sudo mount -t drvfs '\\barbados\apps\conda\conda-bld' /mnt/conda-bld
```

Start the webserver on the conda channel - it's important that you do this on St Barts. Doing it from your local machine isn't sufficient. 

```
cd /mnt/conda-bld
python -m http.server
```

Check that the server is working by visiting <St Barts IP>:8000 and you should see the MF Conda Channel Index page. St Barts IP should be 10.10.30.125

**Build the repo2docker image**

Then in your repo2docker repsitory binder/environment.yml add the reference to the MF Channel like so. 

```
channels:
      - defaults
      - conda-forge
      - http://10.10.30.125:8000/conda-bld
dependencies:
  - my_really_cool_mf_conda_package
```

​    

Then build the image in the conventional way. Once this has complete you can then kill the local server running in conda-bld since it is only used during the installation process. 

**And finally**

```
Live
Laugh
Love
```

