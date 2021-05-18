database_ports = {  
                  3306:'MySQL', 
                  1433:'MSSQL', 
                  1434:'MySQL',
                  27017:'MongoDB', 
                  27018:'MongoDB', 
                  27019:'MongoDB',
                  1521:'Oracle', 
                  1630:'Oracle',
                  6379:'Redis',  
                  6380:'Redis', 
                  5984:'CouchDB', 
                  11211:'Memcached', 
                  50010:'Hadoop', 
                  50020:'Hadoop',
                  50070:'Hadoop',
                  50075:'Hadoop',
                  50090:'Hadoop',
                  50105:'Hadoop',
                  50470:'Hadoop',
                  1006:'Hadoop',
                  1004:'Hadoop',
                  8020:'Hadoop',
                  9200:'Elastic',
                  9300:'Elastic',
                  9042:'ScyllaDB',
                  5433:'PostgreSQL',
                  5432:'PostgreSQL',
                  29015:'RethinkDB',
                  28015:'RethinkDB',
                  50000:'DB2',
                  3000:'Aerospike',
                  2638:'Sybase',
                }

admin_ports = { 
                22:'SSH', 
                2222:'SSH', 
                23:'Telnet',
                3389:'RDP', 
                5900:'VNC', 
                5901:'VNC', 
                5902:'VNC', 
                5903:'VNC', 
                5904:'VNC', 
                137:'NetBIOS', 
                138:'NetBIOS', 
                139:'NetBIOS', 
                160:'SNMP',
                161:'SNMP',
              }

svc_ports  = {2379:'etcd', 23:'Telnet', 2380:'etcd', 2375:'Docker', 15672:'RabbitMQ', 5060:'SIP', 5601:'Kibana', 5672:'RabbitMQ', 3299:'SAP Router', 111:'NFS', 10443:'Fortinet', 1883:'MQTT'}

ftp_ports  = {20:'FTP', 21:'FTP'}

smb_ports  = {445:'SMB'}

exploitable_ports = {  
                  11211:'Memcached', 
                  1090:'Java RMI', 
                  1098:'Java RMI',
                  1099:'Java RMI', 
                  4444:'Java RMI', 
                  11099:'Java RMI',
                  10999:'Java RMI',  
                  7000:'WebLogic', 
                  7001:'WebLogic', 
                  7002:'WebLogic', 
                  7003:'WebLogic', 
                  8000:'WebLogic',
                  8001:'WebLogic',
                  8002:'WebLogic',
                  8003:'WebLogic',
                  9000:'WebLogic',
                  9001:'WebLogic',
                  9002:'WebLogic',
                  9003:'WebLogic',
                  9503:'WebLogic',
                  7070:'WebLogic',
                  7071:'WebLogic',
                  45000:'JDWP',
                  45001:'JDWP',
                  8686:'JMX',
                  9012:'JMX',
                  50500:'JMX',
                  4848:'GlassFish',
                  11111:'JBoss',
                  4445:'JBoss',
                  8180:'JBoss',
                  8280:'JBoss',
                  8380:'JBoss',
                  6379:'Redis',
                  6380:'Redis',
                  27017:'MongoDB', 
                  27018:'MongoDB', 
                  27019:'MongoDB',
                  1521:'Oracle', 
                  1630:'Oracle', 
                  9200:'Elastic',
                  9300:'Elastic',
                  5672:'RabbitMQ',
                  15672:'RabbitMQ',
                  10000:'Webmin',
                  3299:'SAP',
                  50000:'SAP-Java',
                  88:'Kerberos',
                  513:'Rlogin',
                  2049:'NFS_share',
                  3316:'OpenMRS',
                  2375:'Docker',
                  10250:'Kubernetis',
                  5601:'Kibana',
                  8082:'H2database',
                  8082:'probably Seafile',
                }

ldap_ports = {389:'LDAP',636:'LDAPS'}

bgp_ports = {179:'BGP'}

http_ports = {
              80:'HTTP', 
              81:'HTTP', 
              82:'HTTP', 
              83:'HTTP', 
              84:'HTTP', 
              85:'HTTP', 
              86:'HTTP', 
              87:'HTTP', 
              88:'HTTP', 
              89:'HTTP', 
              8090:'HTTP', 
              8008:'HTTP',
              8080:'HTTP',
              8081:'HTTP',
              8082:'HTTP',
              8083:'HTTP',
              8084:'HTTP',
              9090:'HTTP',
              }

https_ports = {443:'HTTPS', 8443:'HTTPS'}

vpn_ports   = {1194:'OpenVPN'}

time_ports  = {123:'NTP'}

dns_ports   = {53:'DNS'}

email_ports = {25:'SMTP', 110:'POP3', 143:'IMAP', 465:'IMAP', 993:'IMAPS', 587:'Mail', 995:'POP3S'}

ssh_ports   = {22:'SSH', 2222:'SSH'}

ignore_ports = {}

rdp_ports = {3389:'RDP'}

known_ports = (vpn_ports, email_ports, admin_ports, ftp_ports, ldap_ports, http_ports, https_ports, time_ports, ignore_ports, smb_ports, database_ports, svc_ports, dns_ports, bgp_ports)






