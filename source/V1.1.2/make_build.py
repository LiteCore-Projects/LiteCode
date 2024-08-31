import os
from cx_Freeze import setup, Executable

# Sürüm numarasını tanımlayın
surum = "1.1.2"

# Yapılandırma
setup(
    name="litecode-" + surum,
    version=surum,
    description="LiteCode",
    executables=[Executable("litecode.py", target_name="litecode", icon="icon.ico")],
)
