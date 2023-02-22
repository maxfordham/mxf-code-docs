# NetExtender on Linux

This document will show you how to install and run NetExtender on Linux.

## Install NetExtender on Linux

REF: <https://www.sonicwall.com/support/knowledge-base/how-can-i-download-and-install-netextender-on-linux/180105195559153/>

### Install pptpd

```bash
sudo apt install pptpd
```

### Download linux .tgz file for either 32-bit or 64-bit: <https://www.sonicwall.com/products/remote-access/vpn-clients/>

You can check which version you are by running:

```bash
uname -m
```

### Extract .tgz

```bash
tar xzvf NetExtender.Linux-10.2.845.x86_64.tgz
```

### Change directory

```bash
cd netExtenderClient
```

### Install

```bash
sudo ./install
```

## Running NetExtender on Linux

### Disconnect from NetExtender VPN on Windows and restart WSL

### Run NetExtender on WSL

```bash
netExtender
```

### Fill in fields

```bash
SSL VPN Server: vpn.maxfordham.com
User: your.user
Password: YourPassword
Domain: LocalDomain
```

### To test that the connection has worked, we can ping the servers

```bash
ansible all -m ping
```

```{note}
Running both NetExtender on Windows and Linux seems to have its issues.
For now, it is best to disconnect from the Windows VPN when doing any deployment via ansible. 
I think this is due to the tunnelling not being set up correctly i.e. NetExtender in Linux
needs further configuration.
```
