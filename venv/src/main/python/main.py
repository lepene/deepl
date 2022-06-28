from fbs_runtime.application_context.PySide2 import ApplicationContext
from main_window import MainWindow
import deepl
import sys

if __name__ == '__main__':
    with open("deepl_auth_key.txt") as f:
        auth_key = f.readlines()[0]
        if len(auth_key) == 36:
            translator = deepl.Translator(auth_key)
        if bool(translator):
            result = translator.translate_text("Hello, world!", target_lang="FR")
            print(result.text)

    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = MainWindow()
    window.resize(250, 150)

    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)