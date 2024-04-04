from tkinter import ttk, constants

class LogoutView:
    def __init__(self, root, handle_login):
        self._root = root
        self._handle_login = handle_login
        self._frame = None
        
        self._initialize()
    
    def pack(self):
        self._frame.pack(fill = constants.X)

    def destroy(self):
        self._frame.destroy()

    def initialize(self):
        self._frame = ttk.Frame(master = self._root)
        button = ttk.Button(master = self._frame,
                            text = "hello",
                            command = self._handle_login)
        button.grid(row = 1, column = 0)