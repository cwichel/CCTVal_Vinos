#!/usr/bin/python
# -*- coding: latin5 -*-

# Libraries #####################################
import numpy as np
import mysql.connector as msq
from mysql.connector import errorcode


# Vinos dbClass #################################
class VinosDBL:
    def __init__(self):
        self.data = []
        self.encoding = 'latin5'
        self.field_type = {
            0:      "%f",                   # DECIMAL
            4:      "%f",				    # FLOAT
            5:      "%f",				    # DOUBLE
            1:      "%d",				    # TINY
            2:      "%d",				    # SHORT
            3:      "%d",				    # LONG
            9:      "%d",				    # INT24
            6:      "NULL",				    # NULL
            8:      "LONGLONG",			    # LONGLONG
            246:    "NEWDECIMAL",           # NEWDECIMAL
            247:    "INTERVAL",             # INTERVAL
            248:    "SET",                  # SET
            255:    "GEOMETRY", 		    # GEOMETRY
            14:     "NEWDATE",			    # NEWDATE
            7:      "TIMESTAMP",	        # TIMESTAMP
            13:     "%Y",				    # YEAR
            10:     "%Y-%m-%d",			    # DATE
            11:     "%H:%M:%S",			    # TIME
            12:     "%Y-%m-%d %H:%M:%S",    # DATETIME
            16:     "'%x'",				    # BIT
            15:     "'%s'",				    # VARCHAR
            249:    "'%s'",			        # TINY BLOB
            250:    "'%s'",			        # MEDIUM BLOB
            251:    "'%s'",			        # LONG BLOB
            252:    "'%s'",			        # BLOB
            253:    "'%s'",			        # VAR STRING
            254:    "'%s'"			        # STRING
            }

    # ================================= Conexión a la DB
    def connect(self, config):
        try:
            config['charset'] = self.encoding
            self.conn = msq.connect(**config)
        except msq.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print "*** ERROR: Something is wrong with your user name or password. ***"
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print "*** ERROR: Database does not exists. ***"
            else:
                print "*** ERROR: Check your connection or host name. ***"

    # -----------------------
    def close(self):
        try:
            self.conn.close()
        except:
            print "*** ERROR: No connection to close. ***"

    # ================================= Utilidades de la DB
    def is_table(self, table_name):
        try:
            query = "show tables like '%s'" % table_name
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

    # -----------------------
    def get_columns(self, table_name):
        if self.is_table(table_name):
            query = "select * from %s limit 0" % table_name
            cursor = self.conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()      # evitar errores por no uso
            result = np.array(cursor.description)
            cursor.close()
            names = ''
            types = ''
            column = len(result[:, 0])
            for col in range(column):
                if col < (column - 1):
                    names += result[col, 0] + ', '
                    types += self.field_type[result[col, 1]] + ', '
                else:
                    names += result[col, 0]
                    types += self.field_type[result[col, 1]]
            return names, types
        else:
            print "*** ERROR: Table doesn't exists. ***"
            return None, None

    # ================================= Utilitarios
    @staticmethod
    def enc_file(file_name):
        '''
        Función que permite codificar un archivo para almacenarlo en la DB.
        :param file_name:  Str.
        :return: Str (coded).
        '''
        file_data = open(file_name, 'r').read()
        return file_data.encode('base64')

    # -----------------------
    @staticmethod
    def dec_file(b64_file):
        '''
        Función que permite decodificar un archivo luego de bajarlo de la DB.
        :param b64_file: Str (coded).
        :return: Str.
        '''
        return b64_file.decode('base64')

    # -----------------------
    @staticmethod
    def to_numpy(data):
        '''
        Convierte un conjunto de datos en un arreglo Numpy (de tipo 'object').
        :param data: Array/List.
        :return: Numpy Array.
        '''
        if type(data) is not np.ndarray:
            return np.array(data, dtype=object)
        else:
            return data

    # ================================= Para carga de datos
    def simple_mysql_save(self, query, data):
        '''
        Función genérica para almacenar datos en una DB.
        :param query: Str.
        :param data: Array.
        :return: Boolean.
                - True: Data stored correctly.
                - False: Error.
        '''
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

    # -----------------------
    def new_vino(self, data):
        '''
        Función que permite almacenar datos en la tabla 'vinos'.
        :param data: Array.
                - Line format:  [nombre(str), tipo(str), vina(str), valle(str), ano(str), descripcion(str)]
        :return: Boolean.
                - True: Data stored correctly.
                - False: Error.
        '''
        if self.is_table('vinos'):
            query = "insert into vinos (nombre, tipo, vina, valle, ano, descripcion) value ('%s', '%s', '%s', '%s', '%d', '%s')"
            # Carga de datos
            return self.simple_mysql_save(query, data)
        else:
            print "*** ERROR: Table doesn't exists. ***"
            return False

    # -----------------------
    def new_estanque(self, data):
        '''
        Función que permite almacenar datos en la tabla 'estanques'.
        :param data: Array.
                - Line format:  [numero(int), descripcion(str)]
        :return: Boolean.
                - True: Data stored correctly.
                - False: Error.
        '''
        if self.is_table('estanques'):
            query = "insert into estanques (numero, descripcion) value ('%d', '%s')"
            # Carga de datos
            return self.simple_mysql_save(query, data)
        else:
            print "*** ERROR: Table doesn't exists. ***"
            return False

    # -----------------------
    def new_vino_in_estanque(self, data):
        '''
        Función que permite almacenar datos en la tabla 'fechas_vinos', asociando temporalmente vinos y estanques.
        :param data: Array.
                - Line Format:  [estanques_id(int), vinos_id(int)]
        :return: Boolean.
                - True: Data stored correctly.
                - False: Error.
        '''
        if self.is_table('vinos') and self.is_table('estanques') and \
           self.is_table('fechas_vinos'):
            query = "insert into fechas_vinos (estanques_id, vinos_id) value ('%d', '%d')"
            # Carga de datos
            return self.simple_mysql_save(query, data)
        else:
            print "*** ERROR: At least one of the tables required doesn't exists. ***"
            return False

    # -----------------------
    def new_parametro(self, parametros, espectro_id):
        '''
        Función que permite almacenar datos en la tabla 'parametros', asociándolos a un espectro determinado.
        :param parametros: Array(float).
                - Line Format: [SO2L, SO2T, AV, `AT(Sulfurica)`, `AT(Tartarica)`, PH, MR, GA, Densidad]
        :param espectro_id: Int.
        :return: Boolean.
                - True: Data stored correctly.
                - False: Error.
        '''
        if self.is_table('parametros'):
            query = "insert into parametros " + \
                    "(SO2L, SO2T, AV, `AT(Sulfurica)`, `AT(Tartarica)`, PH, MR, GA, Densidad, espectros_id) " + \
                    "value ('%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%d')"
            # Preparar a data
            data = self.to_numpy(parametros)
            if data.ndim is 2:
                data = np.insert(data, 9, espectro_id, axis=1)
            else:
                data = np.insert(data, 9, espectro_id, axis=0)
            # Carga de datos
            return self.simple_mysql_save(query, data)
        else:
            print "*** ERROR: Table doesn't exists. ***"
            return False

    # -----------------------
    def new_espectro(self, filename, vino_id, estanque_id):
        '''
        Función que permite almacenar datos en la tabla 'espectros' y registrar este ingreso en la tabla
        'fechas_espectros', registrandolo temporalmente y asociándolo a un determinado vino/estanque.
        :param filename: Str.
        :param vino_id:  Int.
        :param estanque_id: Int.
        :return: Boolean.
                - True: Data stored correctly.
                - False: Error.
        '''
        if self.is_table('vinos') and self.is_table('estanques') and self.is_table('espectros') and self.is_table('fechas_espectros'):
            # ----------
            query1 = "insert into espectros (espectro, flag_procesado) value ('%s', '%d')"
            query2 = "select last_insert_id()"
            query3 = "insert into fechas_espectros (vinos_id, estanques_id, espectros_id) value ('%d', '%d', '%d')"
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
            print "*** ERROR: At least one of the tables required doesn't exists. ***"
            return False

####LALO
    # =======================================
    def simple_mysql_read(self, query, data):
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


    # ================================


    # ================================
    # Lee datos de tabla estanques
    def read_estanque(self, data):
        if self.is_table('estanques'):
            query = " select numero, descripcion from estanques " + \
                    " where numero = '%d' "
            return self.simple_mysql_read(query, data)
        else:
            print "*** ERROR: Table doesn't exists ***"
            return None

    # Leer datos desde tabla vinos
    # Supuesto: Se accede a la tabla vinos por años, nombre y tipo

    def read_vino(self,metodo,data):

        initquery = " select * from vinos "

        if self.is_table('vinos'):

            if metodo == 'ano':
                l = len(data)
                if l > 1:
                    if l == 2:
                        query = initquery + " where ano between %d and %d "
                    else:

                        aux = "where ano = %d"
                        concat = initquery
                        for i in range(l):
                            concat += aux
                            aux = " or ano = %d "
                        query = concat
                else:
                    query = initquery + " where ano = %d "

            elif metodo == 'nombre':
                l = len(data)
                if l > 1:

                    aux = " where nombre = '%s' "
                    concat = initquery
                    for i in range(l):
                        concat += aux
                        aux = " or nombre = '%s' "
                    query = concat

                else:
                    query = initquery + " where nombre = '%s' "

            elif metodo == 'tipo':

                l = len(data)
                if l > 1:

                    aux = " where tipo = '%s' "
                    concat = initquery
                    for i in range(l):
                        concat += aux
                        aux = " or tipo = '%s' "
                    query = concat

                else:
                    query = initquery + " where tipo = '%s' "

            return self.simple_mysql_read(query, tuple(data))
        else:
            print "*** ERROR: Table doesn't exists ***"
            return None

    # Leer datos desde tabla espectros
    # Supuestos:
    # HEADER
    # Fecha: Se leen IDs de tablas espectros, estanques, vinos
    # Estanque: Se lee el número del estanque
    # Vino: Se lee el nombre, tipo y año del vino
    # DATA
    # Espectro: Se lee el espectro

    '''def read_espectro(self, data):

        select es.espectro, tk.numero, vn.nombre, vn.tipo, vn.ano
        from fechas_espectros as fe
        inner join espectros as es on es.id_espectro = fe.espectros_id
        inner join vinos as vn on vn.id_vinos = fe.vinos_id
        inner join estanques as tk on tk.id_estanques = fe.estanques_id

        where fe.fecha between '2017-12-01' and '2017-12-02'
        and es.flag_procesado = 0


        return None'''
































