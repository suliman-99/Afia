import pandas as pd


def get_data():
    data = []
    csv_file_path = 'output.csv'
    pandas_file = pd.read_csv('output.csv')
    for _, row in pandas_file.iterrows():
        record_data = {}
        for key, value in row.items():
            record_data[key] = value
        data.append(record_data)
    return data

data = get_data()
print(data)