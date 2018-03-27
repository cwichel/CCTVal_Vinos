# -*- coding: utf-8 -*-

# ===========================================
# Modules
# ===========================================

import sshtunnel
import numpy as np
import mysql.connector as msq
from mysql.connector import errorcode


# ===========================================
# Clase VinosDBL
# ===========================================

class VinosDBL:

    # inicialización
    def __init__(self):
        self.isSSH = False
        self.data = []
        self.encoding = u'latin5'
        self.field_type = {
            0:      u"%f",                  # DECIMAL
            4:      u"%f",				    # FLOAT
            5:      u"%f",				    # DOUBLE
            1:      u"%d",				    # TINY
            2:      u"%d",				    # SHORT
            3:      u"%d",				    # LONG
            9:      u"%d",				    # INT24
            6:      u"NULL",				# NULL
            8:      u"LONGLONG",			# LONGLONG
            246:    u"NEWDECIMAL",          # NEWDECIMAL
            247:    u"INTERVAL",            # INTERVAL
            248:    u"SET",                 # SET
            255:    u"GEOMETRY", 		    # GEOMETRY
            14:     u"NEWDATE",			    # NEWDATE
            7:      u"TIMESTAMP",	        # TIMESTAMP
            13:     u"%Y",				    # YEAR
            10:     u"%Y-%m-%d",			# DATE
            11:     u"%H:%M:%S",			# TIME
            12:     u"%Y-%m-%d %H:%M:%S",   # DATETIME
            16:     u"'%x'",				# BIT
            15:     u"'%s'",				# VARCHAR
            249:    u"'%s'",                # TINY BLOB
            250:    u"'%s'",			    # MEDIUM BLOB
            251:    u"'%s'",			    # LONG BLOB
            252:    u"'%s'",			    # BLOB
            253:    u"'%s'",			    # VAR STRING
            254:    u"'%s'"			        # STRING
            }

    # =================================
    # Metodos de conexion
    # =================================

    def connect(self, dbConf, sshConf):
        """
        Función que permite conectarse a una base de datos. Si sshConf es None, se conecta de forma directa,
        en caso contrario utiliza el tunel ssh.
        :param dbConf:  diccionario con:    'dbHost', 'dbPort', 'dbUser', 'dbPass', dbName'
        :param sshConf: diccionario con:    'sshHost', 'sshPort', 'sshUser', 'sshPass', 'localHost', 'localPort'
        :return: Boolean.
                - True: Connection succeeded.
                - False: Error.
        """

        try:
            if sshConf is not None:
                self.server = sshtunnel.SSHTunnelForwarder(
                    ssh_address_or_host=(sshConf[u'sshHost'], sshConf[u'sshPort']),
                    remote_bind_address=(dbConf[u'dbHost'], dbConf[u'dbPort']),
                    local_bind_address=(sshConf[u'localHost'], sshConf[u'localPort']),
                    ssh_username=sshConf[u'sshUser'],
                    ssh_password=sshConf[u'sshPass']
                    )
                self.server.start()
                self.conn = msq.connect(
                    host=self.server.local_bind_host,
                    port=self.server.local_bind_port,
                    user=dbConf[u'dbUser'],
                    passwd=dbConf[u'dbPass'],
                    db=dbConf[u'dbName'],
                    charset=self.encoding
                    )
                self.isSSH = True
            else:
                self.conn = msq.connect(
                    host=dbConf[u'dbHost'],
                    port=dbConf[u'dbPort'],
                    user=dbConf[u'dbUser'],
                    passwd=dbConf[u'dbPass'],
                    db=dbConf[u'dbName'],
                    charset=self.encoding
                )
            return True
        except msq.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print u"*** ERROR: Something is wrong with your user name or password. ***"
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print u"*** ERROR: Database does not exists. ***"
            else:
                print u"*** ERROR: Check your connection or host name. ***"
            return False

    def close(self):
        """
        Función que permite cerrar la conexión actual a la base de datos.
        :return: Boolean.
                - True: Connection closed.
                - False: Error.
        """
        try:
            self.conn.close()
            if self.isSSH:
                self.server.stop()
            return True
        except:
            print u"*** ERROR: No connection to close. ***"
            return False

    # =================================
    # Metodos utilitarios
    # =================================

    def is_table(self, table_name):
        """
        Función que indica si una tabla existe o no en la base de datos.
        :param table_name: Str.
        :return: Boolean.
                - True: Table exist.
                - False: Table doesn't exist.
        """
        try:
            query = u"show tables like '%s'" % table_name
            cursor = self.conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            if len(result) > 0:
                return True
            else:
                return False
        except:
            return False

    def get_columns(self, table_name):
        """
        Función que devuelve los nombres de sus columnas y sus tipos de dato.
        :param table_name: Str.
        :return: names: List, types: List.
        """
        if self.is_table(table_name):
            query = u"select * from %s limit 0" % table_name
            cursor = self.conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()      # evitar errores por no uso
            result = np.array(cursor.description)
            cursor.close()
            names = u''
            types = u''
            column = len(result[:, 0])
            for col in range(column):
                if col < (column - 1):
                    names += result[col, 0] + u', '
                    types += self.field_type[result[col, 1]] + u', '
                else:
                    names += result[col, 0]
                    types += self.field_type[result[col, 1]]
            return names, types
        else:
            print u"*** ERROR: Table doesn't exists. ***"
            return None, None

    @staticmethod
    def enc_file(file_name):
        """
        Función que permite codificar un archivo para almacenarlo en la DB.
        :param file_name:  Str.
        :return: Str (coded).
        """
        file_data = open(file_name, u'r').read()
        return file_data.encode(u'base64')

    @staticmethod
    def dec_file(b64_file):
        """
        Función que permite decodificar un archivo luego de bajarlo de la DB.
        :param b64_file: Str (coded).
        :return: Str.
        """
        return b64_file.decode(u'base64')

    @staticmethod
    def to_numpy(data):
        """
        Convierte un conjunto de datos en un arreglo Numpy (de tipo 'object').
        :param data: Array/List.
        :return: Numpy Array.
        """
        if type(data) is not np.ndarray:
            return np.array(data, dtype=object)
        else:
            return data

    # =================================
    # Metodos para carga de datos
    # =================================

    def simple_mysql_save(self, query, data):
        """
        Función genérica para almacenar datos en una DB.
        :param query: Str.
        :param data: Array.
        :return: Boolean.
                - True: Data stored correctly.
                - False: Error.

        """

        indata = self.to_numpy(data)
        cursor = self.conn.cursor()
        try:
            if indata.ndim > 1:
                for line in range(len(indata[:, 0])):
                    sql = query % tuple(indata[line, :])
                    cursor.execute(sql)
            else:
                sql = query % tuple(indata)
                cursor.execute(sql)
            self.conn.commit()
            cursor.close()
            return True
        except:
            self.conn.rollback()
            cursor.close()
            return False

    def new_vino(self, data):
        """
        Función que permite almacenar datos en la tabla 'vinos'.
        :param data: Array.
                - Line format:  [nombre(str), tipo(str), vina(str), valle(str), ano(str), descripcion(str)]
        :return: Boolean.
                - True: Data stored correctly.
                - False: Error.
        """

        if self.is_table(u'vinos'):
            query = u"insert into vinos (nombre, tipo, vina, valle, ano, descripcion) value ('%s', '%s', '%s', '%s', '%d', '%s')"
            # Carga de datos
            return self.simple_mysql_save(query, data)
        else:
            print u"*** ERROR: Table doesn't exists. ***"
            return False

    def new_estanque(self, data):
        """
        Función que permite almacenar datos en la tabla 'estanques'.
        :param data: Array.
                - Line format:  [numero(int), descripcion(str)]
        :return: Boolean.
                - True: Data stored correctly.
                - False: Error.
        """

        if self.is_table(u'estanques'):
            query = u"insert into estanques (numero, descripcion) value ('%d', '%s')"
            # Carga de datos
            return self.simple_mysql_save(query, data)
        else:
            print "*** ERROR: Table doesn't exists. ***"
            return False

    def new_vino_in_estanque(self, data):
        """
        Función que permite almacenar datos en la tabla 'fechas_vinos', asociando temporalmente vinos y estanques.
        :param data: Array.
                - Line Format:  [estanques_id(int), vinos_id(int)]
        :return: Boolean.
                - True: Data stored correctly.
                - False: Error.
        """

        if self.is_table(u'vinos') and self.is_table(u'estanques') and \
           self.is_table(u'fechas_vinos'):
            query = u"insert into fechas_vinos (id_estanques, id_vinos) value ('%d', '%d')"
            # Carga de datos
            return self.simple_mysql_save(query, data)
        else:
            print u"*** ERROR: At least one of the tables required doesn't exists. ***"
            return False

    def new_parametro(self, parametros, espectro_id):
        """
        Función que permite almacenar datos en la tabla 'parametros', asociándolos a un espectro determinado.
        :param parametros: Array(float).
                - Line Format: [SO2L, SO2T, AV, `AT(Sulfurica)`, `AT(Tartarica)`, PH, MR, GA, Densidad]
        :param espectro_id: Int.
        :return: Boolean.
                - True: Data stored correctly.
                - False: Error.
        """

        if self.is_table(u'parametros'):
            query = u"insert into parametros " + \
                    u"(SO2L, SO2T, AV, `AT(Sulfurica)`, `AT(Tartarica)`, PH, MR, GA, Densidad, id_espectros) " + \
                    u"value ('%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%d')"
            # Preparar la data
            data = self.to_numpy(parametros)
            if data.ndim is 2:
                data = np.insert(data, 9, espectro_id, axis=1)
            else:
                data = np.insert(data, 9, espectro_id, axis=0)
            # Carga de datos
            return self.simple_mysql_save(query, data)
        else:
            print u"*** ERROR: Table doesn't exists. ***"
            return False

    def new_espectro(self, filename, vino_id, estanque_id):
        """
        Función que permite almacenar datos en la tabla 'espectros' y registrar este ingreso en la tabla
        'fechas_espectros', registrandolo temporalmente y asociándolo a un determinado vino/estanque.
        :param filename: Str.
        :param vino_id:  Int.
        :param estanque_id: Int.
        :return: Boolean.
                - True: Data stored correctly.
                - False: Error.
        """
        if self.is_table(u'vinos') and self.is_table(u'estanques') and self.is_table(u'espectros') and self.is_table(u'fechas_espectros'):
            # ----------
            query1 = u"insert into espectros (espectro, flag_procesado) value ('%s', '%d')"
            query2 = u"select last_insert_id()"
            query3 = u"insert into fechas_espectros (id_vinos, id_estanques, id_espectros) value ('%d', '%d', '%d')"
            # ----------
            cursor = self.conn.cursor()
            try:
                # Guardar el espectro
                enc_file = self.enc_file(filename)
                query1 = query1 % tuple([enc_file, 0])
                cursor.execute(query1)
                # Recuperar el ID
                cursor.execute(query2)
                res1 = cursor.fetchall()
                query3 = query3 % tuple([vino_id, estanque_id, res1[0][0]])
                cursor.execute(query3)
                # Realizar los cambios
                self.conn.commit()
                cursor.close()
                return True
            except:
                self.conn.rollback()
                cursor.close()
                return False
        else:
            print u"*** ERROR: At least one of the tables required doesn't exists. ***"
            return False

    # =================================
    # Metodos para recuperar datos
    # =================================

    def simple_mysql_read(self, query, data):
        """
        Función genérica para leer datos de una DB.
        :param query: Str.
        :param data: Tuple.
        :return: result: Array con datos de lectura
        """
        cursor = self.conn.cursor()
        try:
            # ---------
            sql = query % data
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
            return result
        except:
            cursor.close()
            return None

    def read_estanque(self, data):
        """
        Función que permite leer datos de la tabla 'estanques'.
        :param data: Tuple.
        :return: result: Array con datos de lectura.
        """
        if self.is_table(u'estanques'):
            query = u" select numero, descripcion, id_estanque from estanques " + \
                    u" where numero = '%d' "
            return self.simple_mysql_read(query, data)
        else:
            print u"*** ERROR: Table doesn't exists ***"
            return None

    def read_vino(self, metodo, data):
        """
        Función que permite leer datos de la tabla 'vinos' por año,
        viña o entre años.
        :param metodo: Str.
        :param data: Tuple.
        :return: result: Array con datos de lectura.
        """
        # Query base
        initquery = " select * from vinos "

        if self.is_table(u'vinos'):
            # Leer dependiendo del modo de lectura deseado
            # y de la cantidad de datos de entrada
            if metodo == u'ano':
                l = len(data)
                # Según cantidad de años completar query basica
                if l > 1:
                    if l == 2:
                        query = initquery + u" where ano between %d and %d "
                    else:
                        aux = u"where ano = %d"
                        concat = initquery
                        for i in range(l):
                            concat += aux
                            aux = u" or ano = %d "
                        query = concat
                else:
                    query = initquery + u" where ano = %d "
            # Leer tabla vinos por el nombre del vino
            elif metodo == u'nombre':
                l = len(data)
                # Leer uno o mas vinos
                if l > 1:
                    aux = u" where nombre = '%s' "
                    concat = initquery
                    for i in range(l):
                        concat += aux
                        aux = u" or nombre = '%s' "
                    query = concat
                else:
                    query = initquery + u" where nombre = '%s' "
            # Leer por tipo de vino
            elif metodo == u'tipo':
                l = len(data)
                # Leer uno o mas tipos de vino
                if l > 1:
                    aux = u" where tipo = '%s' "
                    concat = initquery
                    for i in range(l):
                        concat += aux
                        aux = u" or tipo = '%s' "
                    query = concat
                else:
                    query = initquery + u" where tipo = '%s' "
            return self.simple_mysql_read(query, tuple(data))
        else:
            print u"*** ERROR: Table doesn't exists ***"
            return None

    def read_fechavino(self, data):
        """
        Función que permite leer datos de la tabla 'fechas_vinos' por
        id del estanque correspondiente.
        :param data: Tuple.
        :return: result: Array con datos de lectura.
        """
        # Comprueba si la tabla existe y lee el dato correspondiente a id_estanque
        if self.is_table(u'fechas_vinos'):
            query = u" select fecha, id_vinos from fechas_vinos " + \
                    u" where id_estanques = '%d' "
            return self.simple_mysql_read(query, data)
        else:
            print u"*** ERROR: Table doesn't exists ***"
            return None

