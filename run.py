import os, glob, shutil

# Auto-fix .so naming on first run
if not os.path.exists("d.so"):
    so_files = glob.glob("d.cpython*.so")
    if so_files:
        shutil.copy(so_files[0], "d.so")

import d
d.main()
