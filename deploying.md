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

{Owen please add!}