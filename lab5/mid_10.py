from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
import sys


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Простейший GUI на PyQt5")
window.resize(300, 200)

layout = QVBoxLayout()
label = QLabel("Привет, PyQt5!")
layout.addWidget(label)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())
