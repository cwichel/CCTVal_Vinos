# -*- coding: utf-8 -*-
# =============================================================================
# Modules
# =============================================================================
from VinosDBL import *


# =============================================================================
# Carga de cervezas
# =============================================================================
dbConf = {
    u'dbHost': u'127.0.0.1',
    u'dbPort': 3306,
    u'dbUser': u'root',
    u'dbPass': u'1Q2w3e4r5t6y7u8i9o0p',
    u'dbName': u'vinosdb'
}
sshConf = {
    u'sshHost': u'127.0.0.1',
    u'sshPort': 9999,
    u'sshUser': u'spartan',
    u'sshPass': u'1Q2w3e4r5t6y7u8i9o0p',
    u'localHost': u'127.0.0.1',
    u'localPort': 3037
}

# Connect
vinosDB = VinosDBL()
vinosDB.connect(dbConf=dbConf, sshConf=sshConf)

# Check if ok
isConnected = vinosDB.conn.is_connected()

if isConnected:
    # # Carga de cervezas
    # cervezas = [
    #     [u'cerveza_1', u'tipo_1', u'viña_1', u'valle_1', 2018, u'No disponible'],
    #     [u'cerveza_2', u'tipo_2', u'viña 2', u'valle_2', 2018, u'No disponible']
    # ]
    # vinosDB.new_vino(cervezas)

    # # Carga de estanques
    # estanques = [
    #     [301, u'Estanque para cervezas 1'],
    #     [302, u'Estanque para cervezas 2']
    # ]
    # vinosDB.new_estanque(estanques)

    # Indicar que cerveza esta en que estanque
    # cargas = [
    #     [2, 2],
    #     [3, 3]
    # ]
    # vinosDB.new_vino_in_estanque(cargas)

    # for num in range(1, 31):
    #     fileName = u'../../data/Espectros/cerveza%d.txt' % num
    #     vinosDB.new_espectro(fileName, 2, 2)

    vinosDB.close()