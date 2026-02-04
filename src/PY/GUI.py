import json

def pres_update() -> None:
    
    with open('../take/conf.json', 'r') as configuration:
        conf_data = json.load(configuration)

    MODEL_POW = 5.264083

    altitud = conf_data['H']
    factor_altura = 1 - (0.0065 * altitud) / 288.15
    pres_esperada = 1013.25 * factor_altura ** MODEL_POW

    conf_data['expected_p'] = round(pres_esperada, 2)

    with open('take/conf.json', 'w') as configuration:
        json.dump(conf_data, configuration, indent=4)


pres_update()
