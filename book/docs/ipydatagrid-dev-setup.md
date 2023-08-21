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

For example, let's say we change the function in `js/utils.ts`:

```typescript
export function getBackgroundColor(index = 0, opacity = 1) {
    return getCSSColor('--ipydatagrid-layout-color' + index, opacity);
  }
```

to this 

```typescript
export function getBackgroundColor(index = 0, opacity = 1) {
    "red";
  }
```

We check this change by rebuilding and seeing whether this is shown in JupyterLab.

Before building ensure that you are in the root directory!

Install with yarn first:

```bash
yarn install
```

To build:

```bash
yarn run build
```

Note that `yarn run` will look in the `package.json` file for the relevant entry.
For example, this is a snippet from the `package.json` in ipydatagrid root directory:

```json
  "scripts": {
    "build": "jlpm run build:lib && jlpm run build:nbextension && jlpm run build:labextension",
    "build:dev": "jlpm run build:lib && jlpm run build:nbextension && jlpm run build:labextension:dev",
    "build:labextension": "jupyter labextension build .",
    "build:labextension:dev": "jupyter labextension build --development True .",
    "build:lib": "tsc",
    "build:nbextension": "webpack --mode=production --no-devtool",
    "build:widget-examples": "cd widget-examples/basic && webpack --mode=production",
    "build:all": "jlpm run build:labextension && jlpm run build:nbextension && jlpm run build:widget-examples",
    "clean": "rimraf dist && jlpm run clean:lib && jlpm run clean:labextension && jlpm run clean:nbextension",
    "clean:lib": "rimraf lib",
    "clean:labextension": "rimraf ipydatagrid/labextension",
    "clean:nbextension": "rimraf ipydatagrid/nbextension/index.*",
    "lint": "eslint 'js/**/*.{js,ts}' --quiet --fix",
    "prepack": "jlpm run build:labextension && jlpm run build:nbextension",
    "test": "jest --verbose",
    "watch": "npm-run-all -p watch:*",
    "watch:lib": "tsc -w",
    "watch:nbextension": "webpack --watch",
    "watch:labextension": "jupyter labextension watch ."
  },
```

`yarn run build` will run the `build` script above.

## Running Gelata Tests

Change directory to `ui-tests-ipw8`:

```bash
cd ui-tests-ipw8
```

Install with yarn first:

```bash
yarn install
```

Install project dependencies:

```bash
npm install
```

Then install playwright using

```bash
npx playwright install
```


