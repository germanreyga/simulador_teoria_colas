import PySimpleGUI as sg
from submit_logic import submit_mms, submit_mm1

# Defines the window theme
sg.theme('Reddit')

# Tab M/M/1
LAMBDA_1 = "1_input_1"
MIU_1 = "1_input_2"
SUBMIT_1 = "Simular M/M/1"

mm1_layout = [[sg.Text("Lambda (λ)"), sg.In(key=LAMBDA_1)],
              [sg.Text("Miu (μ)"), sg.In(key=MIU_1)],
              [sg.Button(SUBMIT_1)]
              ]

# Tab M/M/s
LAMBDA_2 = "2_input_1"
MIU_2 = "2_input_2"
SERVERS_2 = "2_input_3"
SUBMIT_2 = "Simular M/M/s"

mms_layout = [[sg.Text("Lambda (λ)"), sg.In(key=LAMBDA_2)],
              [sg.Text("Miu (μ)"), sg.In(key=MIU_2)],
              [sg.Text("Servidores (s)"), sg.In(key=SERVERS_2)],
              [sg.Button(SUBMIT_2)]
              ]


# Creates the Window with a tab for each individual layout

general_layout = [[sg.TabGroup([[
    sg.Tab("M/M/1", mm1_layout),
    sg.Tab("M/M/s", mms_layout),
]])]]

window = sg.Window("Metodos cuantitativos y simulacion - Proyecto 2", general_layout)

# Event Loop to process "events"
if __name__ == '__main__':
    while True:
        event, values = window.read()
        if event in (None, "Cancel"):
            break
        if event == SUBMIT_1:
            submit_mm1(sg=sg, la=values[LAMBDA_1], mi=values[MIU_1])
        if event == SUBMIT_2:
            submit_mms(sg=sg, la=values[LAMBDA_2], mi=values[MIU_2], s=values[SERVERS_2])
    window.close()
