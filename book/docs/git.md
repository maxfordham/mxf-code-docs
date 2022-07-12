# Git

## Github

is great! 

but being cloud-hosted you do need to mess about with access tokens. 

https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token#creating-a-token

## Git Workflow

This shows our git workflow which we believe to be the best practice when working on
new functionality in code repositories.

![Git workflow](images/git_workflow.png)

## Merging branches

Let's say that we have been working on a branch called "Adding Tests", then we merge this to dev by doing:

- in local dev repo
- switch/checkout to Adding Tests branch
- pull changes
- switch/checkout to dev branch 
  - select merge changes to Adding Tests branch
- push dev to git server (git dev now up-to-date)
