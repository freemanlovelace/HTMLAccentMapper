from cx_Freeze import setup, Executable

setup(
    name="HTMLAccentMapperExampleGui",
    version="1.0",
    description="map html accent entities to keyboard",
    executables=[Executable("gui.py", base="tkinter")],
)
