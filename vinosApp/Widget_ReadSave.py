# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Widget_ReadSave.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

# ======================================================
# TRANSFORM FROM QT DESIGNER TO .PY
# pyuic4 -o Widget_ReadSave.py Widget_ReadSave.ui
# ======================================================

# ===========================================
#                  Modules
# ===========================================

import os
import csv
import glob
import shutil
import datetime

from VinosDBL import *
from QListModel import *
from random import *
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

# ===========================================
#
# ===========================================

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

# ===========================================
#               Clase Ui_Form
# ===========================================

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
        self.model_read = ListModel([])
        self.model_save = ListModel([])
        self.initModels()
        self.setAction()

# ===========================================
#              Ui_Form QtDesigner
# ===========================================

    def setupUi(self, ReadSaveData):
        ReadSaveData.setObjectName(_fromUtf8("ReadSaveData"))
        ReadSaveData.resize(692, 378)
        ReadSaveData.setMinimumSize(QtCore.QSize(550, 350))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(ReadSaveData)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.Tabs = QtGui.QTabWidget(ReadSaveData)
        self.Tabs.setMinimumSize(QtCore.QSize(450, 300))
        self.Tabs.setObjectName(_fromUtf8("Tabs"))
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
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(8)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_estanque = QtGui.QLabel(self.Adquirir)
        self.label_estanque.setMinimumSize(QtCore.QSize(90, 30))
        self.label_estanque.setMaximumSize(QtCore.QSize(90, 30))
        self.label_estanque.setAlignment(QtCore.Qt.AlignCenter)
        self.label_estanque.setObjectName(_fromUtf8("label_estanque"))
        self.horizontalLayout_4.addWidget(self.label_estanque)
        self.linedit_estanquein = QtGui.QLineEdit(self.Adquirir)
        self.linedit_estanquein.setMinimumSize(QtCore.QSize(150, 30))
        self.linedit_estanquein.setMaximumSize(QtCore.QSize(350, 30))
        self.linedit_estanquein.setObjectName(_fromUtf8("linedit_estanquein"))
        self.horizontalLayout_4.addWidget(self.linedit_estanquein)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label = QtGui.QLabel(self.Adquirir)
        self.label.setMinimumSize(QtCore.QSize(90, 30))
        self.label.setMaximumSize(QtCore.QSize(90, 30))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_6.addWidget(self.label)
        self.boton_estado = QtGui.QPushButton(self.Adquirir)
        self.boton_estado.setMinimumSize(QtCore.QSize(150, 30))
        self.boton_estado.setMaximumSize(QtCore.QSize(350, 30))
        self.boton_estado.setObjectName(_fromUtf8("boton_estado"))
        self.horizontalLayout_6.addWidget(self.boton_estado)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
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
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.groupBox = QtGui.QGroupBox(self.Adquirir)
        self.groupBox.setMinimumSize(QtCore.QSize(100, 200))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setSpacing(8)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setSpacing(8)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.listview_read = QtGui.QListView(self.groupBox)
        self.listview_read.setMinimumSize(QtCore.QSize(220, 70))
        self.listview_read.setMaximumSize(QtCore.QSize(1500, 150))
        self.listview_read.setObjectName(_fromUtf8("listview_read"))
        self.verticalLayout_9.addWidget(self.listview_read, QtCore.Qt.AlignHCenter)
        self.verticalLayout_7.addLayout(self.verticalLayout_9)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.verticalLayout_14 = QtGui.QVBoxLayout()
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.boton_load = QtGui.QPushButton(self.groupBox)
        self.boton_load.setMinimumSize(QtCore.QSize(95, 60))
        self.boton_load.setMaximumSize(QtCore.QSize(95, 70))
        self.boton_load.setObjectName(_fromUtf8("boton_load"))
        self.verticalLayout_14.addWidget(self.boton_load, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.horizontalLayout_7.addLayout(self.verticalLayout_14)
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.boton_clearall = QtGui.QPushButton(self.groupBox)
        self.boton_clearall.setMinimumSize(QtCore.QSize(95, 25))
        self.boton_clearall.setMaximumSize(QtCore.QSize(140, 30))
        self.boton_clearall.setObjectName(_fromUtf8("boton_clearall"))
        self.verticalLayout_12.addWidget(self.boton_clearall, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.boton_clearselect = QtGui.QPushButton(self.groupBox)
        self.boton_clearselect.setMinimumSize(QtCore.QSize(95, 25))
        self.boton_clearselect.setMaximumSize(QtCore.QSize(140, 30))
        self.boton_clearselect.setObjectName(_fromUtf8("boton_clearselect"))
        self.verticalLayout_12.addWidget(self.boton_clearselect, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.horizontalLayout_7.addLayout(self.verticalLayout_12)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.verticalLayout_13.addLayout(self.verticalLayout_7)
        self.horizontalLayout_8.addWidget(self.groupBox, QtCore.Qt.AlignHCenter)
        self.groupBox_2 = QtGui.QGroupBox(self.Adquirir)
        self.groupBox_2.setMinimumSize(QtCore.QSize(100, 200))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_17 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_17.setObjectName(_fromUtf8("verticalLayout_17"))
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.verticalLayout_15 = QtGui.QVBoxLayout()
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.listview_save = QtGui.QListView(self.groupBox_2)
        self.listview_save.setMinimumSize(QtCore.QSize(220, 70))
        self.listview_save.setMaximumSize(QtCore.QSize(1500, 150))
        self.listview_save.setObjectName(_fromUtf8("listview_save"))
        self.verticalLayout_15.addWidget(self.listview_save)
        self.verticalLayout_10.addLayout(self.verticalLayout_15)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.verticalLayout_20 = QtGui.QVBoxLayout()
        self.verticalLayout_20.setObjectName(_fromUtf8("verticalLayout_20"))
        self.boton_selecttosave = QtGui.QPushButton(self.groupBox_2)
        self.boton_selecttosave.setMinimumSize(QtCore.QSize(95, 25))
        self.boton_selecttosave.setMaximumSize(QtCore.QSize(140, 30))
        self.boton_selecttosave.setObjectName(_fromUtf8("boton_selecttosave"))
        self.verticalLayout_20.addWidget(self.boton_selecttosave, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.boton_clearsave = QtGui.QPushButton(self.groupBox_2)
        self.boton_clearsave.setMinimumSize(QtCore.QSize(95, 25))
        self.boton_clearsave.setMaximumSize(QtCore.QSize(140, 30))
        self.boton_clearsave.setObjectName(_fromUtf8("boton_clearsave"))
        self.verticalLayout_20.addWidget(self.boton_clearsave, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.horizontalLayout_9.addLayout(self.verticalLayout_20)
        self.verticalLayout_16 = QtGui.QVBoxLayout()
        self.verticalLayout_16.setObjectName(_fromUtf8("verticalLayout_16"))
        self.boton_save = QtGui.QPushButton(self.groupBox_2)
        self.boton_save.setMinimumSize(QtCore.QSize(95, 60))
        self.boton_save.setMaximumSize(QtCore.QSize(95, 70))
        self.boton_save.setObjectName(_fromUtf8("boton_save"))
        self.verticalLayout_16.addWidget(self.boton_save, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_9.addLayout(self.verticalLayout_16)
        self.verticalLayout_10.addLayout(self.horizontalLayout_9)
        self.verticalLayout_17.addLayout(self.verticalLayout_10)
        self.horizontalLayout_8.addWidget(self.groupBox_2, QtCore.Qt.AlignHCenter)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)
        self.verticalLayout_5.addLayout(self.verticalLayout_8)
        self.Tabs.addTab(self.Adquirir, _fromUtf8(""))
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

        # ======================================================
        #  Se modifica el archivo diseñado en QtDesigner para
        #  incluir clase figure para graficar espectros
        # ======================================================

        self.verticalLayout_19.addWidget(self.label_3)
        self.graphic = FigureCanvas(self.figure)
        self.graphics_view = NavigationToolbar(self.graphic, self)
        self.graphics_view.setMinimumSize(QtCore.QSize(450, 24))
        self.graphics_view.setObjectName(_fromUtf8("graphics_view"))
        self.verticalLayout_19.addWidget(self.graphics_view)
        self.verticalLayout_19.addWidget(self.graphic)

        # ======================================================

        self.verticalLayout_18.addLayout(self.verticalLayout_19)
        self.verticalLayout.addLayout(self.verticalLayout_18)
        self.Tabs.addTab(self.Visualizar, _fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.Tabs)

        self.retranslateUi(ReadSaveData)
        self.Tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ReadSaveData)

    def retranslateUi(self, ReadSaveData):
        ReadSaveData.setWindowTitle(_translate("ReadSaveData", "Adquisición y Visualización Espectros", None))
        self.label_estanque.setText(_translate("ReadSaveData", "  N° Estanque \n"
                                                               " a Analizar", None))
        self.boton_estado.setText(_translate("ReadSaveData", "Verificar", None))
        self.groupBox.setTitle(_translate("ReadSaveData", "Espectrómetro", None))
        self.boton_load.setText(_translate("ReadSaveData", "Adquirir", None))
        self.boton_clearall.setText(_translate("ReadSaveData", "Clear All", None))
        self.boton_clearselect.setText(_translate("ReadSaveData", "Clear Select", None))
        self.groupBox_2.setTitle(_translate("ReadSaveData", "Base de Datos", None))
        self.boton_selecttosave.setText(_translate("ReadSaveData", "Seleccionar", None))
        self.boton_clearsave.setText(_translate("ReadSaveData", "Clear Select", None))
        self.boton_save.setText(_translate("ReadSaveData", "Guardar a\n"
                                                           " Base de Datos", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.Adquirir), _translate("ReadSaveData", "Adquirir", None))
        self.label_comboboxplot.setText(_translate("ReadSaveData", "Espectros Adquiridos", None))
        self.label_3.setText(_translate("ReadSaveData", "TextLabel", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.Visualizar), _translate("ReadSaveData", "Visualizar", None))

    # ===========================================
    #          Metodos para clase Ui_Form
    # ===========================================

    def initModels(self):
        """
        Función que inicializa los modelos utilizados para  la lectura,
        escritura y visualización de espectros.
        """
        self.listview_read.setModel(self.model_read)
        self.combobox_plot.setModel(self.model_read)
        self.listview_save.setModel(self.model_save)

    def databaseConnect(self):
        """
        Función que realiza las configuraciones necesarias para la conexión
        a la base de datos de forma local o al servidor habilitado mediante
        túnel SSH.
        """
        # ssh hace el túnel hacia el servidor donde
        # esta instalada la base de datos
        sshConf = {
            u'sshHost': u'200.1.17.223',
            u'sshPort': 22,
            u'sshUser': u'spartan',
            u'sshPass': u'1Q2w3e4r5t6y7u8i9o0p',
            u'localHost': u'127.0.0.1',
            u'localPort': 3037
        }
        # el servidor corre una base de datos local
        # con al siguiente configuración
        dbConf = {
            u'dbHost': u'127.0.0.1',
            u'dbPort': 3306,
            u'dbUser': u'root',
            u'dbPass': u'1Q2w3e4r5t6y7u8i9o0p',
            u'dbName': u'vinosdb'
        }
        self.vinosDB.connect(dbConf=dbConf, sshConf=sshConf)
        print u'Conectado a Base de Datos:', self.vinosDB.conn.is_connected()

    def setAction(self):
        """
        Función que asocia cada evento en la interfaz con una acción
        determinada.
        """
        self.boton_estado.clicked.connect(lambda: self.boton_estadoHandler(tankName=self.linedit_estanquein.text()))
        self.boton_load.clicked.connect(lambda: self.boton_loadHandler())
        self.boton_clearall.clicked.connect(lambda: self.boton_clearallHandler())
        self.boton_clearselect.clicked.connect(lambda: self.boton_clearselectHandler())
        self.listview_read.selectionModel().selectionChanged.connect(lambda: self.listread2comboboxplot())
        self.combobox_plot.activated.connect(lambda: self.combobox_plotHandler())
        self.combobox_plot.activated.connect(lambda: self.plotEspectro())
        self.Tabs.currentChanged.connect(lambda: self.plotEspectro())
        self.boton_selecttosave.clicked.connect(lambda: self.boton_selecttosaveHandler())
        self.boton_clearsave.clicked.connect(lambda: self.boton_clearsaveHandler())
        self.boton_save.clicked.connect(lambda: self.boton_saveHandler())

    def resizeEvent(self, event):
        """
        Funcion que reajusta el tamaño del gráfico al cambiar el
        tamalo de la interfaz
        :param event:
        """
        if self.figure.get_axes():
            self.figure.tight_layout()

    def boton_estadoHandler(self, tankName):
        """
        Función que asocia una acción al oprimir el botón "boton_estado" (en GUI
        botón "Verificar", Pestaña Adquirir). La acción es verificar si el número
        de estanque ingresado existe en la tabla "estanques" de la base de datos.
        :param tankName: Str.
        """
        if not tankName:
            data = u'*** ERROR: No ha ingresado número de estanque ***'
            flag = 1
            self.display_row1(data, tankName, flag)
        else:
            flag = 0
            tankName = int(tankName)
            data = self.vinosDB.read_estanque(tankName)
            self.display_row1(data, tankName, flag)

    def display_row1(self, data, tankName, flag):
        """
        Función que despliega información asociada al número de estanque del
        parámetro "tankName", en objeto "display_estanques" (Pestaña Adquirir).
        Específicamente la información contenida en la tabla "estanques" de la
        base de datos (nombre, tipo vino, año y descripción).
        :param data: Tuple
        :param tankName: Str
        :param flag: Bool
        """
        self.display_estanques.clear()
        if flag == False:
            if not data:
                error = u'*** ERROR: Estanque N° %d No Existe***' % tankName
                self.display_estanques.append(u' %s' % error)
            else:
                num = data[0][0]
                desc = data[0][1].split(u', ')
                self.display_estanques.append(u' Estanque número: %s \t ' % num)
                for i in range(len(desc)):
                    self.display_estanques.append(u' %s' % desc[i])
        else:
            self.display_estanques.append(u' %s' % data)

    def boton_loadHandler(self):
        """
        Función que asocia una acción al oprimir el botón "boton_load" (en GUI
        botón "Adquirir", Pestaña Adquirir). La acción es cargar un espectro del
        directorio especificado y lo almacena en directorio temporal creado, en
        espera de visualización en gráfico o escritura a base de datos. También
        incluye el nombre del archivo cargado al modelo "model_read" para administrar
        los archivos a guardar o visualizar.
        """
        ts = unicode(datetime.datetime.now().strftime("- %Y-%m-%d %H-%M-%S"))
        path_read = "../data/Espectros_vino_21-03-2018/*.txt"
        # path_read = "../data/Espectros Vinos/*.txt"
        path_temp = "../data/Temporal_Load"
        if not os.path.isdir(path_temp):
            os.mkdir(path_temp)
        files = glob.glob(path_read)
        temp = files[randint(1, len(files) - 1)]
        name = unicode(os.path.splitext(os.path.basename(temp))[0])
        shutil.copy2(temp, path_temp)
        dst_name = 'Espectro'+' '+name+' '+ts+'.txt'
        os.rename(path_temp+'/'+name+'.txt', path_temp+'/'+dst_name)
        self.model_read.addNewValue(dst_name)
        self.model_read.reset()
        self.listview_read.setCurrentIndex(self.model_read.index(0))

    def boton_clearselectHandler(self):
        """
        Función que asocia una acción al oprimir el botón "boton_clearselect" (en GUI
        botón "Clear Select", Pestaña Adquirir). Elimina el archivo seleccionado en
        la lista "listview_read" del directorio temporal y del modelo "model_read".
        Luego de eliminar el archivo se actualiza el modelo "model_read" y la lista
        "listview_read".
        """
        path_temp = "../data/Temporal_Load/"
        itemIndex = self.listview_read.currentIndex().row()
        itemTotal = self.model_read.rowCount(None)
        if itemTotal is not 0 and itemIndex is not -1:
            item = self.model_read.consultData(itemIndex)
            if item not in self.model_save.model_list:
                name = self.model_read.consultData(itemIndex)
                os.remove(path_temp + name)
                self.model_read.removeRows(self.listview_read.currentIndex().row(), 1, QtCore.QModelIndex())
                self.model_read.reset()
                if itemIndex > 0:
                    self.listview_read.setCurrentIndex(self.model_read.index(itemIndex-1))
                else:
                    self.listview_read.setCurrentIndex(self.model_read.index(0))
            else:
                print u'El item a eliminar ha sido seleccionado para guardar'
        else:
            print u'No item selected/available!'

    def boton_clearallHandler(self):
        """
        Función que asocia una acción al oprimir el botón "boton_clearall" (en GUI
        botón "Clear All", Pestaña Adquirir). Elimina todos los archivos del directorio
        temporal, de la lista "listview_read" y del modelo "model_read". Luego de eliminar
        los archivos se actualiza el modelo "model_read" y la lista "listview_read".
        """
        path_temp = "../data/Temporal_Load/"
        aux_list = []
        for item in self.model_read.model_list:
            if item not in self.model_save.model_list:
                itemIndex = self.model_read.model_list.index(item)
                name = self.model_read.consultData(itemIndex)
                os.remove(path_temp + name)
            else:
                aux_list.append(item)
        self.model_read.model_list = aux_list
        self.model_read.model_list.sort()
        self.model_save.model_list.sort()
        self.model_read.reset()
        self.model_save.reset()

    def combobox_plotHandler(self):
        """
        Función que actualiza los índices correspondientes al modelo para ser
        visualizados en el gráfico (Pestaña Visualizar), según lo que se encuentra
        seleccionado en el combobox "combobox_plot" (Pestaña Visualizar).
        """
        itemIndex = self.combobox_plot.currentIndex()
        itemTotal = self.model_read.rowCount(None)
        if itemTotal is not 0 and itemIndex is not -1:
            if itemIndex > 0:
                self.listview_read.setCurrentIndex(self.model_read.index(itemIndex))
            else:
                self.listview_read.setCurrentIndex(self.model_read.index(0))
        else:
            print u'No item selected/available!'

    def listread2comboboxplot(self):
        """
        Asigna la seleccion en la lista "listview_read" a la seleccion
        en el combobox "combobox_plot" (Pestaña Visualizar), para visualizar el espectro
        seleccionado en la lista "listview_read" al cambiar de pestaña
        en la aplicación.
        """
        itemIndex = self.listview_read.currentIndex().row()
        self.combobox_plot.setCurrentIndex(itemIndex)

    def plotEspectro(self):
        """
        Funcion que grafica el espectro seleccionado en el combobox
        "combobox_plot" (Pestaña Visualizar). Al cambiar la selección en el combobox, se
        actualiza también el gráfico al espectro seleccionado.
        """
        path_temp = "../data/Temporal_Load/"
        itemTotal = self.model_read.rowCount(self)
        itemIndex = self.combobox_plot.currentIndex()
        if itemTotal is not 0 and itemIndex is not -1:
            name = self.model_read.consultData(itemIndex)
            file = open(path_temp + name, "r")
            datos = list(csv.reader(file, delimiter=','))
            n = len(datos[:])
            y = np.zeros((n-3, 1))
            for i in range(0, n-3):
                y[i] = float(datos[i+3][1])
            ax = self.figure.add_subplot(111)
            ax.clear()
            ax.spines["top"].set_visible(False)
            ax.spines["right"].set_visible(False)
            ax.get_xaxis().tick_bottom()
            ax.get_yaxis().tick_left()
            ax.set_xlabel("Frecuencia [Hz]", fontsize=12)
            ax.set_ylabel("Amplitud", fontsize=12)
            ax.plot(np.flipud(y), color='g')
            ax.axis('tight')
            self.figure.set_facecolor('white')
            self.graphics_view.draw()
            self.figure.tight_layout()

    def boton_selecttosaveHandler(self):
        """
        Función que asocia una acción al oprimir el botón "boton_selecttosave" (en GUI
        botón "Seleccionar", Pestaña Adquirir). Selecciona archivos de la lista "listview_read"
        relacionada al modelo "model_read", para visualizar en lista "listview_save" y guardar
        en modelo "model_save".
        """
        itemTotal = self.model_read.rowCount(self)
        itemIndex = self.listview_read.currentIndex().row()
        if itemTotal is not 0 and itemIndex is not -1:
            name = self.model_read.consultData(itemIndex)
            if not self.model_save.consultItem(name):
                self.model_save.addNewValue(name)
                self.model_save.reset()
                self.listview_save.setCurrentIndex(self.model_save.index(0))
            else:
                print u'Espectro ya fue seleccionado'
        else:
            print u'Item no seleccionado/disponible!'

    def boton_clearsaveHandler(self):
        """
        Función que asocia una acción al oprimir el botón "boton_clearsave" (en GUI
        botón "Clear Select", Pestaña Adquirir). Elimina el archivo seleccionado en
        la lista "listview_save" y del modelo "model_save". Luego de eliminar el archivo
        de la lista se actualiza el modelo "model_save" y la lista "listview_save".
        """
        itemIndex = self.listview_save.currentIndex().row()
        itemTotal = self.model_save.rowCount(None)
        if itemTotal is not 0 and itemIndex is not -1:
            self.model_save.removeRows(self.listview_save.currentIndex().row(), 1, QtCore.QModelIndex())
            self.model_save.reset()
            if itemIndex > 0:
                self.listview_save.setCurrentIndex(self.model_save.index(itemIndex - 1))
            else:
                self.listview_save.setCurrentIndex(self.model_save.index(0))
        else:
            print u'No item selected/available!'

    def boton_saveHandler(self):
        """
        Función que asocia una acción al oprimir el botón "boton_save" (en GUI
        botón "Guardar a Base de Datos", Pestaña Adquirir). La acción es guardar
        el espectro seleccionado en la lista "listview_save" a la base de datos
        y actualizar el modelo "model save" luego de realizada la carga del archivo.
        """
        tankName = self.linedit_estanquein.text()
        if not tankName:
            data = u'*** ERROR: No ha ingresado número de estanque *** \n ' \
                   u'Debe ingresar estanque para almacenar espectro en base de datos!'
            flag = 1
            self.display_row1(data, tankName, flag)
        else:
            tankName = int(tankName)
            path_temp = "../data/Temporal_Load/"
            itemIndex = self.listview_save.currentIndex().row()
            itemTotal = self.model_save.rowCount(None)
            if itemTotal is not 0 and itemIndex is not -1:
                if tankName is not None:
                    data_estanque = self.vinosDB.read_estanque(tankName)
                    id_estanque = data_estanque[0][2]
                    data_vinos = self.vinosDB.read_fechavino(id_estanque)
                    id_vino = data_vinos[0][1]
                    item = self.model_save.model_list[itemIndex]
                    filename = path_temp + item
                    self.vinosDB.new_espectro(filename, id_vino, id_estanque)
                    itemIndexRead = self.model_read.model_list.index(item)
                    self.model_save.removeRows(itemIndex, 1)
                    self.model_read.removeRows(itemIndexRead, 1)
                    os.remove(filename)
            else:
                print u'No ha seleccionado/adquirido espectro para guardar!'

    def closeEvent(self, event):
        """
        Función que asocia una acción al evento de cierre de la aplicación.
        Limpia los archivos almacenados en el directorio temporal, limpia los
        nombres contenidos en los modelos, cierra la conexión a la base de
        datos y cierra la aplicación.
        """
        path_temp = "../data/Temporal_Load/*.txt"
        files = glob.glob(path_temp)
        for file in files:
            os.remove(file)
        self.model_read.removeAllRows()
        self.model_save.removeAllRows()
        self.model_read.reset()
        self.model_save.reset()
        self.vinosDB.close()
        self.close()


