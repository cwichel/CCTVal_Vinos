# =============================================================================
# Modules
# =============================================================================
import sys
sys.path.extend(['../vinosApp/'])
from PyQt4 import QtGui
from Widget_ReadSave import Ui_Form

# =============================================================================
# Main Loop
# =============================================================================
if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    exe = Ui_Form()
    exe.show()
    sys.exit(app.exec_())