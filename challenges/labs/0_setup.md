AWS
172.32.1.71 	ip-172-32-1-71.eu-west-1.compute.internal
172.32.1.156	ip-172-32-1-156.eu-west-1.compute.internal
172.32.1.185    ip-172-32-1-185.eu-west-1.compute.internal
172.32.1.230    ip-172-32-1-230.eu-west-1.compute.internal
172.32.1.235    ip-172-32-1-235.eu-west-1.compute.internal

RHEL 7.6

[root@ip-172-32-1-71 ~]# df -kh
Filesystem      Size  Used Avail Use% Mounted on
/dev/nvme0n1p2   50G  1,4G   49G   3% /
devtmpfs        7,6G     0  7,6G   0% /dev
tmpfs           7,6G     0  7,6G   0% /dev/shm
tmpfs           7,6G  8,4M  7,6G   1% /run
tmpfs           7,6G     0  7,6G   0% /sys/fs/cgroup
tmpfs           1,6G     0  1,6G   0% /run/user/1000

yum repolist enabled
Loaded plugins: amazon-id, rhui-lb, search-disabled-repos
repo id                                          repo name                status
rhui-REGION-client-config-server-7/x86_64        Red Hat Update Infrastru      2
rhui-REGION-rhel-server-releases/7Server/x86_64  Red Hat Enterprise Linux 23.676
rhui-REGION-rhel-server-rh-common/7Server/x86_64 Red Hat Enterprise Linux    235
repolist: 23.913

rocky:x:3800:3800::/home/rocky:/bin/bash
denali:x:3900:3900::/home/denali:/bin/bash

rocky:x:3800:
denali:x:3900:
alaska:x:3901:denali
colorado:x:3902:rocky

[root@ip-172-32-1-71 ~]# getent group alaska
alaska:x:3901:denali

[root@ip-172-32-1-71 ~]# getent passwd rocky
rocky:x:3800:3800::/home/rocky:/bin/bash

