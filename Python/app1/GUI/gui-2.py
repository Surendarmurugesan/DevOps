import PySimpleGUI as ss

label1 = ss.Text("Enter feet:")
label2 = ss.Text("Enter inches:")
input_box = ss.InputText("")
input_box2 = ss.InputText("")
button = ss.Button("Convert")

app = ss.Window('Convertor', layout=[[label1, input_box], [label2, input_box2], [button]])
app.read()
app.close()