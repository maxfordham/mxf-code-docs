:: about 
:: ------------------------------------------------------------------------------------
:: ------------------------------------------------------------------------------------
:: chocolatey is a windows package installer.
:: it can be used to install common packages straight from the command line rather than 
:: downloading an installer .exe and running the GUI installer
:: it does a similar job to sccm but is slimmer and more agile
:: other similar things include: OneGet, PackageManager (windows)
:: it installs to (see ref below for reasoning): C:\ProgramData


:: refs:
:: ------------------------------------------------------------------------------------
:: ------------------------------------------------------------------------------------
:: https://chocolatey.org/install
:: https://chocolatey.org/docs/default-chocolatey-install-reasoning


:: this command will download and install chocolatey into "C:\ProgramData"
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"

pause