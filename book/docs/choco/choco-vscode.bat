:: about 
:: ------------------------------------------------------------------------------------
:: ------------------------------------------------------------------------------------

:: optional params:
:: /NoDesktopIcon - Don't add a desktop icon.
:: /NoQuicklaunchIcon - Don't add an icon to the QuickLaunch area.
:: /NoContextMenuFiles - Don't add an Open with Code entry to the context menu for files.
:: /NoContextMenuFolders - Dont't add an Open with Code entry to the context menu for folders.
:: /DontAddToPath - Don't add Visual Studio Code to the system PATH.
:: Example: choco install vscode --params "/NoDesktopIcon /DontAddToPath"

:: refs:
:: ------------------------------------------------------------------------------------
:: ------------------------------------------------------------------------------------
:: https://chocolatey.org/packages/vscode

choco install vscode

pause