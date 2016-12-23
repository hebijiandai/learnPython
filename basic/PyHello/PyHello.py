class PyHello:

    def __init__(self):
        pass

    def SayHello(self):
        return 'Hello Python!'

    def DoAdd(self,a,b):
        return a + b

class _WrapPyHello(PyHello):
    _reg_clsid_ = '{4ae5ed1d-c378-4da1-9816-5a038112deaa}'
    _reg_progid_ = "Python.PyHello"
    _public_methods_ = ['SayHello','DoAdd']

if __name__=='__main__':
    import win32com.server.register
    win32com.server.register.UseCommandLine(_WrapPyHello)
