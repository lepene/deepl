from PySide2 import QtWidgets
import deepl

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setup_ui()
        with open("deepl_auth_key.txt") as f:
            auth_key = f.readlines()[0]
            if len(auth_key) == 36:
                self.translator = deepl.Translator(auth_key)
            if bool(self.translator):
                result = self.translator.translate_text("Hello, world!", target_lang="FR")
                print(result.text)

    def setup_ui(self):
        self.setWindowTitle("Deepl")
        # create layouts
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.icons_bar_layout = QtWidgets.QHBoxLayout()
        self.top_layout = QtWidgets.QHBoxLayout()
        self.middle_layout = QtWidgets.QHBoxLayout()
        self.bottom_layout = QtWidgets.QHBoxLayout()
        # create widgets
        self.combo_source = QtWidgets.QComboBox()
        self.combo_cible = QtWidgets.QComboBox()
        self.txt_source = QtWidgets.QTextEdit()
        self.txt_cible = QtWidgets.QTextEdit()
        self.btn_options = QtWidgets.QPushButton("Options")
        self.btn_translate = QtWidgets.QPushButton("Traduire")
        # Add widgets to layouts
        self.icons_bar_layout.addWidget(self.btn_options)
        self.icons_bar_layout.addWidget(self.btn_translate)
        self.top_layout.addWidget(self.combo_source)
        self.top_layout.addWidget(self.combo_cible)
        self.middle_layout.addWidget(self.txt_source)
        self.middle_layout.addWidget(self.txt_cible)
        # Add layouts
        self.main_layout.addLayout(self.icons_bar_layout)
        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addLayout(self.middle_layout)
        self.main_layout.addLayout(self.bottom_layout)
        # Add connections




