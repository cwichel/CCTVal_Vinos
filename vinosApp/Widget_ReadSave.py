# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Widget_ReadSave.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

########################################################
#TRANSFORM FROM QT DESIGNER TO .PY
#pyuic4 -o Widget_ReadSave.py Widget_ReadSave.ui
########################################################



import os
import glob
import csv
import shutil
import datetime

from VinosDBL import *
from QListModel import *
from random import *
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(QtGui.QWidget):

    def __init__(self):
        # Declaración de elementos
        QtGui.QWidget.__init__(self)
        self.vinosDB = VinosDBL()
        self.figure = Figure()
        # ==============
        # Activación Elementos
        self.setupUi(self)
        self.databaseConnect()
        # ==============
        # Inicializando Modelos
        self.model = ListModel([])
        self.initModels()
        self.setAction()

##################################################################
################### Upgradeable de QtDesigner ####################
##################################################################

    def setupUi(self, ReadSaveData):
        ReadSaveData.setObjectName(_fromUtf8("ReadSaveData"))
        ReadSaveData.resize(664, 468)
        ReadSaveData.setMinimumSize(QtCore.QSize(550, 350))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(ReadSaveData)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.ventanacompleta = QtGui.QTabWidget(ReadSaveData)
        self.ventanacompleta.setMinimumSize(QtCore.QSize(450, 300))
        self.ventanacompleta.setObjectName(_fromUtf8("ventanacompleta"))
        self.Adquirir = QtGui.QWidget()
        self.Adquirir.setMinimumSize(QtCore.QSize(400, 300))
        self.Adquirir.setObjectName(_fromUtf8("Adquirir"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.Adquirir)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_estanque = QtGui.QLabel(self.Adquirir)
        self.label_estanque.setMinimumSize(QtCore.QSize(145, 30))
        self.label_estanque.setMaximumSize(QtCore.QSize(250, 30))
        self.label_estanque.setAlignment(QtCore.Qt.AlignCenter)
        self.label_estanque.setObjectName(_fromUtf8("label_estanque"))
        self.verticalLayout_7.addWidget(self.label_estanque)
        self.linedit_estanquein = QtGui.QLineEdit(self.Adquirir)
        self.linedit_estanquein.setMinimumSize(QtCore.QSize(198, 30))
        self.linedit_estanquein.setMaximumSize(QtCore.QSize(250, 30))
        self.linedit_estanquein.setObjectName(_fromUtf8("linedit_estanquein"))
        self.verticalLayout_7.addWidget(self.linedit_estanquein)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_estado = QtGui.QLabel(self.Adquirir)
        self.label_estado.setMinimumSize(QtCore.QSize(95, 30))
        self.label_estado.setMaximumSize(QtCore.QSize(140, 30))
        self.label_estado.setAlignment(QtCore.Qt.AlignCenter)
        self.label_estado.setObjectName(_fromUtf8("label_estado"))
        self.verticalLayout_4.addWidget(self.label_estado)
        self.boton_estado = QtGui.QPushButton(self.Adquirir)
        self.boton_estado.setMinimumSize(QtCore.QSize(95, 30))
        self.boton_estado.setMaximumSize(QtCore.QSize(140, 30))
        self.boton_estado.setObjectName(_fromUtf8("boton_estado"))
        self.verticalLayout_4.addWidget(self.boton_estado)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.display_estanques = QtGui.QTextBrowser(self.Adquirir)
        self.display_estanques.setMinimumSize(QtCore.QSize(195, 90))
        self.display_estanques.setMaximumSize(QtCore.QSize(250, 150))
        self.display_estanques.setObjectName(_fromUtf8("display_estanques"))
        self.verticalLayout_3.addWidget(self.display_estanques)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setSpacing(8)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.label_read = QtGui.QLabel(self.Adquirir)
        self.label_read.setMinimumSize(QtCore.QSize(95, 30))
        self.label_read.setMaximumSize(QtCore.QSize(200, 30))
        self.label_read.setAlignment(QtCore.Qt.AlignCenter)
        self.label_read.setObjectName(_fromUtf8("label_read"))
        self.verticalLayout_10.addWidget(self.label_read)
        self.boton_load = QtGui.QPushButton(self.Adquirir)
        self.boton_load.setMinimumSize(QtCore.QSize(95, 30))
        self.boton_load.setMaximumSize(QtCore.QSize(95, 30))
        self.boton_load.setObjectName(_fromUtf8("boton_load"))
        self.verticalLayout_10.addWidget(self.boton_load)
        self.horizontalLayout_3.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.read_bar = QtGui.QProgressBar(self.Adquirir)
        self.read_bar.setMinimumSize(QtCore.QSize(198, 30))
        self.read_bar.setMaximumSize(QtCore.QSize(295, 30))
        self.read_bar.setProperty("value", 24)
        self.read_bar.setObjectName(_fromUtf8("read_bar"))
        self.horizontalLayout_7.addWidget(self.read_bar)
        self.verticalLayout_11.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.boton_clearall = QtGui.QPushButton(self.Adquirir)
        self.boton_clearall.setMinimumSize(QtCore.QSize(95, 30))
        self.boton_clearall.setMaximumSize(QtCore.QSize(140, 30))
        self.boton_clearall.setObjectName(_fromUtf8("boton_clearall"))
        self.horizontalLayout_6.addWidget(self.boton_clearall)
        self.boton_clearselect = QtGui.QPushButton(self.Adquirir)
        self.boton_clearselect.setMinimumSize(QtCore.QSize(95, 30))
        self.boton_clearselect.setMaximumSize(QtCore.QSize(140, 30))
        self.boton_clearselect.setObjectName(_fromUtf8("boton_clearselect"))
        self.horizontalLayout_6.addWidget(self.boton_clearselect)
        self.verticalLayout_11.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.listview_read = QtGui.QListView(self.Adquirir)
        self.listview_read.setMinimumSize(QtCore.QSize(195, 90))
        self.listview_read.setMaximumSize(QtCore.QSize(250, 150))
        self.listview_read.setObjectName(_fromUtf8("listview_read"))
        self.verticalLayout_12.addWidget(self.listview_read)
        self.horizontalLayout_3.addLayout(self.verticalLayout_12)
        self.verticalLayout_9.addLayout(self.horizontalLayout_3)
        self.verticalLayout_5.addLayout(self.verticalLayout_9)
        self.verticalLayout_13 = QtGui.QVBoxLayout()
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(8)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_14 = QtGui.QVBoxLayout()
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.label_save = QtGui.QLabel(self.Adquirir)
        self.label_save.setMinimumSize(QtCore.QSize(95, 30))
        self.label_save.setMaximumSize(QtCore.QSize(95, 30))
        self.label_save.setAlignment(QtCore.Qt.AlignCenter)
        self.label_save.setObjectName(_fromUtf8("label_save"))
        self.verticalLayout_14.addWidget(self.label_save)
        self.boton_save = QtGui.QPushButton(self.Adquirir)
        self.boton_save.setMinimumSize(QtCore.QSize(95, 30))
        self.boton_save.setMaximumSize(QtCore.QSize(95, 30))
        self.boton_save.setObjectName(_fromUtf8("boton_save"))
        self.verticalLayout_14.addWidget(self.boton_save)
        self.horizontalLayout_4.addLayout(self.verticalLayout_14)
        self.verticalLayout_15 = QtGui.QVBoxLayout()
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.label_savebar = QtGui.QLabel(self.Adquirir)
        self.label_savebar.setMinimumSize(QtCore.QSize(198, 30))
        self.label_savebar.setMaximumSize(QtCore.QSize(295, 30))
        self.label_savebar.setAlignment(QtCore.Qt.AlignCenter)
        self.label_savebar.setObjectName(_fromUtf8("label_savebar"))
        self.verticalLayout_15.addWidget(self.label_savebar)
        self.save_bar = QtGui.QProgressBar(self.Adquirir)
        self.save_bar.setMinimumSize(QtCore.QSize(198, 30))
        self.save_bar.setMaximumSize(QtCore.QSize(295, 30))
        self.save_bar.setProperty("value", 24)
        self.save_bar.setObjectName(_fromUtf8("save_bar"))
        self.verticalLayout_15.addWidget(self.save_bar)
        self.horizontalLayout_4.addLayout(self.verticalLayout_15)
        self.verticalLayout_16 = QtGui.QVBoxLayout()
        self.verticalLayout_16.setObjectName(_fromUtf8("verticalLayout_16"))
        self.list_saved = QtGui.QListView(self.Adquirir)
        self.list_saved.setMinimumSize(QtCore.QSize(195, 90))
        self.list_saved.setMaximumSize(QtCore.QSize(250, 150))
        self.list_saved.setObjectName(_fromUtf8("list_saved"))
        self.verticalLayout_16.addWidget(self.list_saved)
        self.horizontalLayout_4.addLayout(self.verticalLayout_16)
        self.verticalLayout_13.addLayout(self.horizontalLayout_4)
        self.verticalLayout_5.addLayout(self.verticalLayout_13)
        self.ventanacompleta.addTab(self.Adquirir, _fromUtf8(""))
        self.Visualizar = QtGui.QWidget()
        self.Visualizar.setMinimumSize(QtCore.QSize(400, 300))
        self.Visualizar.setObjectName(_fromUtf8("Visualizar"))
        self.verticalLayout = QtGui.QVBoxLayout(self.Visualizar)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setSpacing(8)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_comboboxplot = QtGui.QLabel(self.Visualizar)
        self.label_comboboxplot.setMinimumSize(QtCore.QSize(120, 25))
        self.label_comboboxplot.setMaximumSize(QtCore.QSize(100, 25))
        self.label_comboboxplot.setObjectName(_fromUtf8("label_comboboxplot"))
        self.horizontalLayout_5.addWidget(self.label_comboboxplot)
        self.combobox_plot = QtGui.QComboBox(self.Visualizar)
        self.combobox_plot.setMinimumSize(QtCore.QSize(340, 25))
        self.combobox_plot.setMaximumSize(QtCore.QSize(1000, 25))
        self.combobox_plot.setObjectName(_fromUtf8("combobox_plot"))
        self.horizontalLayout_5.addWidget(self.combobox_plot)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_18 = QtGui.QVBoxLayout()
        self.verticalLayout_18.setObjectName(_fromUtf8("verticalLayout_18"))
        self.verticalLayout_19 = QtGui.QVBoxLayout()
        self.verticalLayout_19.setObjectName(_fromUtf8("verticalLayout_19"))
        self.label_3 = QtGui.QLabel(self.Visualizar)
        self.label_3.setMinimumSize(QtCore.QSize(250, 25))
        self.label_3.setMaximumSize(QtCore.QSize(400, 25))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_19.addWidget(self.label_3)

        #########################################################

        # self.graphics_view = QtGui.QGraphicsView(self.Visualizar)
        # self.graphics_view.setMinimumSize(QtCore.QSize(450, 145))
        # self.graphics_view.setObjectName(_fromUtf8("graphics_view"))
        # self.verticalLayout_19.addWidget(self.graphics_view)

        self.graphic = FigureCanvas(self.figure)
        self.graphics_view = NavigationToolbar(self.graphic, self)
        self.graphics_view.setMinimumSize(QtCore.QSize(450, 24))
        self.graphics_view.setObjectName(_fromUtf8("graphics_view"))
        self.verticalLayout_19.addWidget(self.graphics_view)
        self.verticalLayout_19.addWidget(self.graphic)

        ########################################################

        self.verticalLayout_18.addLayout(self.verticalLayout_19)
        self.verticalLayout.addLayout(self.verticalLayout_18)
        self.ventanacompleta.addTab(self.Visualizar, _fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.ventanacompleta)

        self.retranslateUi(ReadSaveData)
        self.ventanacompleta.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(ReadSaveData)

    def retranslateUi(self, ReadSaveData):
        ReadSaveData.setWindowTitle(_translate("ReadSaveData", "Form", None))
        self.label_estanque.setText(_translate("ReadSaveData", "  N° Estanque", None))
        self.label_estado.setText(_translate("ReadSaveData", "  Estado", None))
        self.boton_estado.setText(_translate("ReadSaveData", "Verificar", None))
        self.label_read.setText(_translate("ReadSaveData", "Adquirir\n"
                                                           "Espectro", None))
        self.boton_load.setText(_translate("ReadSaveData", "Adquirir", None))
        self.boton_clearall.setText(_translate("ReadSaveData", "Clear All", None))
        self.boton_clearselect.setText(_translate("ReadSaveData", "Clear Select", None))
        self.label_save.setText(_translate("ReadSaveData", "Guardar", None))
        self.boton_save.setText(_translate("ReadSaveData", "Ok", None))
        self.label_savebar.setText(_translate("ReadSaveData", "Listo?", None))
        self.ventanacompleta.setTabText(self.ventanacompleta.indexOf(self.Adquirir),
                                        _translate("ReadSaveData", "Tab 1", None))
        self.label_comboboxplot.setText(_translate("ReadSaveData", "Espectros Adquiridos", None))
        self.label_3.setText(_translate("ReadSaveData", "TextLabel", None))
        self.ventanacompleta.setTabText(self.ventanacompleta.indexOf(self.Visualizar),
                                        _translate("ReadSaveData", "Tab 2", None))

##################################################################
################### Desarrollo de Aplicacion #####################
##################################################################

    def initModels(self):
        self.listview_read.setModel(self.model)
        self.combobox_plot.setModel(self.model)

    def databaseConnect(self):
        # Configuración de la DB y conexión:
        db_config = {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'passwd': '',
            'db': 'vinosdb'
        }
        self.vinosDB.connect(db_config)

    def setAction(self):
        self.boton_estado.clicked.connect(lambda: self.boton_estadoHandler(tankName = self.linedit_estanquein.text()))
        self.boton_load.clicked.connect(lambda: self.boton_loadHandler())
        self.boton_clearall.clicked.connect(lambda: self.boton_clearallHandler())
        self.boton_clearselect.clicked.connect(lambda: self.boton_clearselectHandler())
        self.listview_read.selectionModel().selectionChanged.connect(lambda: self.listread2comboboxplot())
        self.combobox_plot.activated.connect(lambda: self.combobox_plotHandler())
        self.combobox_plot.activated.connect(lambda: self.plotEspectro())
        self.ventanacompleta.currentChanged.connect(lambda: self.plotEspectro())


    def resizeEvent(self, event):
        if self.figure.get_axes():
            self.figure.tight_layout()

    def boton_estadoHandler(self, tankName):
        tankName = int(tankName)
        data = self.vinosDB.read_estanque(tankName)
        self.display_row1(data, tankName)

    def display_row1(self, data, tankName):
        self.display_estanques.clear()
        if not data:
            error = u'*** ERROR: Estanque N° %d No Existe***' % tankName
            self.display_estanques.append(u' %s' % error)
        else:
            num = data[0][0]
            desc = data[0][1].split(u', ')
            self.display_estanques.append(u' Estanque número: %s \t ' % num)
            for i in range(len(desc)):
                self.display_estanques.append(u' %s' % desc[i])

    def boton_loadHandler(self):
        # cacho de copiar y renombrar
        ts = unicode(datetime.datetime.now().strftime("- %Y-%m-%d %H-%M-%S"))
        path_read = "../data/Espectros/*.txt"
        path_temp = "../data/Temporal/"
        if not os.path.isdir(path_temp):
            os.mkdir(path_temp)
        files = glob.glob(path_read)
        temp = files[randint(1, len(files) - 1)]
        name = unicode(os.path.splitext(os.path.basename(temp))[0])
        shutil.copy2(temp, path_temp)
        dst_name = 'Espectro'+' '+name+' '+ts+'.txt'
        os.rename(path_temp+'/'+name+'.txt', path_temp+'/'+dst_name)
        # agregar al modelo
        self.model.addNewValue(dst_name)
        self.model.reset()
        self.listview_read.setCurrentIndex(self.model.index(0))

    def boton_clearselectHandler(self):
        path_temp = "../data/Temporal/"
        itemIndex = self.listview_read.currentIndex().row()
        itemTotal = self.model.rowCount(None)
        if itemTotal is not 0 and itemIndex is not -1:
            name = self.model.consultData(itemIndex)
            os.remove(path_temp + name)
            self.model.removeRows(self.listview_read.currentIndex().row(), 1, QtCore.QModelIndex())
            self.model.reset()
            if itemIndex > 0:
                self.listview_read.setCurrentIndex(self.model.index(itemIndex-1))
            else:
                self.listview_read.setCurrentIndex(self.model.index(0))
        else:
            print u'No item selected/available!'

    def boton_clearallHandler(self):
        path_temp = "../data/Temporal/*.txt"
        files = glob.glob(path_temp)
        for file in files:
            os.remove(file)
        self.model.removeAllRows()
        self.model.reset()

    def combobox_plotHandler(self):
        itemIndex = self.combobox_plot.currentIndex()
        itemTotal = self.model.rowCount(None)
        if itemTotal is not 0 and itemIndex is not -1:
            if itemIndex > 0:
                self.listview_read.setCurrentIndex(self.model.index(itemIndex))
            else:
                self.listview_read.setCurrentIndex(self.model.index(0))
        else:
            print u'No item selected/available!'

    def listread2comboboxplot(self):
        itemIndex = self.listview_read.currentIndex().row()
        self.combobox_plot.setCurrentIndex(itemIndex)

    def plotEspectro(self):
        path_temp = "../data/Temporal/"
        itemTotal = self.model.rowCount(self)
        itemIndex = self.combobox_plot.currentIndex()
        if itemTotal is not 0 and itemIndex is not -1:
            name = self.model.consultData(itemIndex)
            file = open(path_temp + name, "r")
            datos = list(csv.reader(file, delimiter=','))
            n = len(datos[:])
            X = np.zeros((n-1, 1))
            Y = np.zeros((n-1, 1))
            for i in range(0, n-1):
                X[i] = float(datos[i+1][0])
                Y[i] = float(datos[i+1][1])
            ax = self.figure.add_subplot(111)
            ax.clear()
            ax.spines["top"].set_visible(False)
            ax.spines["right"].set_visible(False)
            ax.get_xaxis().tick_bottom()
            ax.get_yaxis().tick_left()
            ax.set_xlabel("Frecuencia [Hz]", fontsize=12)
            ax.set_ylabel("Amplitud", fontsize=12)
            ax.plot(X, np.flipud(Y), color='g')
            ax.axis('tight')
            self.figure.set_facecolor('white')
            self.graphics_view.draw()
            self.figure.tight_layout()

    def closeEvent(self, event):
        self.boton_clearallHandler()






















# implementacion tonta
####def boton_clearallHandler(self):
####    self.modelList = []
####    model = ListModel(self.modelList)
####    self.listview_read.setModel(model)

####def boton_loadHandler(self):###
####    ts = datetime.datetime.now().strftime(" - %Y-%m-%d %H:%M:%S")
####    path = "../data/Espectros/*.txt"
####    files = glob.glob(path)
####    temp = files[randint(1, len(files)-1)] + ts
####    self.modelList.append(temp)
####    model = ListModel(self.modelList)
####    self.listview_read.setModel(model)

####def boton_clearselectHandler(self):
####    itemIndex = self.listview_read.currentIndex().row()
####    itemTotal = len(self.modelList)
####    if itemTotal is not 0 and itemIndex is not -1:
####        print u'Modifying item...'
####        del self.modelList[itemIndex]
####        model = ListModel(self.modelList)
####        self.listview_read.setModel(model)
####    else:
####        print u'No item selected/available!














