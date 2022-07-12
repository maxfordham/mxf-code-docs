:: about 
:: ------------------------------------------------------------------------------------
:: ------------------------------------------------------------------------------------
:: using choco we can install anaconda automatically (at a button click)
:: we will choose to install it in the user space. 

:: refs:
:: ------------------------------------------------------------------------------------
:: ------------------------------------------------------------------------------------
:: https://chocolatey.org/packages/Miniconda3


choco install Miniconda3 --params '"/AddToPath:1 /InstallationType:JustMe /D:%SystemDrive%\Miniconda3 /RegisterPython:0"' --force

pause