import ctypes

# Carregar a DLL
lib = ctypes.CDLL('./testlib.dll')

# Usar a função hello
lib.hello()