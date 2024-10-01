# Documentation

## Branch Names

The branch names on jupyterhub-maxfordham must not contain any full-stops, otherwise the "Launch" button does not working correctly.

For example, ipypdt repo is used for the equipment-schedule-maker. If we were to create a branch from the tag 0.1.4 (in git), we would
name the branch equipment-schedule-maker-v0_1_4.

## Sphinx Extensions

- [nbsphinx-link](https://nbsphinx-link.readthedocs.io/_/downloads/en/stable/pdf/)

## Sphinx github changelog extension

We can use https://github.com/ewjoachim/sphinx-github-changelog to add the Github releases log to our documetation.

To do this, create a releases.rst file and add it to the toc.yml file.

Then add this into the relases.rst file so that the log is added:

`
.. changelog::
    :changelog-url: https://your-project.readthedocs.io/en/stable/#changelog
    :github: https://github.com/you/your-project/releases/
    :pypi: https://pypi.org/project/your-project/
`

The most import link to add is the github releases link. The other changelog-url and pypi are optional.

If the github repository is private then you must create a github token so that sphinx can gain read access. Otherwise, no data will be retrieved.

Generate a new token here: https://github.com/settings/tokens

The token then must be added to the _config.yml:

`
sphinx_github_changelog_token = "..."
`

Don't forget to add the extension too!

`
extensions = [
    ...,  # your other extensions
    "sphinx_github_changelog",
]
`

Note: Having the github token in the config file is not very safe as you can imagine so we can call it in as an environment variable.
Currently, the only way we've figured out how to do this is by explictly editing the conf.py file.
At the top of py file, `import os`, and then update:

`
sphinx_github_changelog_token = os.environ.get("GITHUB_TOKEN")
`

where GITHUB_TOKEN is a set environment variable in the environment you are running the sphinx build command from.

In WSL, set the environment variable by doing:

`
export GITHUB_TOKEN=...
`

Now the problem with editing the conf.py is that we are supposed to generate it from the _config.yml but unfortunately, adding the python code to the yml file doesn't translate
properly to the generated conf.py

There is an open github issue on this: https://github.com/executablebooks/jupyter-book/issues/1709
