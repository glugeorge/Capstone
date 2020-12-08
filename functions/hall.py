from import_libraries import *

resistivity_config = {"V34I21":[], "V43I12":[], "V41I32":[], "V14I23":[],
                      "V12I43":[], "V21I34":[], "V23I14":[], "V32I41":[]}
hall_config = {"V24+I13":[], "V42+I31":[], "V13+I42":[], "V31+I24":[],
               "V24-I13":[], "V42-I31":[], "V13-I42":[], "V31-I24":[]}

def take_hall_measurement(I_p, I_n, V_p, V_n, B_on, B_orient, filename):

    f = open(filename, "w")
    text = "Hall experiment measurements \nConfiguration,Voltage,Current \n"
    f.write(text)
    f.close()

    # take measurements
    voltage = random.random()
    current = random.random()

    if B_on:
        config = f"V{V_p}{V_n}{B_orient}I{I_p}{I_n}"
        if config in hall_config:
            hall_config[config].append((voltage, current))
        else:
            print("This is not a valid combination")
    else:
        config = f"V{V_p}{V_n}I{I_p}{I_n}"
        if config in resistivity_config:
            resistivity_config[config].append((voltage, current))
        else:
            print("This is not a valid combination")

    f = open(filename, "a")

    for V_I in resistivity_config.keys():
        text = V_I + ","
        f.write(text)
        for i in range(len(resistivity_config[V_I])):
            text = str(resistivity_config[V_I][i]) + ","
            f.write(text)
        text = "\n"
        f.write(text)

    for V_I in hall_config.keys():
        text = V_I + ","
        f.write(text)
        for i in range(len(hall_config[V_I])):
            text = str(hall_config[V_I][i]) + ","
            f.write(text)
        text = "\n"
        f.write(text)



    f.close()

if __name__ == "__main__":
    take_hall_measurement(1,2,4,3,0,"+","file.txt")
    take_hall_measurement(2,1,3,4,0,"+","file.txt")
    take_hall_measurement(1,2,4,3,0,"+","file.txt")
