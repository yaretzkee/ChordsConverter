# -------- enable importing from parent dir -----------------------------------
import subprocess
import sys
sys.path.insert(0, '..')
# ------------------------------------------------------------------------------


class UIC:
    def __init__(self, ui_file, out_file):
        self.ui_file = ui_file
        self.out_file = out_file

    def compile(self):
        cmd = subprocess.run(["pyside6-uic", self.ui_file], encoding='utf-8', capture_output=True)
        if cmd.returncode == 0:
            with open(file=self.out_file, mode='w', encoding='utf-8') as f:
                f.write(cmd.stdout)


if __name__ == '__main__':
    uic = UIC('main_window.ui', 'ui_mainwindow.py')
    uic.compile()
