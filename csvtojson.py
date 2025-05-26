import pandas as pd
import json

def csv_to_json(csv_file, json_file):
    df = pd.read_csv(csv_file)
    data = df.to_dict(orient='records')
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


if __name__ == '__main__':
    csv_to_json('profiles1.csv', 'data.json')