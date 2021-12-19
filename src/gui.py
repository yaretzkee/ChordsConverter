# -------- enable importing from parent dir -----------------------------------
import subprocess
import sys
sys.path.insert(0, '..')
from PySide6.QtDesigner import QFormBuilder
from PySide6.QtCore import QFile
# ------------------------------------------------------------------------------


class Designer:
    def __init__(self):
        pass

    def build(self, mode, in_file, out_file):
        program = f'pyside6-{mode}'
        cmd = subprocess.run([program, in_file], encoding='utf-8', capture_output=True)
        if cmd.returncode == 0:
            with open(file=out_file, mode='w', encoding='utf-8') as f:
                f.write(cmd.stdout)
        return True

        
if __name__ == '__main__':
    uic = Designer()
    uic.build('uic','main_window.ui', 'ui_mainwindow.py')
    uic.build('rcc', '../img/icons.qrc', 'icons_rc.py')
    #uic.build()
