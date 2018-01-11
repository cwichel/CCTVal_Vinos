
from PyQt4 import QtCore, QtGui, uic
import os



class ListModel(QtCore.QAbstractListModel):

    def __init__(self, files = [], parent = None):

        QtCore.QAbstractListModel.__init__(self, parent)
        self.__files = files

    def rowCount(self, parent):
        largo = len(self.__files)
        return largo

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            name = [unicode(os.path.splitext(os.path.basename(itm))[0]) for itm in self.__files]
            date = [unicode(os.path.splitext(os.path.basename(itm))[1]) for itm in self.__files]
            self.__files[row] = name[row] + date[row]
            value = self.__files[row]
            return value

    def flags(self, index):
        return QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable

    def insertRows(self, position, rows, parent=QtCore.QModelIndex()):
        self.beginInsertRows(parent, position, position + rows - 1)
        for i in range(rows):
            defaultValue = u'Empty'
            self.__files.insert(position, defaultValue)
        self.endInsertRows()
        return True

    def removeRows(self, position, rows, parent=QtCore.QModelIndex()):
        self.beginRemoveRows(parent, position, position + rows + 1)
        value = self.__files[position]
        self.__files.remove(value)
        self.endRemoveRows()
        return True

    def addNewValue(self, value):
        try:
            self.insertRows(0, 1)
            self.__files[0] = unicode(QtCore.QString(value))
            self.reset()
            return True
        except:
            return False

    def removeAllRows(self):
        self.__files = []
        return True
