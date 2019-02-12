

# 1. vm.swappiness
First the vm.swappiness is set to 60:
```

Run command to change (as root):
```
sudo sysctl vm.swappiness=1

```

After the change:
```
'cat /proc/sys/vm/swappiness'

1

"vm.swappiness = 1" needs to be added to /etc/sysctl.conf file for persistence
```
'echo "vm.swappiness = 1" >> /etc/sysctl.conf'
```

# 2. Mount attributes
```
sudo 'mount -l'

sysfs on /sys type sysfs (rw,nosuid,nodev,noexec,relatime,seclabel)
proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)
devtmpfs on /dev type devtmpfs (rw,nosuid,seclabel,size=7873196k,nr_inodes=1968299,mode=755)
securityfs on /sys/kernel/security type securityfs (rw,nosuid,nodev,noexec,relatime)
tmpfs on /dev/shm type tmpfs (rw,nosuid,nodev,seclabel)
devpts on /dev/pts type devpts (rw,nosuid,noexec,relatime,seclabel,gid=5,mode=620,ptmxmode=000)
tmpfs on /run type tmpfs (rw,nosuid,nodev,seclabel,mode=755)
tmpfs on /sys/fs/cgroup type tmpfs (ro,nosuid,nodev,noexec,seclabel,mode=755)
cgroup on /sys/fs/cgroup/systemd type cgroup (rw,nosuid,nodev,noexec,relatime,seclabel,xattr,release_agent=/usr/lib/systemd/systemd-cgroups-agent,name=systemd)
pstore on /sys/fs/pstore type pstore (rw,nosuid,nodev,noexec,relatime)
cgroup on /sys/fs/cgroup/blkio type cgroup (rw,nosuid,nodev,noexec,relatime,seclabel,blkio)
cgroup on /sys/fs/cgroup/memory type cgroup (rw,nosuid,nodev,noexec,relatime,seclabel,memory)
cgroup on /sys/fs/cgroup/perf_event type cgroup (rw,nosuid,nodev,noexec,relatime,seclabel,perf_event)
cgroup on /sys/fs/cgroup/hugetlb type cgroup (rw,nosuid,nodev,noexec,relatime,seclabel,hugetlb)
cgroup on /sys/fs/cgroup/net_cls,net_prio type cgroup (rw,nosuid,nodev,noexec,relatime,seclabel,net_prio,net_cls)
cgroup on /sys/fs/cgroup/cpu,cpuacct type cgroup (rw,nosuid,nodev,noexec,relatime,seclabel,cpuacct,cpu)
cgroup on /sys/fs/cgroup/cpuset type cgroup (rw,nosuid,nodev,noexec,relatime,seclabel,cpuset)
cgroup on /sys/fs/cgroup/devices type cgroup (rw,nosuid,nodev,noexec,relatime,seclabel,devices)
cgroup on /sys/fs/cgroup/freezer type cgroup (rw,nosuid,nodev,noexec,relatime,seclabel,freezer)
cgroup on /sys/fs/cgroup/pids type cgroup (rw,nosuid,nodev,noexec,relatime,seclabel,pids)
configfs on /sys/kernel/config type configfs (rw,relatime)
/dev/nvme0n1p2 on / type xfs (rw,relatime,seclabel,attr2,inode64,noquota)
selinuxfs on /sys/fs/selinux type selinuxfs (rw,relatime)
hugetlbfs on /dev/hugepages type hugetlbfs (rw,relatime,seclabel)
mqueue on /dev/mqueue type mqueue (rw,relatime,seclabel)
debugfs on /sys/kernel/debug type debugfs (rw,relatime)
systemd-1 on /proc/sys/fs/binfmt_misc type autofs (rw,relatime,fd=42,pgrp=1,timeout=0,minproto=5,maxproto=5,direct,pipe_ino=46342)
tmpfs on /run/user/1000 type tmpfs (rw,nosuid,nodev,relatime,seclabel,size=1579140k,mode=700,uid=1000,gid=1000)

```
ansible -i hosts all --become -c paramiko -m shell -a 'cat /etc/fstab'
ec2-18-194-208-128.eu-central-1.compute.amazonaws.com | SUCCESS | rc=0 >>

#
# /etc/fstab
# Created by anaconda on Tue Jun  5 13:56:10 2018
#
# Accessible filesystems, by reference, are maintained under '/dev/disk'
# See man pages fstab(5), findfs(8), mount(8) and/or blkid(8) for more info
#
UUID=c64c61c1-9e9b-4f2e-912d-d81ce4c3b716 /                       ext4    defaults        1 1
tmpfs                   /dev/shm                tmpfs   defaults        0 0
devpts                  /dev/pts                devpts  gid=5,mode=620  0 0
sysfs                   /sys                    sysfs   defaults        0 0
proc                    /proc                   proc    defaults        0 0
```
# 3. Show the reserve space of any non-root, ext-based volumes
```
[ec2-user@ip-172-32-1-71 ~]$ sudo lsblk
NAME        MAJ:MIN RM SIZE RO TYPE MOUNTPOINT
nvme0n1     259:1    0  50G  0 disk 
├─nvme0n1p1 259:2    0   1M  0 part 
└─nvme0n1p2 259:3    0  50G  0 part /
nvme1n1     259:0    0  12G  0 disk 

ansible -i hosts all --become -c paramiko -m shell -a 'df -h'
ec2-35-158-75-43.eu-central-1.compute.amazonaws.com | SUCCESS | rc=0 >>
Filesystem      Size  Used Avail Use% Mounted on
/dev/xvda1      7.8G  752M  6.7G  10% /
tmpfs           7.8G     0  7.8G   0% /dev/shm
```
The AWS settings were supposed to add 30GB, but it is not configured on the partition.
The workaround for this problem is to install growpart utils and resize root partition:

```
ansible -i hosts all --become -c paramiko -m shell -a 'yum install -y epel-release'

ansible -i hosts all --become -c paramiko -m shell -a 'yum -y install cloud-utils-growpart'
```
```
ansible -i hosts all --become -c paramiko -m shell -a 'growpart /dev/xvda 1'
ec2-18-185-97-117.eu-central-1.compute.amazonaws.com | SUCCESS | rc=0 >>
CHANGED: partition=1 start=2048 old: size=16775168 end=16777216 new: size=62908492,end=62910540
```
and reboot the VMs.
```
ansible -i hosts all  --become -c paramiko -m shell -a 'reboot'
```
Run df -h again:
```
ansible -i hosts all --become -c paramiko -m shell -a 'df -h'
ec2-18-185-97-117.eu-central-1.compute.amazonaws.com | SUCCESS | rc=0 >>
Filesystem      Size  Used Avail Use% Mounted on
/dev/xvda1       30G  819M   28G   3% /
tmpfs           7.8G     0  7.8G   0% /dev/shm
```
```
ansible -i hosts all  --become -c paramiko -m shell -a 'lsblk'
ec2-18-196-113-149.eu-central-1.compute.amazonaws.com | SUCCESS | rc=0 >>
NAME    MAJ:MIN RM SIZE RO TYPE MOUNTPOINT
xvda    202:0    0  30G  0 disk
└─xvda1 202:1    0  30G  0 part /
```

# 4. Disable transparent hugepage support
By default transparent hugepage support was enabled:
```
ansible -i hosts all --become  -c paramiko -m shell -a 'cat /sys/kernel/mm/redhat_transparent_hugepage/defrag'
ec2-35-158-75-43.eu-central-1.compute.amazonaws.com | SUCCESS | rc=0 >>
[always] madvise never
```
```
ansible -i hosts all --become -c paramiko -m shell -a 'cat /sys/kernel/mm/redhat_transparent_hugepage/enabled'
ec2-52-59-231-3.eu-central-1.compute.amazonaws.com | SUCCESS | rc=0 >>
[always] madvise never
```
To diasble (interactively):
```
echo never > /sys/kernel/mm/transparent_hugepage/defrag'
```
echo never > /sys/kernel/mm/transparent_hugepage/enabled'
:
```
cat /sys/kernel/mm/transparent_hugepage/defrag'
always madvise [never]
```
```
cat /sys/kernel/mm/transparent_hugepage/enabled'
always madvise [never]
```
To disable on reboot modify /etc/rc.d/rc.local file:
```
ansible -i hosts all --become -c paramiko -m shell -a 'echo "echo never > /sys/kernel/mm/redhat_transparent_hugepage/defrag" >> /etc/rc.d/rc.local'
```
```
ansible -i hosts all --become -c paramiko -m shell -a 'echo "echo never > /sys/kernel/mm/redhat_transparent_hugepage/enabled" >> /etc/rc.d/rc.local'
```
# 5. List your network interface configuration
```
ansible -i hosts all --become -c paramiko -m shell -a 'ifconfig'
ec2-18-196-113-149.eu-central-1.compute.amazonaws.com | SUCCESS | rc=0 >>
eth0      Link encap:Ethernet  HWaddr 06:AA:A3:3B:92:FE
          inet addr:172.31.44.213  Bcast:172.31.47.255  Mask:255.255.240.0
          inet6 addr: fe80::4aa:a3ff:fe3b:92fe/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:9001  Metric:1
          RX packets:1220 errors:0 dropped:0 overruns:0 frame:0
          TX packets:939 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:809520 (790.5 KiB)  TX bytes:122985 (120.1 KiB)

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:0 (0.0 b)  TX bytes:0 (0.0 b)
```
# 6.
nslookup tool is not installed on CentOS server. To install:
```
ansible -i hosts all --become -c paramiko -m shell -a 'sudo yum install -y bind-utils'
```
[ec2-user@ip-172-32-1-71 ~]nslookup ec2-34-247-254-210.eu-wescompute.amazonaws.com
Server:		169.254.169.253
Address:	169.254.169.253#53

Non-authoritative answer:
Name:	ec2-34-247-254-210.eu-west-1.compute.amazonaws.com
Address: 172.32.1.235

[ec2-user@ip-172-32-1-71 ~]$ nslookup 34.247.254.210
Server:		169.254.169.253
Address:	169.254.169.253#53

Non-authoritative answer:
210.254.247.34.in-addr.arpa	name = ec2-34-247-254-210.eu-west-1.compute.amazonaws.com.

Authoritative answers can be found from:


```

Google.com
```
ansible -i hosts all --become -c paramiko -m shell -a 'nslookup google.com'
ec2-18-185-97-117.eu-central-1.compute.amazonaws.com | SUCCESS | rc=0 >>
Server:		172.31.0.2
Address:	172.31.0.2#53

Non-authoritative answer:
Name:	google.com
Address: 172.217.22.110
```

# 7. Show the nscd service is running
nscd is not installed by default on CentOS 6.
To install and configure:
```
ansible -i hosts all --become -c paramiko -m shell -a 'yum -y install nscd'
```
```
ansible -i hosts all --become -c paramiko -m shell -a 'service nscd start'
```
```
ansible -i hosts all --become -c paramiko -m shell -a 'chkconfig nscd on'
```
Check if running:
```
[ec2-user@ip-172-32-1-71 ~]$ sudo nscd -g
nscd configuration:

              0  server debug level
         2m  5s  server runtime
              5  current number of threads
             32  maximum number of threads
              0  number of times clients had to wait
             no  paranoia mode enabled
           3600  restart internal
              5  reload count

passwd cache:

            yes  cache is enabled
            yes  cache is persistent
            yes  cache is shared
            211  suggested size
         216064  total data pool size
            344  used data pool size
            600  seconds time to live for positive entries
             20  seconds time to live for negative entries
              0  cache hits on positive entries
              0  cache hits on negative entries
              2  cache misses on positive entries
              0  cache misses on negative entries
              0% cache hit rate
              4  current number of cached values
              4  maximum number of cached values
              0  maximum chain length searched
              0  number of delays on rdlock
              0  number of delays on wrlock
              0  memory allocations failed
            yes  check /etc/passwd for changes

group cache:

            yes  cache is enabled
            yes  cache is persistent
            yes  cache is shared
            211  suggested size
         216064  total data pool size
             80  used data pool size
           3600  seconds time to live for positive entries
             60  seconds time to live for negative entries
              0  cache hits on positive entries
              0  cache hits on negative entries
              0  cache misses on positive entries
              2  cache misses on negative entries
              0% cache hit rate
              1  current number of cached values
              1  maximum number of cached values
              0  maximum chain length searched
              0  number of delays on rdlock
              0  number of delays on wrlock
              0  memory allocations failed
            yes  check /etc/group for changes

hosts cache:

            yes  cache is enabled
            yes  cache is persistent
            yes  cache is shared
            211  suggested size
         216064  total data pool size
              0  used data pool size
           3600  seconds time to live for positive entries
             20  seconds time to live for negative entries
              0  cache hits on positive entries
              0  cache hits on negative entries
              0  cache misses on positive entries
              0  cache misses on negative entries
              0% cache hit rate
              0  current number of cached values
              0  maximum number of cached values
              0  maximum chain length searched
              0  number of delays on rdlock
              0  number of delays on wrlock
              0  memory allocations failed
            yes  check /etc/hosts for changes

services cache:

            yes  cache is enabled
            yes  cache is persistent
            yes  cache is shared
            211  suggested size
         216064  total data pool size
              0  used data pool size
          28800  seconds time to live for positive entries
             20  seconds time to live for negative entries
              0  cache hits on positive entries
              0  cache hits on negative entries
              0  cache misses on positive entries
              0  cache misses on negative entries
              0% cache hit rate
              0  current number of cached values
              0  maximum number of cached values
              0  maximum chain length searched
              0  number of delays on rdlock
              0  number of delays on wrlock
              0  memory allocations failed
            yes  check /etc/services for changes

[ec2-user@ip-172-32-1-71 ~]$ time nslookup google.com
Server:		169.254.169.253
Address:	169.254.169.253#53

Non-authoritative answer:
Name:	google.com
Address: 74.125.193.102
Name:	google.com
Address: 74.125.193.138
Name:	google.com
Address: 74.125.193.113
Name:	google.com
Address: 74.125.193.100
Name:	google.com
Address: 74.125.193.139
Name:	google.com
Address: 74.125.193.101


real	0m0.009s
user	0m0.005s
sys	0m0.003s


# 8. Show the ntpd service is running
For AWS Amazon Time Sync Service can be used (chronyd instead of ntpd). Steps are desribed here:
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/set-time.html
Chrony running:
```
[ec2-user@ip-172-32-1-71 ~]$ sudo service chronyd status
Redirecting to /bin/systemctl status chronyd.service
● chronyd.service - NTP client/server
   Loaded: loaded (/usr/lib/systemd/system/chronyd.service; enabled; vendor preset: enabled)
   Active: active (running) since So 2019-02-10 18:18:41 UTC; 18h ago
     Docs: man:chronyd(8)
           man:chrony.conf(5)
 Main PID: 2167 (chronyd)
   CGroup: /system.slice/chronyd.service
           └─2167 /usr/sbi
```
[ec2-user@ip-172-32-1-71 ~]$ sudo chronyc sources -v
210 Number of sources = 4

  .-- Source mode  '^' = server, '=' = peer, '#' = local clock.
 / .- Source state '*' = current synced, '+' = combined , '-' = not combined,
| /   '?' = unreachable, 'x' = time may be in error, '~' = time too variable.
||                                                 .- xxxx [ yyyy ] +/- zzzz
||      Reachability register (octal) -.           |  xxxx = adjusted offset,
||      Log2(Polling interval) --.      |          |  yyyy = measured offset,
||                                \     |          |  zzzz = estimated error.
||                                 |    |           \
MS Name/IP address         Stratum Poll Reach LastRx Last sample               
===============================================================================
^- 69.195.159.158                2  10   277   177  -6183us[-6209us] +/-   98ms
^- ec2-52-48-113-20.eu-west>     2   7   377    94  -1428us[-1457us] +/-   46ms
^- ec2-52-209-118-149.eu-we>     2   7   377   118  +1483us[+1453us] +/- 7307us
^* ec2-52-17-231-73.eu-west>     2   7   377    46    -47us[  -78us] +/-  760us
[ec2-user@ip-172-32-1-71 ~]$ sudo chronyc tracking
Reference ID    : 3411E749 (ec2-52-17-231-73.eu-west-1.compute.amazonaws.com)
Stratum         : 3
Ref time (UTC)  : Mon Feb 11 13:12:59 2019
System time     : 0.000008925 seconds slow of NTP time
Last offset     : -0.000030526 seconds
RMS offset      : 0.000039479 seconds
Frequency       : 6.977 ppm fast
Residual freq   : -0.013 ppm
Skew            : 0.086 ppm
Root delay      : 0.001427444 seconds
Root dispersion : 0.000123399 seconds
Update interval : 128.2 seconds
Leap status     : Normal

