import json

# Esta función le vamos a dar cuello después
def check_pressure_sensor():
    with open('conf.json', 'r') as f:
        conf_data = json.load(f)

    if not conf_data['pyt_sens']:
        print("No pressure sensor detected")
    else:
        match conf_data['pyt_sens']:
            case "BME280":
                print('Ejecutando controlador para BME280')
            case "BMP280":
                print('Ejecutando controlador para BMP280')
            case _:
                print('No se ha encontrado el controlador requerido')

def pres_update(tolerance: float) -> None:
    
    with open('conf.json', 'r') as configuration:
        conf_data = json.load(configuration)

    MODEL_POW = 5.264083

    altitud = conf_data['H']
    factor_altura = 1 - (0.0065 * altitud) / 288.15
    pres_esperada = 1013.25 * factor_altura ** MODEL_POW

    conf_data['expected_p'] = round(pres_esperada, 2)
    
    conf_data['p_tolerance'] = round(tolerance, 2)

    with open('conf.json', 'w') as configuration:
        json.dump(conf_data, configuration, indent=4)

def pres_sens_exist(sens_type) -> None:
    
    with open('conf.json', 'r') as configuration:
        conf_data = json.load(configuration)

        conf_data['pyt_sens'] = sens_type
    
    with open('conf.json', 'w') as configuration:
        json.dump(conf_data, configuration, indent=4)

