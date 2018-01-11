

## Esto debe ir en vez del graphicview_plot

self.graphic = FigureCanvas(self.figure)
self.graphics_view = NavigationToolbar(self.graphic, self)
self.graphics_view.setMinimumSize(QtCore.QSize(450, 25))
self.graphics_view.setObjectName(_fromUtf8("graphics_view"))
self.verticalLayout_19.addWidget(self.graphics_view)
self.verticalLayout_19.addWidget(self.graphic)