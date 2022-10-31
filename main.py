from PyQt5 import QtCore, QtGui, QtWidgets
from carre import Ui_MainWindow


def carre():
    nombre_recup = int(ui.nombre.text())
    carreN = nombre_recup * nombre_recup
    ui.n_nombre.setText(str(nombre_recup))
    ui.resultat.setText(str(carreN))

def actualiser():
    ui.nombre.setText("")



import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
ui.btn_valider.clicked.connect(carre)
ui.btn_valider.clicked.connect(actualiser)
sys.exit(app.exec_())
