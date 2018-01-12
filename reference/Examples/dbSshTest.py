from VinosDBL import *

# ESTO FUNCIONA!!!

# Para servidor local:
# dbConf = {
#     u'dbHost': u'127.0.0.1',
#     u'dbPort': 3306,
#     u'dbUser': u'root',
#     u'dbPass': u'',
#     u'dbName': u'vinosdb'
# }
# sshConf = None

# Para SSH
dbConf = {
    u'dbHost': u'127.0.0.1',
    u'dbPort': 3306,
    u'dbUser': u'root',
    u'dbPass': u'1Q2w3e4r5t6y7u8i9o0p',
    u'dbName': u'vinosdb'
}
sshConf = {
    u'sshHost': u'200.1.17.223',
    u'sshPort': 22,
    u'sshUser': u'spartan',
    u'sshPass': u'1Q2w3e4r5t6y7u8i9o0p',
    u'localHost': u'127.0.0.1',
    u'localPort': 3037
}
vinosDB = VinosDBL()
vinosDB.connect(dbConf=dbConf, sshConf=sshConf)
print vinosDB.conn.is_connected()
print vinosDB.simple_mysql_read(u'select * from %s', u'vinos')

# Referencias:
# https://github.com/pahaz/sshtunnel
# https://stackoverflow.com/questions/45213676/access-remote-db-via-ssh-tunnel-python-3