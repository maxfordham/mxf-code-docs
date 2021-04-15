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
- When tagging releases in a version control system, the tag for a version MUST be "vX.Y.Z" e.g. "v3.1.0". 
[ref](https://stackoverflow.com/questions/2006265/is-there-a-standard-naming-convention-for-git-tags)
- use verioneer.py and _version.py found in the cookiecutter folder-structures and in [xlsxtemplater](https://github.com/gunstonej/xlsxtemplater). This will automatically make the version make with the git tag when building.

### conda-build - a generic example from WSL

example below for package called `mypackage`.

```bash
# mount the network location
mkdir /mnt/conda-bld
sudo mount -t drvfs '\\barbados\apps\conda\conda-bld' /mnt/conda-bld

# add conda mf conda channel if not already there... this allows mf internal pacakges to be included in the build
conda config --add channels file:///mnt/conda-bld 

# run command from local root dir of conda package (requires a conda.recipe folder in the dir)
conda activate base_mf  # assuming base_mf env has conda build installed
conda build conda.recipe

# note. the cmd above builds into the default --croot
# default = `\\wsl$\Ubuntu-20.04\home\gunstonej\miniconda3\envs\base_mf\conda-bld`
# can specify a custom `croot` as follows:
# `--croot /mnt/c/engDev/channel`

# publish to mf conda channel
# copy and paste the croot/linux-64 files `mypackage*.tar.bz2` from into `\\barbados\apps\conda\conda-bld\linux-64`
conda convert --platform all /mnt/conda-bld/linux-64/mypackage*.tar.bz2
conda index /mnt/conda-bld

# install package into your conda env
conda install mypackage
# or 
conda install -c file:///mnt/conda-bld mypackage
```

### Install internal conda packages - Windows

to install conda packages into windows you need to expose the conda channel (again, in the future this will be done by mamba-boa).

```{cmd}
:: navigate to Z:\conda\conda-bld
:: create a python server of the directory on your local host
Z:\conda\conda-bld> python -m http.server

:: open a new cmd
```

```cmd
mamba install xlsxtemplater -c http://localhost:8000/
```

## pip

simpler, pip packages can be built from conda packages.  
this will be useful for shared packages between: Revit-pyRevit, IES-VEScripts and other python tools.
In both Revit-pyRevit and IES-VEScripts a pip directory can be simply appended to the `sys.path` to make external packages available to these scripts.

pip packages can be created from conda packages as follows (ask Owen for help if req);

```cmd
:: as before, expose conda channel on localhost
Z:\conda\conda-bld> python -m http.server

pip install mypackage --target=Z:\pip --extra-index-url = http://localhost:8000/
:: --target = shared pip folder, this can be appended to `sys.path`
:: --extra-index-url = where to look for mypackage
```
