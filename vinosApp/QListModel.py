
from PyQt4 import QtCore, QtGui, uic
import os




class ListModel(QtCore.QAbstractListModel):

    def __init__(self, files = [], parent = None):

        QtCore.QAbstractListModel.__init__(self, parent)
        self.__files = files

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return QtCore.QString("Espectros Adquiridos")
            else:
                return QtCore.QString("Espectro %d").arg(section)

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

    # def flags(self, index):
    #     return QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable
    #
    #
    # def clearData(self, index, role = QtCore.Qt.EditRole):
    #
    #     if role == QtCore.Qt.EditRole:
    #         row = index.row()
    #         del self.__files[row]
    #         return true
    #     return false