# Packaging

- __conda-bld__: back-end code / repos are built into conda repositories that can be imported into various environments
- __pip__: pip packages can be built from conda packages for use with VEScripts or pyRevit
- __repo2docker__: repo2docker is used to build docker images of front-end repos for user-interface tools

## conda-build

### folder structure

- refer to the following cookiecutters
  - [cookiecutter-pypackage-conda](https://github.com/michaelaye/cookiecutter-pypackage-conda)
    - `J:\J4321\DigitalDesignTeam\CodeDev\cookiecutter_condapypackage`
    - `J:\J4321\DigitalDesignTeam\CodeDev\cookiecutter_condarecipe`
- refer to the following mf repos
  - [xlsxtemplater](https://github.com/gunstonej/xlsxtemplater)
  - [mffileutilities](https://github.com/buckettt/mffileutilities)

### Version Control

- __Semantic versioning__ to be used for version control of ongoing development work.
[https://semver.org/](https://semver.org/)
- __Git tags__ to be used to track Semantic Versioning.
- When tagging releases in a version control system, the tag for a version MUST be "X.Y.Z" e.g. "3.1.0". 
[ref](https://stackoverflow.com/questions/2006265/is-there-a-standard-naming-convention-for-git-tags)
- use verioneer.py and _version.py found in the cookiecutter folder-structures and in [xlsxtemplater](https://github.com/gunstonej/xlsxtemplater). This will automatically make the version make with the git tag when building.

### conda-build - a generic example from WSL

create a conda build environment: 

```bash
conda create --name base_mf --clone base
mamnba install conda-build
```

example below for package called `mypackage`.

```bash
# mount the network location
mkdir /mnt/conda-bld
sudo mount -t drvfs '{{ servers.mffileserver.FDIR_CONDA_BUILD }}' /mnt/conda-bld

# add conda mf conda channel if not already there... 
# this allows mf internal pacakges to be included in the build
conda config --add channels file:///mnt/conda-bld 

# run command from local root dir of conda package (requires a conda.recipe folder in the dir)
conda activate base_mf  # assuming base_mf env has conda build installed
conda build conda.recipe

# note. the cmd above builds into the default --croot
# default = `\\wsl$\Ubuntu-20.04\home\gunstonej\miniconda3\envs\base_mf\conda-bld`
# can specify a custom `croot` as follows:
# `--croot /mnt/c/engDev/channel`

# publish to mf conda channel
# manually copy and paste from:
# {{croot}}/linux-64/`mypackage*.tar.bz2`
# --> 
# {{ servers.mffileserver.FDIR_CONDA_BUILD }}
# convert
conda convert --platform all /mnt/conda-bld/linux-64/mypackage*.tar.bz2 --output-dir /mnt/conda-bld
# update index
conda index /mnt/conda-bld

# install package into your conda env
conda install mypackage
# or 
conda install -c file:///mnt/conda-bld mypackage
```

### Install internal conda packages - Windows

to install conda packages into windows you need to expose the conda channel (again, in the future this will be done by mamba-boa).

```bat
:: navigate to Z:\conda\conda-bld
:: create a python server of the directory on your local host
Z:\conda\conda-bld> python -m http.server

:: open a new cmd

```bat
mamba install mypackage -c http://localhost:8000/
```

## pip

To build from pip, make sure your directory is set up with the necessary configuration files. 

You will need a __setup.cfg__ for static metadata and potentially a __<span>setup.py</span>__ for dynamic metadata. 

You can also define a __requirements.txt__ to state the packages required. 

Please note that a __<span>MANIFEST.in</span>__ will be needed to state any files that need to be included in the build. For example, we will need to add "include requirements.txt" so that this file can be read from the build location.

Now, check pip is installed in the current environment. If not, install using mamba. We can use the environment base_mf for this.

Then perform updates: 

```
python3 -m pip install --upgrade build pip setuptools wheel
```

After this, go to the directory where the repository lives and run:

```
python3 -m build
``` 

The package (filetype tar.gz) will be dumped in the "dist" folder which will be created within the directory of repository.

To check the the package we can try install it by running:

```
pip install FPATH
```

where FPATH is the path to the tar.gz file.

Reference: https://packaging.python.org/en/latest/tutorials/packaging-projects/

### pip from conda package

simpler, pip packages can be built from conda packages.  
this will be useful for shared packages between: Revit-pyRevit, IES-VEScripts and other python tools.
In both Revit-pyRevit and IES-VEScripts a pip directory can be simply appended to the `sys.path` to make external packages available to these scripts.

pip packages can be created from conda packages as follows (ask Owen for help if req);

```bat
:: as before, expose conda channel on localhost
Z:\conda\conda-bld> python -m http.server

pip install mypackage --target=Z:\pip --extra-index-url = http://localhost:8000/
:: --target = shared pip folder, this can be appended to `sys.path`
:: --extra-index-url = where to look for mypackage
```

## [Repo2Docker](https://repo2docker.readthedocs.io/en/latest/usage.html)

Repo2docker is a tool that builds a docker image (and associated environment) from a Git repository.
Max Fordham's jupyter hub server has the [tljh-repo2docker](https://github.com/plasmabio/tljh-repo2docker) plugin installed
and configured making it simple to add new environments / apps. It works in the same way as [mybinder](https://mybinder.org/).

### Configuring the docker image

The docker image is configured by the [config_files](https://mybinder.readthedocs.io/en/latest/using/config_files.html).
In the simplest (most common) case, the only file that is required is "environment.yml" file to specify the conda environment.
The "postbuild" can be used to add jupyter extensions.

e.g. the config files for the TM59ArchetypeResultsViewer App
![config_repo2docker](images/config_repo2docker.png)

### Adding the J:\drive

The Max Fordham TLJH has been configured to add a "jobs" folder to the root repository when a server or app is launched.
This gives easy access to read and write files from the J:\drive.

## Troubleshooting

config_build_config.yml:

```yaml 
python:
  - 3.9
  - 3.8

numpy:
  - 1.19
```

Noting issue when building mfschedule. Numpy 1.16 was causing issues when building from conda.recipe. When removed, build was successful.