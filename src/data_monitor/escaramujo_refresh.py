import json
import glob
import pandas as pd
from datetime import datetime, timezone
import time

# Tiempo actual UTC

translation_time = 10

while (1):
    now_utc = datetime.now(timezone.utc)
    refresh_time = now_utc.strftime('%Y-%m-%d %H:%M')


    data_files = sorted(glob.glob('../../data/*'))
    cur_data_file = data_files[-1]

    cur_data = pd.read_csv(cur_data_file)

    median_C = cur_data['C'].median()


    with open('escaramujo_data.json', 'r') as f:
        escaramujo_monitor = json.load(f)
    
    measure_time = datetime.strptime(escaramujo_monitor['date'] + " " + escaramujo_monitor['utc'], '%Y-%m-%d %H:%M')
    status_check_dif =  datetime.strptime(refresh_time, '%Y-%m-%d %H:%M') - measure_time
    status_check = status_check_dif.total_seconds() / 60
    print(status_check)
    status = "OPERATIVO" if status_check < translation_time + 5 else "INTERRUMPIDO"

    for key in escaramujo_monitor:
        if key != 'median' and key != 'refresh' and key != 'ID' and key != 'status':
            value = cur_data[key].iloc[-1]
            escaramujo_monitor[key] = value.item() if hasattr(value, "item") else value
        elif key == 'median':
            escaramujo_monitor[key] = round(median_C)
        elif key == 'refresh':
            escaramujo_monitor[key] = refresh_time
        elif key == 'status':
            escaramujo_monitor[key] = status

    with open('escaramujo_data.json', 'w') as f:
        json.dump(escaramujo_monitor, f, indent=4)
    
    time.sleep(30)

