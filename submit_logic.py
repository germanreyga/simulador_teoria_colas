from colas_simulator import mms, mm1, mmsk, mg1, mek1


def submit_mms(sg, la, mi, s):
    inputsAreValid = True
    incorrectInputs = ""

    try:
        la = float(la)
        mi = float(mi)
        s = int(s)
    except (ValueError):
        sg.Print("Error de casteo. Lambda y Miu deben ser enteros o flotantes. Servidores debe ser entero.", text_color="red")
        return

    if la <= 0:
        inputsAreValid = False
        incorrectInputs += "* Lambda no puede ser negativo ni cero\n"
    if mi <= 0:
        inputsAreValid = False
        incorrectInputs += "* Miu no puede ser negativo ni cero\n"
    if s <= 1:
        inputsAreValid = False
        incorrectInputs += "* Servidores no puede ser menor o igual a uno\n"

    if inputsAreValid:
        l, lq, w, wq = mms(la, mi, s)
        result = f"L:{l}\nLq:{lq}\nW:{w}\nWq:{wq}"
        sg.Print("Resultado de la simulacion M/M/s")
        sg.Print(result, text_color="green")
    else:
        sg.Print("Error en los inputs:", text_color="red")
        sg.Print(incorrectInputs, text_color="red")


def submit_mm1(sg, la, mi):

    inputsAreValid = True
    incorrectInputs = ""

    try:
        la = float(la)
        mi = float(mi)
    except (ValueError):
        sg.Print("Error de casteo. Lambda y Miu deben ser enteros o flotantes.", text_color="red")
        return

    if la <= 0:
        inputsAreValid = False
        incorrectInputs += "* Lambda no puede ser negativo ni cero\n"
    if mi <= 0:
        inputsAreValid = False
        incorrectInputs += "* Miu no puede ser negativo ni cero\n"

    if inputsAreValid:
        l, lq, w, wq = mm1(la, mi)
        result = f"L:{l}\nLq:{lq}\nW:{w}\nWq:{wq}"
        sg.Print("Resultado de la simulacion M/M/1")
        sg.Print(result, text_color="green")
    else:
        sg.Print("Error en los inputs:", text_color="red")
        sg.Print(incorrectInputs, text_color="red")
