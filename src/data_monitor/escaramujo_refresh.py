import json
import glob
import pandas as pd
from datetime import datetime, timezone
import time

# Tiempo actual UTC
now_utc = datetime.now(timezone.utc)
cur_year = now_utc.strftime('%Y')
cur_month = now_utc.strftime('%m')


data_files = sorted(glob.glob('../../data/*'))
cur_data_file = data_files[-1]

cur_data = pd.read_csv(cur_data_file)

median_C = cur_data['C'].median()


with open('escaramujo_data.json', 'r') as f:
    escaramujo_monitor = json.load(f)

for key in escaramujo_monitor:
    if key == 'median':
        escaramujo_monitor[key] = round(median_C)
    elif key in cur_data.columns:
        print(cur_data[key].iloc[-1])
        value = cur_data[key].iloc[-1]
        escaramujo_monitor[key] = value.item() if hasattr(value, "item") else value

with open('escaramujo_data.json', 'w') as f:
    json.dump(escaramujo_monitor, f, indent=4)

