from cx_Freeze import setup, Executable

setup (
    name="Whatsapp Automatizado",
    version="1.0.0",
    options={"build_exe": {
        'packages': ["os", "sys", "ctypes", "tkinter", "time", "automated_whatsapp"],
        'include_msvcr': True,
    }},
    executables=[Executable ("automated_GUI_whatsapp.py", base="Win32GUI")]
)
