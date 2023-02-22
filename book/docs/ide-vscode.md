# VS Code

## Extending with extensions

```bash
# https://gist.github.com/joseluisq/4740e37a9f2358357381e308aa39c52d

# get list of extension
code --list-extensions | sed -e 's/^/code --install-extension /' > my_vscode_extensions.sh

# install extensions from file
bash my_vscode_extensions.sh
```

when I run the above I get the following: 

`my_vscode_extensions.sh`
```bash
code --install-extension alexcvzz.vscode-sqlite
code --install-extension bierner.markdown-mermaid
code --install-extension chrisjsewell.myst-lsp
code --install-extension darkriszty.markdown-table-prettify
code --install-extension DavidAnson.vscode-markdownlint
code --install-extension donjayamanne.githistory
code --install-extension DotJoshJohnson.xml
code --install-extension eriklynd.json-tools
code --install-extension ExecutableBookProject.myst-highlight
code --install-extension GitHub.copilot-nightly
code --install-extension GitHub.vscode-pull-request-github
code --install-extension Gruntfuggly.todo-tree
code --install-extension hbenl.vscode-test-explorer
code --install-extension littlefoxteam.vscode-python-test-adapter
code --install-extension mhutchie.git-graph
code --install-extension ms-python.isort
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
code --install-extension ms-toolsai.jupyter
code --install-extension ms-toolsai.jupyter-keymap
code --install-extension ms-toolsai.jupyter-renderers
code --install-extension ms-toolsai.vscode-jupyter-cell-tags
code --install-extension ms-toolsai.vscode-jupyter-powertoys
code --install-extension ms-toolsai.vscode-jupyter-slideshow
code --install-extension ms-vscode.test-adapter-converter
code --install-extension njpwerner.autodocstring
code --install-extension Percy.vscode-numpy-viewer
code --install-extension redhat.vscode-xml
code --install-extension samuelcolvin.jinjahtml
code --install-extension TakumiI.markdowntable
code --install-extension tamasfe.even-better-toml
code --install-extension yzhang.markdown-all-in-one
```