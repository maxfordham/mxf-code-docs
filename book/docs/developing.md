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
  
## General Best Practice

### Python formatting style - use [__Black__](https://github.com/psf/black)

- [install black](https://anaconda.org/conda-forge/black): `mamba install -c conda-forge black`
- in jupyterlab use [nb_black](https://github.com/dnanhkhoa/nb_black)
  - [install nb_black](https://anaconda.org/conda-forge/nb_black): `mamba install -c conda-forge nb_black`
  - add to 1st cell `%load_ext lab_black`
- in vscode format on save as per this article: [setting-up-python-black-on-visual-studio-code](https://marcobelo.medium.com/setting-up-python-black-on-visual-studio-code-5318eba4cd00)

annoyingly it will need configuring for every conda environment. 

#### How to use underscores

[the-special-meaning-of-underscores-in-python](https://betterprogramming.pub/the-special-meaning-of-underscores-in-python-9ceaaeb41007)

In classes i think this is particularly pertinent... underscores can denote methods that we expect the user to call or not e.g. 

```
class MyClass:
	def __init__(self, ...):
		pass
		
	def _init_class(self):
		self._privatemethod()
	
	def usermethod(self, ...):
		pass
		
	def _privatemethod(self, ...):
		pass
		
obj = MyClass()
obj.usermethod(x) #  this encouraged
obj._privatemethod(x) #  this discouraged
```

### Comments

https://stackoverflow.blog/2021/07/05/best-practices-for-writing-code-comments/

### Docstrings

Use google style guide format. 

- https://google.github.io/styleguide/pyguide.html
- https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

Use Python Docstring Generator if using VS Code. 

- https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring

### Managing defaults, optional and required variables

- something should be a default if in production the value is normally fixed / should have default behaviour
- minimum required dependent variables should normally be non-default args / params to indicate to the user that these values are required to be set

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

###  Jinja for templating 

```python

from jinja2 import Template

template = """{
    "hostname": "{{ hostname }}",
    "name_server_pri": "{{ name_server_pri }}",
    "name_server_sec": "{{ name_server_sec }}",
    "ntp_server_pri": "{{ ntp_server_pri }}",
    "ntp_server_sec": "{{ ntp_server_sec }}",
}"""

data = {
    "hostname": "core-sw-waw-01",
    "name_server_pri": "1.1.1.1",
    "name_server_sec": "8.8.8.8",
    "ntp_server_pri": "0.pool.ntp.org",
    "ntp_server_sec": "1.pool.ntp.org",
}

j2_template = Template(template)

print(j2_template.render(data))
```

### Functools

functools is awesome. 

functools.partial useful for quickly wrapping a function with known args and kwargs. you loose the __name__ property though. if thats problematic do similar with functools.wraps.

## Software Automation

add brief description here


