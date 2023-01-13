
[list-all-super-users](https://askubuntu.com/questions/611584/how-could-i-list-all-super-users)
`grep -Po '^sudo.+:\K.*$' /etc/group`