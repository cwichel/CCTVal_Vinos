
import os
import glob as gl
from PyQt4 import QtGui, QtCore, uic


# =============================================================================
# View Models
# =============================================================================
# =============================================== List-like
class listModel(QtCore.QAbstractListModel):
    def __init__(self, data=[], header=u'Empty', parent=None):
        QtCore.QAbstractListModel.__init__(self, parent)
        # ==============
        self.listData = data

    # ================================= Item Flags
    def flags(self, index):
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    # ================================= Data Presentation
    def data(self, index, role=None):                           # Element View

        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            value = self.listData[row]
            return value

    # ================================= Data Size
    def rowCount(self, parent=None, *args, **kwargs):
        return len(self.listData)

    def columnCount(self, parent=None, *args, **kwargs):
        return 1











