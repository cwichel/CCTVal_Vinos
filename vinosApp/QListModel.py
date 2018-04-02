# coding=utf-8
# Import models
from PyQt4 import QtCore, QtGui, uic

class ListModel(QtCore.QAbstractListModel):

    # Inicialización
    def __init__(self, files = [], parent = None):

        QtCore.QAbstractListModel.__init__(self, parent)
        self.model_list = files

    # =================================
    #      Metodos utilitarios
    # =================================

    def rowCount(self, parent = None):
        """
        Función que retorna el largo de la estructura asociada al modelo.
        :param parent: None, se ignora el parámetro pues se trabaja con lista
                       simplemente enlazada.
        :return: Int: largo de la estructura
        """
        largo = len(self.model_list)
        return largo

    def data(self, index, role):
        """
        Función que retorna elemento del modelo correspondiente a index.
        :param index: Int : índice del elemento en el modelo.
        :param role: método para retornar diferentes tipos de datos, por
                     ahora sólo se utilizará el método "Display" para retornar
                     Strings.
        :return: Str: nombre de archivo almacenado en modelo.
        """
        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            value = self.model_list[row]
            return value

    def flags(self, index):
        """
        Función que habilita la selección, visualización y edición de los elementos del modelo.
        """
        return QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable

    def insertRows(self, position, rows, parent=QtCore.QModelIndex()):
        """
        Funcion que inserta uno o más elementos de valor vacío al modelo desde la posición especificada.
        :param position: Int: posición de elemento a insertar.
        :param rows: Int: cantidad de elementos de valor vacío a insertar.
        :param parent: Int: index del el primer item del modelo.
        :return: Bool: True después de ejecutar la función.
        """
        self.beginInsertRows(parent, position, position + rows - 1)
        for i in range(rows):
            defaultValue = u'Empty'
            self.model_list.insert(position, defaultValue)
        self.endInsertRows()
        return True

    def removeRows(self, position, rows, parent=QtCore.QModelIndex()):
        """
        Funcion que elimina uno o más elementos del modelo desde la posición especificada.
        :param position: Int: posición desde donde se comienza a eliminar elementos.
        :param rows: Int: cantidad de elementos a eliminar.
        :param parent: Int: index del el primer item del modelo.
        :return: Bool: True después de ejecutar la función.
        """
        self.beginRemoveRows(parent, position, position + rows + 1)
        value = self.model_list[position]
        self.model_list.remove(value)
        self.endRemoveRows()
        return True

    def addNewValue(self, value):
        """
        Función que inserta un elemento "value" no vacío al modelo en la posición
        cero por defecto.
        :param value: Str: nombre de archivo.
        :return: Bool:
                - True: inserta el elemento al modelo.
                - False: ocurre un error al insertar elemento.
        """
        try:
            self.insertRows(0, 1)
            self.model_list[0] = unicode(QtCore.QString(value))
            self.reset()
            return True
        except:
            return False

    def removeAllRows(self):
        """
        Función que vacía la estructura de datos asociada al modelo (lista simple).
        :return: Bool: True después de ejecutar la función.
        """
        self.model_list = []
        return True

    def consultData(self, index):
        """
        Función que consulta el elemento o dato del modelo en la posición index.
        :param index: Int: posición del elemento que se desea consultar.
        :return: Str: nombre de archivo almacenado en posición index.
        """
        return self.model_list[index]

    def consultItem(self, item):
        """
        Función que consulta si el item de entrada se encuentra en la estructura
        asociada al modelo.
        :param:  item: Str: nombre de archivo de espectro.
        :return: Bool:
                - True: el item de entrada se encuentra en el modelo
                - False: el item de entrada no se encuentra en el modelo..
        """
        return item in self.model_list

    def consultIndex(self, item):
        """
        Función que consulta por el index del item de entrada si se encuentra en
        el modelo.
        :param item: Str: nombre de archivo de espectro.
        :return: Int: index del item consultado.
                 Bool: False, si el item no se encuentra en el modelo.
        """
        if item in self.model_list:
            return self.model_list.index(item)
        else:
            print u'El item no se encuentra en la lista'
            return False

    def model_list(self):
        """
        Función que retorna la estructura de datos del modelo "model_list"(lista simple).
        :return: List: lista simplemente enlazada asociada al modelo.
        """
        return self.model_list

