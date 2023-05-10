from PyQt6.QtWidgets import QApplication, QMainWindow, QScrollArea, QLineEdit, QFileDialog, QGroupBox, QLabel, QGridLayout, QWidget, QTextEdit, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt6.QtGui import QPixmap


class Ventana_principal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejercicio 1")
        self.resize(800, 600)

        self.label_titulo = QLabel("Ejercicio 1")
        self.label_usuario = QLabel("Nombre de usuario:")
        self.edit_usuario = QLineEdit()
        self.boton_imagen = QPushButton("Seleccionar imagen")
        self.imagen = QLabel()
        self.imagen.setFixedSize(150, 150)
        self.label_descripcion = QLabel("Descripcion:")
        self.edit_descripcion = QTextEdit()
        self.grupo_atributos = QGroupBox("Atributos")
        self.layout_atributos = QGridLayout()
        self.layout_valores = QGridLayout()
        self.boton_guardar = QPushButton("Guardar")

        self.layout_principal = QHBoxLayout()
        self.layout_izquierda = QVBoxLayout()
        self.layout_izquierda.addWidget(self.label_usuario)
        self.layout_izquierda.addWidget(self.edit_usuario)
        self.layout_izquierda.addWidget(self.boton_imagen)
        self.layout_izquierda.addWidget(self.imagen)
        self.layout_izquierda.addWidget(self.label_descripcion)
        self.layout_izquierda.addWidget(self.edit_descripcion)
        self.layout_izquierda.addWidget(self.grupo_atributos)
        self.layout_izquierda.addWidget(self.boton_guardar)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_widget = QWidget()
        self.layout_derecha = QVBoxLayout()
        self.layout_derecha.addWidget(QLabel("Atributos"))
        self.scroll_widget.setLayout(self.layout_derecha)
        self.scroll_area.setWidget(self.scroll_widget)

        for i in range(6):
            label_atributo = QLabel(f"atributo{i+1}:")
            label_valor = QLabel(f"valor {i+1}:")
            edit_atributo = QLineEdit()
            edit_valor = QLineEdit()
            self.layout_atributos.addWidget(label_atributo, i, 0)
            self.layout_atributos.addWidget(edit_atributo, i, 1)
            self.layout_valores.addWidget(label_valor, i, 0)
            self.layout_valores.addWidget(edit_valor, i, 1)
        
        self.grupo_atributos.setLayout(self.layout_atributos)
        self.layout_derecha.addLayout(self.layout_atributos, 0, 0, 1, 2)
        self.layout_derecha.addLayout(self.layout_valores, 1, 0, 1, 2)

        self.layout_principal.addLayout(self.layout_izquierda)
        self.layout_principal.addWidget(self.scroll_area)

        self.widget = QWidget()
        self.widget.setLayout(self.layout_principal)

        self.boton_imagen.clicked.connect(self.seleccionar_imagen)
        self.boton_guardar.clicked.connect(self.guardar_perfil)

        self.setCentralWidget(self.widget)

    def seleccionar_imagen(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Seleccionar imagen")
        if filename:
            pixmap = QPixmap(filename)
            self.imagen.setPixmap(pixmap)

    def guardar_perfil(self):
        Usuario = self.edit_usuario.text()
        descripcion = self.edit_descripcion.toPlainText()
        atributos = [self.layout_atributos.itemAt(i).widget().text() for i in range(self.layout_atributos.count()) if i % 2 != 0]
        valores = [self.layout_valores.itemAt(i).widget().text() for i in range(self.layout_valores.count()) if i % 2 != 0]
        print(f"Usuario: {Usuario}")
        print(f"Descripcion: {descripcion}")
        print(f"Atributos:")
        for atributo, valor in zip(atributos, valores):
            print(f"{atributo}: {valor}")

if __name__ == '__main__':
    app = QApplication([])
    window = Ventana_principal()
    window.show()
    app.exec()