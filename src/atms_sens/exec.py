import json

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
