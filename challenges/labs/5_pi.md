[root@ip-172-32-1-71 java]# yum -y install krb5-workstation krb5-libs krb5-auth-dialog
Loaded plugins: amazon-id, rhui-lb, search-disabled-repos
Package krb5-workstation-1.15.1-37.el7_6.x86_64 already installed and latest version
Package krb5-libs-1.15.1-37.el7_6.x86_64 already installed and latest version
No package krb5-auth-dialog available.
Nothing to do
[root@ip-172-32-1-71 java]# yum -y install krb5-workstation krb5-libs krb5-auth-dialog
Loaded plugins: amazon-id, rhui-lb, search-disabled-repos
Package krb5-workstation-1.15.1-37.el7_6.x86_64 already installed and latest version
Package krb5-libs-1.15.1-37.el7_6.x86_64 already installed and latest version
No package krb5-auth-dialog available.
Nothing to do
[root@ip-172-32-1-71 java]# vi /var/kerberos/krb5kdc/kdc.conf
[root@ip-172-32-1-71 java]# vi /var/kerberos/krb5kdc/kdc.conf
[root@ip-172-32-1-71 java]# vi /etc/krb5.conf
[root@ip-172-32-1-71 java]# cat /etc/krb5.conf
# Configuration snippets may be placed in this directory as well
includedir /etc/krb5.conf.d/

[logging]
 default = FILE:/var/log/krb5libs.log
 kdc = FILE:/var/log/krb5kdc.log
 admin_server = FILE:/var/log/kadmind.log

[libdefaults]
 dns_lookup_realm = false
 ticket_lifetime = 24h
 renew_lifetime = 7d
 forwardable = true
 rdns = false
 pkinit_anchors = /etc/pki/tls/certs/ca-bundle.crt
 default_realm = SNAWALGARIA
 default_ccache_name = KEYRING:persistent:%{uid}
 default_tgs_enctypes = aes256-cts-hmac-sha1-96
 default_tkt_enctypes = aes256-cts-hmac-sha1-96
 permitted_enctypes = aes256-cts-hmac-sha1-96
 udp_preference_limit = 1
 kdc_timeout = 3000


[realms]
 SNAWALGARIA = {
  kdc = 172.32.1.71
  admin_server = 172.32.1.71
 }

[domain_realm]
SNAWALGARIA = SNAWALGARIA
[root@ip-172-32-1-71 java]# /usr/sbin/kdb5_util create -s
Loading random data
Initializing database '/var/kerberos/krb5kdc/principal' for realm 'SNAWALGARIA',
master key name 'K/M@SNAWALGARIA'
You will be prompted for the database Master Password.
It is important that you NOT FORGET this password.
Enter KDC database master key: 
Re-enter KDC database master key to verify: 
[root@ip-172-32-1-71 java]# kadmin.local
Authenticating as principal root/admin@SNAWALGARIA with password.
kadmin.local:  addprinc cloudera-scm@SNAWALGARIA
WARNING: no policy specified for cloudera-scm@SNAWALGARIA; defaulting to no policy
Enter password for principal "cloudera-scm@SNAWALGARIA": 
Re-enter password for principal "cloudera-scm@SNAWALGARIA": 
Principal "cloudera-scm@SNAWALGARIA" created.
kadmin.local:  exit
[root@ip-172-32-1-71 java]# vi /var/kerberos/krb5kdc/kadm5.acl
[root@ip-172-32-1-71 java]# kadmin.local
Authenticating as principal root/admin@SNAWALGARIA with password.
kadmin.local:  addpol admin
kadmin.local:  addpol users
kadmin.local:  addpol hosts
kadmin.local:  exit
[root@ip-172-32-1-71 java]# service krb5kdc start
Redirecting to /bin/systemctl start krb5kdc.service
[root@ip-172-32-1-71 java]# service kadmin start
Redirecting to /bin/systemctl start kadmin.service
[root@ip-172-32-1-71 java]# kadmin.local
Authenticating as principal root/admin@SNAWALGARIA with password.
kadmin.local:  addprincp rocky@SNAWALGARIA
kadmin.local: Unknown request "addprincp".  Type "?" for a request list.
kadmin.local:  ?
Available kadmin.local requests:

add_principal, addprinc, ank
                         Add principal
delete_principal, delprinc
                         Delete principal
modify_principal, modprinc
                         Modify principal
rename_principal, renprinc
                         Rename principal
change_password, cpw     Change password
get_principal, getprinc  Get principal
list_principals, listprincs, get_principals, getprincs
                         List principals
add_policy, addpol       Add policy
modify_policy, modpol    Modify policy
delete_policy, delpol    Delete policy
get_policy, getpol       Get policy
list_policies, listpols, get_policies, getpols
                         List policies
get_privs, getprivs      Get privileges
ktadd, xst               Add entry(s) to a keytab
ktremove, ktrem          Remove entry(s) from a keytab
lock                     Lock database exclusively (use with extreme caution!)
unlock                   Release exclusive database lock
purgekeys                Purge previously retained old keys from a principal
get_strings, getstrs     Show string attributes on a principal
set_string, setstr       Set a string attribute on a principal
del_string, delstr       Delete a string attribute on a principal
list_requests, lr, ?     List available requests.
quit, exit, q            Exit program.
kadmin.local:  
kadmin.local:  addprinc rocky@SNAWALGARIA
WARNING: no policy specified for rocky@SNAWALGARIA; defaulting to no policy
Enter password for principal "rocky@SNAWALGARIA": 
Re-enter password for principal "rocky@SNAWALGARIA": 
Principal "rocky@SNAWALGARIA" created.
kadmin.local:  addprinc denali@SNAWALGARIA
WARNING: no policy specified for denali@SNAWALGARIA; defaulting to no policy
Enter password for principal "denali@SNAWALGARIA": 
Re-enter password for principal "denali@SNAWALGARIA": 
Principal "denali@SNAWALGARIA" created.
kadmin.local:  addprinc cloudera-scm@SNAWALGARIA
WARNING: no policy specified for cloudera-scm@SNAWALGARIA; defaulting to no policy
Enter password for principal "cloudera-scm@SNAWALGARIA": 
Re-enter password for principal "cloudera-scm@SNAWALGARIA": 
add_principal: Principal or policy already exists while creating "cloudera-scm@SNAWALGARIA".
kadmin.local:  exit
[root@ip-172-32-1-71 java]# kinit 
kinit: Client 'root@SNAWALGARIA' not found in Kerberos database while getting initial credentials
[root@ip-172-32-1-71 java]# kinit cloudera-scm
Password for cloudera-scm@SNAWALGARIA: 
[root@ip-172-32-1-71 java]# klist
Ticket cache: KEYRING:persistent:0:0
Default principal: cloudera-scm@SNAWALGARIA

Valid starting       Expires              Service principal
15.02.2019 11:39:56  16.02.2019 11:39:56  krbtgt/SNAWALGARIA@SNAWALGARIA
	renew until 22.02.2019 11:39:56
[root@ip-172-32-1-71 java]# 

