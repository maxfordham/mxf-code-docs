
# mfcode_docs

**Max Fordham Engineering Development Best Practice**

This documentation aims to provide high-level, non-verbose notes outlining Max Fordham's engineering software development infrastructure.
Links to external sources and standards to describe the approach are preferred where possible.
The intended audience are those contributing-to and maintaining internal development tools, or external parties and collaborators interested in our approach.
Code snippets are encouraged.

**We stand on the shoulders of giants**. Our software is built on robust, high-quality opensource packages, and we are proud to share the work that we produce with the opensource community.
When writing code there are always many solutions to a problem;
we standardise the technologies we use for a given task to ensure a consistent approach across projects. See below for key technologies on which we rely.



:::{panels}
:container: +full-width text-center
:column: col-lg-4 px-2 py-2
:card:


**[software-automation](software-automation.md)**
^^^
 we develop scripts to automate tasks using the open APIs available within our core softwares.

[![pyrevit](images/pyrevit-icon.png)](https://www.notion.so/pyrevitlabs/pyRevit-bd907d6292ed4ce997c46e84b6ef67a0 " pyRevit (with lowercase py) is a Rapid Application Prototyping (RAD) environment for Autodesk Revit. It helps you quickly sketch out your automation and add-on ideas, in whichever language that you are most comfortable with, inside the Revit environment and using its APIs.")
[![grasshopper+ladybug-tools](images/grasshopper+ladybug-tools-icon.png)](https://www.food4rhino.com/en/app/ladybug-tools " visual coding and python scripting environment inside McNeel Rhino. good for early-stage concept design development and analysis.")
[![IES-vescripts](images/IES-vescripts-icon.png)](https://www.iesve.com/software/python-scripting " You can use the VE Python API to create your own customised scripts to: automate reports, data input, parametric simulations and many other tasks.")

---


**[authoring-tools]()**
^^^
 The majority of our work can be done in Jupyter. All Engineers have access to managed common environments on the
JupyterHub server. 


[![jupyter](images/jupyter-icon.png)](https://jupyter.org/ "interactive coding and in-line report production")
[![vscode](images/vscode-icon.png)](https://code.visualstudio.com/ "state of the art IDE for software development")

---


**[frontend]()**
^^^
To simplify the number of tools our developers need to interact with, we produce the majority of frontend apps using ipywidgets and the many visualisation libraries Jupyter supports. For Revit automation we also use WPF forms.

[![voila](images/voila-icon.png)](https://github.com/voila-dashboards/voila "Voilà turns Jupyter notebooks into standalone web applications.")
[![plotly](images/plotly-icon.png)](https://plotly.com/python/getting-started/ "simple but powerful interactive web visualisation")
[![altair](images/altair-icon.png)](https://altair-viz.github.io/ "declarative 2D plotting that wraps around vega d3 schemas")
[![bqplot](images/bqplot-icon.png)](https://github.com/bqplot/bqplot "plotting library build with jupyter widgets. allows for complex interactions with ipywidgets.")

---


**[packaging](packaging.md)**
^^^
 Perhaps the most important step to well structured ongoing development.Code is packaged into conda packages allowing portability and simple version control.


[![conda-forge](images/conda-forge-icon.png)](https://conda-forge.org/ "community maintained collection of opensource packages and template specifcation for new packages.")
[![conda](images/conda-icon.png)](https://docs.conda.io/en/latest/conda-build.html "tool for building conda packages, maintained by Anaconda.")
[![mamba](images/mamba-icon.png)](https://docs.conda.io/en/latest/conda-build.html "Mamba is a fast, robust, and cross-platform package manager; it is a reimplementation of the conda package manager in C++.")

---


**[deploying](deploying.md)**
^^^
 A server hosted jupyterhub gives all Max Fordham users access to jupyter notebooks and apps.  the server is setup, deployed and updated using ansible playbooks. the work was done by Quantstack, and utilises a previous set-up they configured [plasmabio](https://docs.plasmabio.org/en/latest/overview/index.html)see [jupyterhub-maxfordham](https://github.com/gunstonej/jupyterhub-maxfordham) for MF setup and configuration. 

[![ansible](images/ansible-icon.png)](https://docs.ansible.com/ " Ansible playbooks are used to automate the setup, configuration and update of remote servers from a local machine. This is used to deploy our JupyterHub server.")
[![jupyterhub](images/jupyterhub-icon.png)](https://jupyterhub.readthedocs.io/en/stable/ " JupyterHub is the best way to serve Jupyter notebook for multiple users. It can be used in a class of students, a corporate data science group or scientific research group. ")
[![repo2docker](images/repo2docker-icon.png)](https://repo2docker.readthedocs.io/en/latest/index.html " repo2docker fetches a repository (from GitHub, GitLab, Zenodo, Figshare, Dataverse installations, a Git repository or a local directory) and builds a container image in which the code can be executed. The image build process is based on the configuration files found in the repository.")

---


**[databases](databases.md)**
^^^
 Insight can be extract from structured data. our automation tools create structured data that is passed to databases for global review and analysis.

[![postgresql](images/postgresql-icon.png)](https://www.postgresql.org/ " PostgreSQL is a powerful, open source object-relational database system with over 30 years of active development that has earned it a strong reputation for reliability, feature robustness, and performance. It is used for production-grade tools.")
[![sqlite](images/sqlite-icon.png)](https://www.sqlite.org/index.html " SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine. It is used for some standalone apps and prototyping.")

---


**[backend-tools]()**
^^^
Making object-models and defined datastructures is the basis of solid engineering tools. Utilising FastAPI packages can be turned into server hosted APIs that are accessible to any machine with no install.And SQLAlchemy handles creation and interations with SQL tables.

[![sqlalchemy](images/sqlalchemy-icon.png)](https://www.sqlalchemy.org/ " SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL. Table definitions and relations are developed in SQL alchemy, as well as data-serialisation with pydantic.")
[![pydantic](images/pydantic-icon.png)](https://pydantic-docs.helpmanual.io/ "Define how data should be in pure, canonical python; validate it with pydantic.Used to create object definitions that feed: databases, calculation tools and documentation.")
[![FastAPI](images/FastAPI-icon.png)](https://fastapi.tiangolo.com/ "FastAPI framework, high performance, easy to learn, fast to code, ready for production.It makes maintainence, upgrade and integration of production packages with software scripts simple asthe packages and environment is installed on the server.")

---


**[external-experts]()**
^^^
for help with the heavy lifting and deployment we call in the pros.Quantstack are one of the core Jupyter developers and are active members of the opensource community.Working with them gives us confidence in our approach to software development,whilst concentrating on what we're best at: Engineering.

[![quantstack](images/quantstack-icon.png)](https://quantstack.net/ "for help with the heavy lifting and deployment we call in the pros.Quantstack are one of the core Jupyter developers and are active members of the opensource community.Working with them gives us confidence in our approach to software development,whilst concentrating on what we're best at: Engineering.")

---


**[documentation](documentation.md)**
^^^
 Without clear documentation code risks becoming a black-box. When writing python code we use the Google Style Guide: [pyguide](https://google.github.io/styleguide/pyguide.html), [mit-pyguide](https://drake.mit.edu/styleguide/pyguide.html), [sphinx-example](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).this allows for autodocs using sphinx, or for more simple docs using [mydocstring](https://github.com/ooreilly/mydocstring).Jupyter Book is used to pull it all together.

[![jupyter-book](images/jupyter-book-icon.png)](https://jupyterbook.org/intro.html "Jupyter Book is an open source project for building beautiful, publication-quality books and documents from computational material.")
[![sphinx](images/sphinx-icon.png)](https://www.sphinx-doc.org/en/master/ "Jupyter book utilises sphinx for many of its functions. Sphinx can also be used to auto-doc docstrings written in the Google Style Guide (MF standard).")

---

 :::