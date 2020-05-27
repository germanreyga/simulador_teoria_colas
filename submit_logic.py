from colas_simulator import mms, mm1, mmsk, mg1, mek1


def are_invalid(la, mi, s):
    if la >= s*mi:
        return True
    return False


def are_invalid_2(la, mi):
    if la >= mi:
        return True
    return False


def submit_mms(window, sg, la, mi, s):
    inputsAreValid = True
    incorrectInputs = ""

    try:
        la = float(la)
        mi = float(mi)
        s = int(s)
    except (ValueError):
        window["print_output"].print("Error de casteo. Lambda y Miu deben ser enteros o flotantes. Servidores debe ser entero.", text_color="red")
        return

    if are_invalid(la, mi, s):
        inputsAreValid = False
        incorrectInputs += "* Lambda no puede ser mayor o igual a s*Miu\n"
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
        result = f"L:\t{l} ({float(l)})\nLq:\t{lq} ({float(lq)})\nW:\t{w} ({float(w)})\nWq:\t{wq} ({float(wq)})"
        window["print_output"].print("Resultado de la simulacion M/M/s")
        window["print_output"].print(result, text_color="green")
    else:
        window["print_output"].print("Error en los inputs:", text_color="red")
        window["print_output"].print(incorrectInputs, text_color="red")


def submit_mm1(window, sg, la, mi):

    inputsAreValid = True
    incorrectInputs = ""
    try:
        la = float(la)
        mi = float(mi)
        s = 1
    except (ValueError):
        window["print_output"].print("Error de casteo. Lambda y Miu deben ser enteros o flotantes.", text_color="red")
        return

    if are_invalid(la, mi, s):
        inputsAreValid = False
        incorrectInputs += "* Lambda no puede ser mayor o igual a Miu\n"
    if la <= 0:
        inputsAreValid = False
        incorrectInputs += "* Lambda no puede ser negativo ni cero\n"
    if mi <= 0:
        inputsAreValid = False
        incorrectInputs += "* Miu no puede ser negativo ni cero\n"

    if inputsAreValid:
        l, lq, w, wq = mm1(la, mi)
        result = f"L:\t{l} ({float(l)})\nLq:\t{lq} ({float(lq)})\nW:\t{w} ({float(w)})\nWq:\t{wq} ({float(wq)})"
        window["print_output"].print("Resultado de la simulacion M/M/1")
        window["print_output"].print(result, text_color="green")
    else:
        window["print_output"].print("Error en los inputs:", text_color="red")
        window["print_output"].print(incorrectInputs, text_color="red")


def submit_mmsk(window, sg, la, mi, s, k):

    inputsAreValid = True
    incorrectInputs = ""

    try:
        la = float(la)
        mi = float(mi)
        s = int(s)
        k = int(k)
    except (ValueError):
        window["print_output"].print("Error de casteo. Lambda y Miu deben ser enteros o flotantes. Servidores y Capacidad deben ser enteros.", text_color="red")
        return

    if are_invalid(la, mi, s):
        inputsAreValid = False
        incorrectInputs += "* Lambda no puede ser mayor o igual a s*Miu\n"
    if la <= 0:
        inputsAreValid = False
        incorrectInputs += "* Lambda no puede ser negativo ni cero\n"
    if mi <= 0:
        inputsAreValid = False
        incorrectInputs += "* Miu no puede ser negativo ni cero\n"
    if s <= 1:
        inputsAreValid = False
        incorrectInputs += "* Servidores no puede ser menor o igual a uno\n"
    if k <= 0:
        inputsAreValid = False
        incorrectInputs += "* Capacidad no puede ser negativo ni cero\n"

    if inputsAreValid:
        lae, l, lq, w, wq = mmsk(la, mi, s, k)
        result = f"λe:\t{lae} ({float(lae)})\nL:\t{l} ({float(l)})\nLq:\t{lq} ({float(lq)})\nW:\t{w} ({float(w)})\nWq:\t{wq} ({float(wq)})"
        window["print_output"].print("Resultado de la simulacion M/M/s/k")
        window["print_output"].print(result, text_color="green")
    else:
        window["print_output"].print("Error en los inputs:", text_color="red")
        window["print_output"].print(incorrectInputs, text_color="red")


def submit_mg1(window, sg, la, mi, sig):

    inputsAreValid = True
    incorrectInputs = ""

    try:
        la = float(la)
        mi = float(mi)
        sig = float(sig)
    except (ValueError):
        window["print_output"].print("Error de casteo. Lambda, Miu y Sigma deben ser enteros o flotantes", text_color="red")
        return

    if are_invalid_2(la, mi):
        inputsAreValid = False
        incorrectInputs += "* Lambda no puede ser mayor o igual a Miu\n"
    if la <= 0:
        inputsAreValid = False
        incorrectInputs += "* Lambda no puede ser negativo ni cero\n"
    if mi <= 0:
        inputsAreValid = False
        incorrectInputs += "* Miu no puede ser negativo ni cero\n"
    if sig >= 1 or sig <= 0:
        inputsAreValid = False
        incorrectInputs += "* Sigma solo puede ser un valor entre 0 y 1 (no inclusivo)\n"

    if inputsAreValid:
        l, lq, w, wq = mg1(la, mi, sig)
        result = f"L:\t{l} ({float(l)})\nLq:\t{lq} ({float(lq)})\nW:\t{w} ({float(w)})\nWq:\t{wq} ({float(wq)})"
        window["print_output"].print("Resultado de la simulacion M/G/1")
        window["print_output"].print(result, text_color="green")
    else:
        window["print_output"].print("Error en los inputs:", text_color="red")
        window["print_output"].print(incorrectInputs, text_color="red")


def submit_mek1(window, sg, la, mi, k):

    inputsAreValid = True
    incorrectInputs = ""

    try:
        la = float(la)
        mi = float(mi)
        k = int(k)
    except (ValueError):
        window["print_output"].print("Error de casteo. Lambda y Miu deben ser enteros o flotantes. Capacidad debe ser entero.", text_color="red")
        return

    if are_invalid_2(la, mi):
        inputsAreValid = False
        incorrectInputs += "* Lambda no puede ser mayor o igual a Miu\n"
    if la <= 0:
        inputsAreValid = False
        incorrectInputs += "* Lambda no puede ser negativo ni cero\n"
    if mi <= 0:
        inputsAreValid = False
        incorrectInputs += "* Miu no puede ser negativo ni cero\n"
    if k <= 0:
        inputsAreValid = False
        incorrectInputs += "* Capacidad no puede ser negativo ni cero\n"

    if inputsAreValid:
        l, lq, w, wq = mek1(la, mi, k)
        result = f"L:\t{l} ({float(l)})\nLq:\t{lq} ({float(lq)})\nW:\t{w} ({float(w)})\nWq:\t{wq} ({float(wq)})"
        window["print_output"].print("Resultado de la simulacion M/M/s/k")
        window["print_output"].print(result, text_color="green")
    else:
        window["print_output"].print("Error en los inputs:", text_color="red")
        window["print_output"].print(incorrectInputs, text_color="red")
