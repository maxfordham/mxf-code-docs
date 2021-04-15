# Intro

Max Fordham is using code to: streamline workflows, develop robust engineering tools, communicate insight from data and create an ongoing feedback loop from lessons learnt.

This drive came from a desire to "stop re-inventing the wheel". This statement has 2-fold implications to internal software development:

1. By creating internally developed code we are formally recording common engineering processes that are observed on many projects
2. Many of the technical answers to the problems that we face exist in the external world in the form of open-source code. Use it! (The caveat to this is to as few dependencies as practical and give preference to open-source projects with active communities / well-resourced backers.)

This documentation sets out Max Fordham's development environment and tools / workflows / packages that should be used to ensure consistency.

Code development within engineering generally falls into 1 of the 2 categories:

- standalone internally developed tools
- software automation (i.e. pyRevit, IES VEscripts, Rhino + Grasshopper + Python)

As a general rule, any tools that has potentially general use (i.e. outside of a specific software package) should be developed independently of our software tools. Software automation scripts can then be made to connect data to these independent tools (an example of this is scheduling: the schedules are generated from the JupyterHub, but can be supplied data from the Revit model).