# ipydatagrid Development Setup

## Prerequisite Installation

Ensure that both npm and yarn are installed into your linux distribution:

```bash
sudo apt install npm
```

```bash
sudo apt install yarn
```

If you're having issues with the above not running then try:

```bash
sudo apt update
```

## ipydatagrid test environment

Firstly, clone the repository:

```bash
git clone git@github.com:bloomberg/ipydatagrid.git
```

Create the development environment:

```bash
mamba env create -f test-environment.yaml
```

and activate the environment:

```bash
conda activate ipydatagrid-test
```

Then install ipydatagrid itself:

```bash
pip install -ve .
```

Enable the development install for JupyterLab:

```bash
jupyter labextension develop . --overwrite
```

## Making Changes and Rebuilding

So we can make changes to the typescript files and rebuild to see these
in JupyterLab.

For example, let's say we change in 


## Running Gelata

Change directory to `ui-tests-ipw8`:

```bash
cd ui-tests-ipw8
```

Install playwright using

```bash
npx playwright install
```
