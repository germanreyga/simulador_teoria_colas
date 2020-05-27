import PySimpleGUI as sg
from submit_logic import submit_mms, submit_mm1, submit_mmsk, submit_mg1, submit_mek1

# General variables
sigma_text = u"\u03C3"
lambda_text = u"\u03BB"
miu_text = u"\u03BC"


def FText(text):  # Defines a justified text
    return sg.Text(text, justification="right", size=(12, 1))


def FButton(event_name):
    return sg.Button(event_name)


# Defines the window theme
sg.theme('Reddit')

# Tab M/M/1
LAMBDA_1 = "1_input_1"
MIU_1 = "1_input_2"
CW_1 = "1_input_3"
CS_1 = "1_input_4"
SUBMIT_1 = "Simular M/M/1"

mm1_layout = [[FText(f"Lambda ({lambda_text})"), sg.In(key=LAMBDA_1)],
              [FText(f"Miu ({miu_text})"), sg.In(key=MIU_1)],
              [FText("Cw ($)"), sg.In(key=CW_1)],
              [FText("Cs ($)"), sg.In(key=CS_1)],
              [FButton(SUBMIT_1)]
              ]

# Tab M/M/s
LAMBDA_2 = "2_input_1"
MIU_2 = "2_input_2"
SERVERS_2 = "2_input_3"
CW_2 = "2_input_4"
CS_2 = "2_input_5"
SUBMIT_2 = "Simular M/M/s"

mms_layout = [[FText(f"Lambda ({lambda_text})"), sg.In(key=LAMBDA_2)],
              [FText(f"Miu ({miu_text})"), sg.In(key=MIU_2)],
              [FText("Servidores (s)"), sg.In(key=SERVERS_2)],
              [FText("Cw ($)"), sg.In(key=CW_2)],
              [FText("Cs ($)"), sg.In(key=CS_2)],
              [FButton(SUBMIT_2)]
              ]

# Tab M/M/s
LAMBDA_3 = "3_input_1"
MIU_3 = "3_input_2"
SERVERS_3 = "3_input_3"
CAPACITY_3 = "3_input_4"
CW_3 = "3_input_5"
CS_3 = "3_input_6"
SUBMIT_3 = "Simular M/M/s/k"

mmsk_layout = [[FText(f"Lambda ({lambda_text})"), sg.In(key=LAMBDA_3)],
               [FText(f"Miu ({miu_text})"), sg.In(key=MIU_3)],
               [FText("Servidores (s)"), sg.In(key=SERVERS_3)],
               [FText("Capacidad (k)"), sg.In(key=CAPACITY_3)],
               [FText("Cw ($)"), sg.In(key=CW_3)],
               [FText("Cs ($)"), sg.In(key=CS_3)],
               [FButton(SUBMIT_3)]
               ]

# Tab M/G/1
LAMBDA_4 = "4_input_1"
MIU_4 = "4_input_2"
SIGMA_4 = "4_input_3"
CW_4 = "4_input_4"
CS_4 = "4_input_5"
SUBMIT_4 = "Simular M/G/1"
mg1_layout = [[FText(f"Lambda ({lambda_text})"), sg.In(key=LAMBDA_4)],
              [FText(f"Miu ({miu_text})"), sg.In(key=MIU_4)],
              [FText(f"Sigma ({sigma_text})"), sg.In(key=SIGMA_4)],
              [FText("Cw ($)"), sg.In(key=CW_4)],
              [FText("Cs ($)"), sg.In(key=CS_4)],
              [FButton(SUBMIT_4)]
              ]

# Tab M/M/s
LAMBDA_5 = "5_input_1"
MIU_5 = "5_input_2"
CAPACITY_5 = "5_input_3"
CW_5 = "5_input_4"
CS_5 = "5_input_5"
SUBMIT_5 = "Simular M/Ek/1"

mek1_layout = [[FText(f"Lambda ({lambda_text})"), sg.In(key=LAMBDA_5)],
               [FText(f"Miu ({miu_text})"), sg.In(key=MIU_5)],
               [FText("Capacidad (k)"), sg.In(key=CAPACITY_5)],
               [FText("Cw ($)"), sg.In(key=CW_5)],
               [FText("Cs ($)"), sg.In(key=CS_5)],
               [FButton(SUBMIT_5)]
               ]


# Creates the Window with a tab for each individual layout

general_layout = [[sg.TabGroup([[
    sg.Tab("M/M/1", mm1_layout),
    sg.Tab("M/M/s", mms_layout),
    sg.Tab("M/M/s/k", mmsk_layout),
    sg.Tab("M/G/1", mg1_layout),
    sg.Tab("M/Ek/1", mek1_layout),
]]), sg.Multiline(size=(40, 10), key="print_output", do_not_clear=False, font=("Consolas", 16))]]

window = sg.Window("Metodos cuantitativos y simulacion - Proyecto 2", general_layout, element_padding=(15, 5), default_element_size=(35, 1))

# Event Loop to process "events"
if __name__ == '__main__':
    while True:
        event, values = window.read()
        if event in (None, "Cancel"):
            break
        if event == SUBMIT_1:
            submit_mm1(window=window, sg=sg, la=values[LAMBDA_1], mi=values[MIU_1], cw=values[CW_1], cs=values[CS_1])
        if event == SUBMIT_2:
            submit_mms(window=window, sg=sg, la=values[LAMBDA_2], mi=values[MIU_2], s=values[SERVERS_2], cw=values[CW_2], cs=values[CS_2])
        if event == SUBMIT_3:
            submit_mmsk(window=window, sg=sg, la=values[LAMBDA_3], mi=values[MIU_3], s=values[SERVERS_3], k=values[CAPACITY_3], cw=values[CW_3], cs=values[CS_3])
        if event == SUBMIT_4:
            submit_mg1(window=window, sg=sg, la=values[LAMBDA_4], mi=values[MIU_4], sig=values[SIGMA_4], cw=values[CW_4], cs=values[CS_4])
        if event == SUBMIT_5:
            submit_mek1(window=window, sg=sg, la=values[LAMBDA_5], mi=values[MIU_5], k=values[CAPACITY_5], cw=values[CW_5], cs=values[CS_5])

    window.close()
