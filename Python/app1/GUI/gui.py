import PySimpleGUI as sg

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window('To Do Application', layout=[[label], [input_box, add_button]])
window.read()
print("Hello")
window.close()