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

    def rowCount(self, parent):
        """
        Función que retorna el largo de la estructura asociada al modelo.
        :param parent:
        :return: int largo de la estructura
        """
        largo = len(self.model_list)
        return largo

    def data(self, index, role):
        """
        Función que retorna elemento del modelo correspondiente a index.
        :param index: int índice del modelo.
        :param role:
        :return: str nombre de archivo almacenado en modelo.
        """
        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            value = self.model_list[row]
            return value

    def flags(self, index):
        """
        Funcion que
        :param index:
        :return:
        """
        return QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable

    def insertRows(self, position, rows, parent=QtCore.QModelIndex()):
        """
        Funcion que inserta uno o más elementos de valor vacío al modelo desde la posición especificada.
        :param position: int posición de elemento a insertar.
        :param rows: int cantidad de elementos de valor vacío a insertar.
        :param parent:
        :return: bool: True después de ejecutar la función.
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
        :param position: int posición desde donde se comienza a eliminar elementos.
        :param rows: int cantidad de elementos a eliminar.
        :param parent:
        :return: bool: True después de ejecutar la función.
        """
        self.beginRemoveRows(parent, position, position + rows + 1)
        value = self.model_list[position]
        self.model_list.remove(value)
        self.endRemoveRows()
        return True

    def addNewValue(self, value):
        """
        Función
        :param value:
        :return:
        """
        try:
            self.insertRows(0, 1)
            self.model_list[0] = unicode(QtCore.QString(value))
            self.reset()
            return True
        except:
            return False

    def removeAllRows(self):
        self.model_list = []
        return True

    def consultData(self, index):
        return self.model_list[index]

    def consultItem(self, item):
        return item in self.model_list

    def consultIndex(self, item):
        if item in self.model_list:
            return self.model_list.index(item)
        else:
            print u'El item no se encuentra en la lista'
            return False

    def model_list(self):
        return self.model_list

