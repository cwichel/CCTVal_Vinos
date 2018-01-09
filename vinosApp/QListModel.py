
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

