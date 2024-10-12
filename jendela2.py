import PySimpleGUI as sg
window=sg.Window(title="profile",
                 layout=[[sg.Text("NPM          : 2210010589")],
                         [sg.Text("Nama         : MUHAMMAD HANIFAH MUSLIM")],
                         [sg.Text("Kelas        : 5N")],
                         [sg.Text("Matkull      : pempograman Visual 3")]],
                 size=(400,200))
window()
window.close()