# mfcode_docs

**Max Fordham Engineering Development Best Practice**

This documentation aims to provide high-level, non-verbose notes outlining Max Fordham's engineering software development infrastructure.
Links to external sources and standards to describe the approach are preferred where possible.
The intended audience are those contributing / maintaining internal development tools, or external parties / collaborators interested in our approach.
Code snippets are encouraged.

We stand on the shoulders of giants. See below for key packages on which we rely.

:::{panels}
:container: +full-width text-center
:column: col-lg-4 px-2 py-2
:card:

**[packaging](packaging.md)**
^^^
conda build used to build conda packages to conda-forge feedstock recipe.
![conda-forge](images/conda-forge-icon.png)
---

**[deploying](deploying.md)**
^^^
the jupyterhub server is deployed to an internal server using ansible playbooks.
![ansible](images/ansible-icon.png)

---
**[jupyterhub](deploying.md)**
^^^
a server hosted jupyterhub gives all Max Fordham users access to notebooks and apps. repo2docker creates docker images of apps and notebook environments.
![jupyterhub](images/jupyterhub-icon.png)
![repo2docker](images/repo2docker-icon.png)

---
**[apps](developing.md)**
^^^
standalone apps are made from notebooks using voila. they are deployed to the server using repo2docker. 
![voila](images/voila-icon.png)

---
**[pyrevit](developing.md)**
^^^
Revit software is customised using pyRevit - a RapidApplicationDevelopment environment and python wrapper to the Revit API.
![pyrevit](images/pyrevit-icon.png)

---
**[api](developing.md)**
^^^
FastAPI is used to create server hosted APIs. This templates interactions with databases and gives Revit or IES scripts access to 
other MF automation tools without complex user installs. 
![fastapi](images/fastapi-icon.png)

---
**[databases](databases.md)**
^^^
postgresSQL is the preferred database tool. SQLalchemy uses to manage python interface.
![postgresql](images/postgresql-icon.png)
![sqlalchemy](images/sqlalchemy-icon.png)

:::