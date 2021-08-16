# Developing

## Intro

there are 2no main strands of internal software development:

- Standalone Development
  - Software that is developed independently of a piece of software. This software can interface
    the core MF software (by passing data between the apps) but does not have direct access to the software API's.
  - Typically runs on the jupyter server.
    - Ad-hoc jupyter notebooks for a given job.
    - Standalone Apps built using Voila and ipywidgets.

- Software Automation
  - pyRevit
    - pyRevit is used to automate Revit processes. It is described as RAD (Rapid Application Development),
      making it fast to build utility scripts the Revit application.
  - IES VEscripts
  - Rhino + Grasshopper + Python (currently Light and Air only)
  
## Genreal Best Practice

### Comments

https://stackoverflow.blog/2021/07/05/best-practices-for-writing-code-comments/

## Standalone Development

Within this paradigm, apps and packages are developed on the developers machine and deployed to the practice on the
JupyterHub server. Whilst packages can be developed anywhere, it is suggested to match the server deployment as
closely as possible.

### [Configure development environment](developing-envsetup.md)

### Conda / Mamba for managing package requirements

covered in more detail in "packaging".
During development of an App it is typical to use an inflated conda environment that contains more than what is explicitly required for the app.
See [manage-environments](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).
Use "mamba" as a drop-in replacement for "conda" by installing in your base conda env:

```bash
conda activate base
conda install -c conda-forge mamba
```

When packaging the app care is then taken to ensure only the packages that are required are listed as dependencies.

Environment variables can also be specified within a conda environment. 
see [work-with-variables](https://anaconda-project.readthedocs.io/en/latest/user-guide/tasks/work-with-variables.html#adding-a-variable).

### Standard development libraries for different tasks

| task                | package    | description                                                                                                                |
| ------------------- | ---------- | -------------------------------------------------------------------------------------------------------------------------- |
| filepath operations | pathlib    | always use pathlib for filepath operations. avoid using filepath strings. this ensure parity between linux and windows os. |
| object models       | pydantic   | [objectModels](objectModels.md)                                                                                            |
| python sql orm      | sqlalchemy |                                                                                       |

### User interfaces and visual experience

The jupyter ecosystem has a rich selection of packages that can be used to make high-quality front-ends.

| package      | description                                                                                                           |
| ------------ | --------------------------------------------------------------------------------------------------------------------- |
| voila        | converts a jupyter notebook (.ipynb) into a standalone app                                                            |
| ipywidgets   | core widget library with common UI components                                                                         |
| ipydatagrid  | fast, performant datagrid, featuring: filters, cell editing, cell rendering, etc.                                     |
| bqplot       | 2D plotting library based on the "The Gramma of Graphics". Facilitates customisable complex interactions.             |
| altair       | 2D plotting library based on the "The Gramma of Graphics". Python binding of vegalite. Excellent for simple plotting. |
| plotly       | Plotting library. Generally prefer the above, but plotly also very good! Supports 3D plotting.                        |
| ipycytoscape | widget enabling interactive graph visualization                                                                       |
| ipygany      | 3D visualisation widget                                                                                               |
| pydeck       | 3D visualisation widget built using deck.gl                                                                           |
|              |                                                                                                                       |

### Accessing the J:\drive

When using the JupyterHub server the a folder called /jobs is mounted onto the root repo.
When developing on WSL, it is possible to replicate this as follows:

i think there is a way to do ^ using wsl direct also.

## Software Automation

add brief description here


