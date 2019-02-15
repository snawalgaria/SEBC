ls /etc/yum.repos.d
cloudera-manager.repo  index.html.2                    redhat-rhui.repo
index.html             index.html.3                    rhui-load-balancers.conf
index.html.1           redhat-rhui-client-config.repo
[root@ip-172-32-1-156 yum.repos.d]#


[root@ip-172-32-1-156 yum.repos.d]# 
[root@ip-172-32-1-156 yum.repos.d]# 
[root@ip-172-32-1-156 yum.repos.d]# /usr/share/cmf/schema/scm_prepare_database.sh mariadb -h 172.32.1.71 scm scm
Unknown database type: mariadb
usage: /usr/share/cmf/schema/scm_prepare_database.sh [options] (postgresql|mysql|oracle) database username [password]

Prepares a database (currently either MySQL, PostgreSQL or Oracle)
for use by Cloudera Service Configuration Manager (SCM):
o Creates a database (For PostgreSQL and MySQL only)
o Grants access to that database, by:
  - (PostgreSQL) Creating a role
  - (MySQL) Creating a grant
o Creates the SCM database configuration file.
o Tests if the database connection parameters are valid.

MANDATORY PARAMETERS
database type: either "oracle", "postgresql" or "mysql"
database: For PostgreSQL and MySQL, name of the SCM database to create.
          For Oracle this is the SID of the Oracle database.
username: Username for access to SCM's database.

OPTIONAL PARAMETERS
password: Password for the SCM user. If not provided, and --scm-password-script
          is not specified as an option, will prompt for it.

OPTIONS
   -h|--host       Database host. Default is to connect locally.
   -P|--port       Database port. If not specified, the database specific
                   default will be used: namely, 3306 for MySQL,
                   5432 for PostgreSQL, and 1521 for Oracle.
   -u|--user       Database username that has privileges for creating
                   users and grants.  The default is 'root'.
                   Typical values are 'root' for MySQL and
                   'postgres' for PostgreSQL. Not applicable for Oracle.
   -p|--password   Database Password. Default is no password.
   --scm-host      SCM server's hostname. Omit if SCM is colocated with MySQL.
   --config-path   Path to SCM configuration files.
                   Default is /etc/cloudera-scm-server.
   --scm-password-script Instead of obtaining the SCM username's password
                   directly, execute a script whose stdout is used as the
                   password.
   -f|--force      Don't stop when an error is encountered.
   -v|--verbose    Print more informational messages.
   -?|--help       Show this message.

NOTE ON POSTGRESQL CONFIGURATION
PostgreSQL must be configured to accept connections
with md5 password authentication.  To do so,
edit /var/lib/pgsql/data/pg_hba.conf (or similar)
to include "host all all 127.0.0.1/32 md5" _above_
a similar line that allows 'ident' authentication.
[root@ip-172-32-1-156 yum.repos.d]# /usr/share/cmf/schema/scm_prepare_database.sh mysql -h 172.32.1.71 scm scm
Enter SCM password: 
JAVA_HOME=/usr/lib/jvm/java-openjdk
Verifying that we can write to /etc/cloudera-scm-server
Creating SCM configuration file in /etc/cloudera-scm-server
Executing:  /usr/lib/jvm/java-openjdk/bin/java -cp /usr/share/java/mysql-connector-java.jar:/usr/share/java/oracle-connector-java.jar:/usr/share/java/postgresql-connector-java.jar:/usr/share/cmf/schema/../lib/* com.cloudera.enterprise.dbutil.DbCommandExecutor /etc/cloudera-scm-server/db.properties com.cloudera.cmf.db.
[                          main] DbCommandExecutor              INFO  Successfully connected to database.
All done, your SCM database is configured correctly!
[root@ip-172-32-1-156 yum.repos.d]# /usr/share/cmf/schema/scm_prepare_database.sh mysql -h 172.32.1.71 rman rman
Enter SCM password: 
JAVA_HOME=/usr/lib/jvm/java-openjdk
Verifying that we can write to /etc/cloudera-scm-server
Creating SCM configuration file in /etc/cloudera-scm-server
Executing:  /usr/lib/jvm/java-openjdk/bin/java -cp /usr/share/java/mysql-connector-java.jar:/usr/share/java/oracle-connector-java.jar:/usr/share/java/postgresql-connector-java.jar:/usr/share/cmf/schema/../lib/* com.cloudera.enterprise.dbutil.DbCommandExecutor /etc/cloudera-scm-server/db.properties com.cloudera.cmf.db.
[                          main] DbCommandExecutor              INFO  Successfully connected to database.
All done, your SCM database is configured correctly!
[root@ip-172-32-1-156 yum.repos.d]# /usr/share/cmf/schema/scm_prepare_database.sh mysql -h 172.32.1.71 hive hive
Enter SCM password: 
JAVA_HOME=/usr/lib/jvm/java-openjdk
Verifying that we can write to /etc/cloudera-scm-server
Creating SCM configuration file in /etc/cloudera-scm-server
Executing:  /usr/lib/jvm/java-openjdk/bin/java -cp /usr/share/java/mysql-connector-java.jar:/usr/share/java/oracle-connector-java.jar:/usr/share/java/postgresql-connector-java.jar:/usr/share/cmf/schema/../lib/* com.cloudera.enterprise.dbutil.DbCommandExecutor /etc/cloudera-scm-server/db.properties com.cloudera.cmf.db.
[                          main] DbCommandExecutor              INFO  Unable to login using supplied username/password.
[                          main] DbCommandExecutor              ERROR Error when connecting to database.
java.sql.SQLException: Access denied for user 'hive'@'ip-172-32-1-156.eu-west-1.compute.internal' (using password: YES)
	at com.mysql.jdbc.SQLError.createSQLException(SQLError.java:965)[mysql-connector-java.jar:5.1.47]
	at com.mysql.jdbc.MysqlIO.checkErrorPacket(MysqlIO.java:3978)[mysql-connector-java.jar:5.1.47]
	at com.mysql.jdbc.MysqlIO.checkErrorPacket(MysqlIO.java:3914)[mysql-connector-java.jar:5.1.47]
	at com.mysql.jdbc.MysqlIO.checkErrorPacket(MysqlIO.java:871)[mysql-connector-java.jar:5.1.47]
	at com.mysql.jdbc.MysqlIO.proceedHandshakeWithPluggableAuthentication(MysqlIO.java:1714)[mysql-connector-java.jar:5.1.47]
	at com.mysql.jdbc.MysqlIO.doHandshake(MysqlIO.java:1224)[mysql-connector-java.jar:5.1.47]
	at com.mysql.jdbc.ConnectionImpl.coreConnect(ConnectionImpl.java:2199)[mysql-connector-java.jar:5.1.47]
	at com.mysql.jdbc.ConnectionImpl.connectOneTryOnly(ConnectionImpl.java:2230)[mysql-connector-java.jar:5.1.47]
	at com.mysql.jdbc.ConnectionImpl.createNewIO(ConnectionImpl.java:2025)[mysql-connector-java.jar:5.1.47]
	at com.mysql.jdbc.ConnectionImpl.<init>(ConnectionImpl.java:778)[mysql-connector-java.jar:5.1.47]
	at com.mysql.jdbc.JDBC4Connection.<init>(JDBC4Connection.java:47)[mysql-connector-java.jar:5.1.47]
	at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)[:1.8.0_191]
	at sun.reflect.NativeConstructorAccessorImpl.newInstance(NativeConstructorAccessorImpl.java:62)[:1.8.0_191]
	at sun.reflect.DelegatingConstructorAccessorImpl.newInstance(DelegatingConstructorAccessorImpl.java:45)[:1.8.0_191]
	at java.lang.reflect.Constructor.newInstance(Constructor.java:423)[:1.8.0_191]
	at com.mysql.jdbc.Util.handleNewInstance(Util.java:425)[mysql-connector-java.jar:5.1.47]
	at com.mysql.jdbc.ConnectionImpl.getInstance(ConnectionImpl.java:386)[mysql-connector-java.jar:5.1.47]
	at com.mysql.jdbc.NonRegisteringDriver.connect(NonRegisteringDriver.java:330)[mysql-connector-java.jar:5.1.47]
	at java.sql.DriverManager.getConnection(DriverManager.java:664)[:1.8.0_191]
	at java.sql.DriverManager.getConnection(DriverManager.java:247)[:1.8.0_191]
	at com.cloudera.enterprise.dbutil.DbCommandExecutor.testDbConnection(DbCommandExecutor.java:253)[db-common-5.16.1.jar:]
	at com.cloudera.enterprise.dbutil.DbCommandExecutor.main(DbCommandExecutor.java:138)[db-common-5.16.1.jar:]
[                          main] DbCommandExecutor              ERROR Exiting with exit code 8
--> Error 8, giving up (use --force if you wish to ignore the error)
[root@ip-172-32-1-156 yum.repos.d]# /usr/share/cmf/schema/scm_prepare_database.sh mysql -h 172.32.1.71 hive hive
Enter SCM password: 
JAVA_HOME=/usr/lib/jvm/java-openjdk
Verifying that we can write to /etc/cloudera-scm-server
Creating SCM configuration file in /etc/cloudera-scm-server
Executing:  /usr/lib/jvm/java-openjdk/bin/java -cp /usr/share/java/mysql-connector-java.jar:/usr/share/java/oracle-connector-java.jar:/usr/share/java/postgresql-connector-java.jar:/usr/share/cmf/schema/../lib/* com.cloudera.enterprise.dbutil.DbCommandExecutor /etc/cloudera-scm-server/db.properties com.cloudera.cmf.db.
[                          main] DbCommandExecutor              INFO  Successfully connected to database.
All done, your SCM database is configured correctly!
[root@ip-172-32-1-156 yum.repos.d]# /usr/share/cmf/schema/scm_prepare_database.sh mysql -h 172.32.1.71 oozie oozie
Enter SCM password: 
JAVA_HOME=/usr/lib/jvm/java-openjdk
Verifying that we can write to /etc/cloudera-scm-server
Creating SCM configuration file in /etc/cloudera-scm-server
Executing:  /usr/lib/jvm/java-openjdk/bin/java -cp /usr/share/java/mysql-connector-java.jar:/usr/share/java/oracle-connector-java.jar:/usr/share/java/postgresql-connector-java.jar:/usr/share/cmf/schema/../lib/* com.cloudera.enterprise.dbutil.DbCommandExecutor /etc/cloudera-scm-server/db.properties com.cloudera.cmf.db.
[                          main] DbCommandExecutor              INFO  Successfully connected to database.
All done, your SCM database is configured correctly!
[root@ip-172-32-1-156 yum.repos.d]# /usr/share/cmf/schema/scm_prepare_database.sh mysql -h 172.32.1.71 hue hue
Enter SCM password: 
JAVA_HOME=/usr/lib/jvm/java-openjdk
Verifying that we can write to /etc/cloudera-scm-server
Creating SCM configuration file in /etc/cloudera-scm-server
Executing:  /usr/lib/jvm/java-openjdk/bin/java -cp /usr/share/java/mysql-connector-java.jar:/usr/share/java/oracle-connector-java.jar:/usr/share/java/postgresql-connector-java.jar:/usr/share/cmf/schema/../lib/* com.cloudera.enterprise.dbutil.DbCommandExecutor /etc/cloudera-scm-server/db.properties com.cloudera.cmf.db.
[                          main] DbCommandExecutor              INFO  Successfully connected to database.
All done, your SCM database is configured correctly!
[root@ip-172-32-1-156 yum.repos.d]# /usr/share/cmf/schema/scm_prepare_database.sh mysql -h 172.32.1.71 hue hue
 
