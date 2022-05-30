# Comparing use of IronPython (2.7.7) and CPython (3.8.5)

- Issues with encoding seem to be resolved when using CPython.
	- For example, when using subprocess, and then decoding, the unicode strings were not printing correctly.
	- When switching to use CPython, these issues resolved.
	- So if you are experiencing encoding problems, try switching to using CPython.
	
- clr.AddReferenceToFileAndPath attribute error in CPython
	- GitHub issue: https://github.com/eirannejad/pyRevit/issues/1500
	
- In IronPython, there are issues when importing the "requests" package
	