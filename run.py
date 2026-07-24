import os, glob, shutil

# Auto-fix .so naming on first run
if not os.path.exists("de.so"):
    so_files = glob.glob("de.cpython*.so")
    if so_files:
        shutil.copy(so_files[0], "de.so")

import de
de.main()
