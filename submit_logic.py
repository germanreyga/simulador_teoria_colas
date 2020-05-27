from colas_simulator import mms, mm1, mmsk, mg1, mek1, total_cost


def parse_o(value):
    return round(float(value), 4)


def print_total_cost(window, label, cost):
    window["print_output"].print(label)
    window["print_output"].print(f"${cost}", text_color="blue")


def print_result(window, label, result):
    window["print_output"].print(label)
    window["print_output"].print(result, text_color="green")


def print_error(window, label, result):
    window["print_output"].print(label)
    window["print_output"].print(result, text_color="red")


def are_invalid(la, mi, s):
    if la >= s*mi:
        return True
    return False


def submit_mms(window, sg, la, mi, s, cw, cs):
    inputsAreValid = True
    incorrectInputs = ""

    try:
        la = float(la)
        mi = float(mi)
        s = int(s)
        cw = float(cw)
        cs = float(cs)
    except (ValueError):
        window["print_output"].print("Error de casteo. Lambda, Miu, Cw y Cs deben ser enteros o flotantes. Servidores debe ser entero.", text_color="red")
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
    if cw < 0:
        inputsAreValid = False
        incorrectInputs += "* El costo por tiempo de espera no puede ser menor a 0\n"
    if cs < 0:
        inputsAreValid = False
        incorrectInputs += "* El costo del servicio no puede ser menor a 0\n"

    if inputsAreValid:
        l, lq, w, wq, rho = mms(la, mi, s)
        result = f"L:\t{parse_o(l)}\nLq:\t{parse_o(lq)}\nW:\t{parse_o(w)}\nWq:\t{parse_o(wq)}\nRho:\t{parse_o(rho)}\n"
        print_result(window, "Resultado de la simulacion M/M/s", result)
        cost = total_cost(lq, cw, s, cs)
        print_total_cost(window, "Costo del sistema", parse_o(cost))
    else:
        print_error(window, "Error en los inputs:", incorrectInputs)


def submit_mm1(window, sg, la, mi, cw, cs):

    inputsAreValid = True
    incorrectInputs = ""
    try:
        la = float(la)
        mi = float(mi)
        s = 1
        cw = float(cw)
        cs = float(cs)
    except (ValueError):
        window["print_output"].print("Error de casteo. Lambda, Miu, Cw y Cs deben ser enteros o flotantes.", text_color="red")
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
    if cw < 0:
        inputsAreValid = False
        incorrectInputs += "* El costo por tiempo de espera no puede ser menor a 0\n"
    if cs < 0:
        inputsAreValid = False
        incorrectInputs += "* El costo del servicio no puede ser menor a 0\n"

    if inputsAreValid:
        l, lq, w, wq, rho = mm1(la, mi)
        result = f"L:\t{parse_o(l)}\nLq:\t{parse_o(lq)}\nW:\t{parse_o(w)}\nWq:\t{parse_o(wq)}\nRho:\t{parse_o(rho)}\n"
        print_result(window, "Resultado de la simulacion M/M/1", result)
        cost = total_cost(lq, cw, s, cs)
        print_total_cost(window, "Costo del sistema", parse_o(cost))
    else:
        print_error(window, "Error en los inputs:", incorrectInputs)


def submit_mmsk(window, sg, la, mi, s, k, cw, cs):

    inputsAreValid = True
    incorrectInputs = ""

    try:
        la = float(la)
        mi = float(mi)
        s = int(s)
        k = int(k)
        cw = float(cw)
        cs = float(cs)
    except (ValueError):
        window["print_output"].print("Error de casteo. Lambda, Miu, Cw y Cs deben ser enteros o flotantes. Servidores y Capacidad deben ser enteros.", text_color="red")
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
    if cw < 0:
        inputsAreValid = False
        incorrectInputs += "* El costo por tiempo de espera no puede ser menor a 0\n"
    if cs < 0:
        inputsAreValid = False
        incorrectInputs += "* El costo del servicio no puede ser menor a 0\n"

    if inputsAreValid:
        lae, l, lq, w, wq, rho = mmsk(la, mi, s, k)
        result = f"λe:\t{parse_o(lae)}\nL:\t{parse_o(l)}\nLq:\t{parse_o(lq)}\nW:\t{parse_o(w)}\nWq:\t{parse_o(wq)}\nRho:\t{parse_o(rho)}\n"
        print_result(window, "Resultado de la simulacion M/M/s/k", result)
        cost = total_cost(lq, cw, s, cs)
        print_total_cost(window, "Costo del sistema", parse_o(cost))
    else:
        print_error(window, "Error en los inputs:", incorrectInputs)


def submit_mg1(window, sg, la, mi, sig, cw, cs):

    inputsAreValid = True
    incorrectInputs = ""

    try:
        la = float(la)
        mi = float(mi)
        sig = float(sig)
        cw = float(cw)
        cs = float(cs)
    except (ValueError):
        window["print_output"].print("Error de casteo. Lambda, Miu, Sigma, Cw y Cs deben ser enteros o flotantes", text_color="red")
        return

    if are_invalid(la, mi, 1):
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
    if cw < 0:
        inputsAreValid = False
        incorrectInputs += "* El costo por tiempo de espera no puede ser menor a 0\n"
    if cs < 0:
        inputsAreValid = False
        incorrectInputs += "* El costo del servicio no puede ser menor a 0\n"

    if inputsAreValid:
        l, lq, w, wq, rho = mg1(la, mi, sig)
        result = f"L:\t{parse_o(l)}\nLq:\t{parse_o(lq)}\nW:\t{parse_o(w)}\nWq:\t{parse_o(wq)}\nRho:\t{parse_o(rho)}\n"
        print_result(window, "Resultado de la simulacion M/G/1", result)
        cost = total_cost(lq, cw, 1, cs)
        print_total_cost(window, "Costo del sistema", parse_o(cost))
    else:
        print_error(window, "Error en los inputs:", incorrectInputs)


def submit_mek1(window, sg, la, mi, k, cw, cs):

    inputsAreValid = True
    incorrectInputs = ""

    try:
        la = float(la)
        mi = float(mi)
        k = int(k)
        cw = float(cw)
        cs = float(cs)
    except (ValueError):
        window["print_output"].print("Error de casteo. Lambda, Miu, Cw y Cs deben ser enteros o flotantes. Capacidad debe ser entero.", text_color="red")
        return

    if are_invalid(la, mi, 1):
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
    if cw < 0:
        inputsAreValid = False
        incorrectInputs += "* El costo por tiempo de espera no puede ser menor a 0\n"
    if cs < 0:
        inputsAreValid = False
        incorrectInputs += "* El costo del servicio no puede ser menor a 0\n"

    if inputsAreValid:
        l, lq, w, wq, rho = mek1(la, mi, k)
        result = f"L:\t{parse_o(l)}\nLq:\t{parse_o(lq)}\nW:\t{parse_o(w)}\nWq:\t{parse_o(wq)}\nRho:\t{parse_o(rho)}\n"
        print_result(window, "Resultado de la simulacion M/Ek/1", result)
        cost = total_cost(lq, cw, 1, cs)
        print_total_cost(window, "Costo del sistema", parse_o(cost))
    else:
        print_error(window, "Error en los inputs:", incorrectInputs)
