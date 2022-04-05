# Documentation

## Branch Names

The branch names on jupyterhub-maxfordham must not contain any full-stops, otherwise the "Launch" button does not working correctly.

For example, ipypdt repo is used for the equipment-schedule-maker. If we were to create a branch from the tag 0.1.4 (in git), we would
name the branch equipment-schedule-maker-v0_1_4.

## Make Markdown Files Pretty in Notepad++

To make markdown files more readable in notepad++, we can install markdown markdown-plus-plus.

https://github.com/Edditoria/markdown-plus-plus

1. Open command prompt and run conda.
2. Activate mf_base and install nodejs:
	```
	mamba install nodejs
	```
3. Now change location to Notepad++:
	```
	cd %AppData%\Notepad++\
	```
4. Make a new directory for the language:
	```
	mkdir userDefineLangs
	```
5. Now change to that new location:
	```
	cd userDefineLangs
	```
6. Run markdown-plus-plus to create the laguange file:
	```
	npx markdown-plus-plus default
	```
7. Finally, open notepad++ and click on the "Language" tab. Then select "Markdown (Default)". 

## Format toml files in Notepad++

https://github.com/Theodor-Lindberg/NPP-TOML-Syntax


## Sphinx Extensions

- [nbsphinx-link](https://nbsphinx-link.readthedocs.io/_/downloads/en/stable/pdf/)