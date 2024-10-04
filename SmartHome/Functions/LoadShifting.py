import pandas as pd
from openpyxl import load_workbook

def load_shifting(data, threshold):
    for i, value in enumerate(data.iloc[-1, 13:18].values):
        total_sum = value

        while total_sum > threshold:
            min_priority = float('inf')
            min_priority_index = -1

            for j, number in enumerate(data.iloc[:-1, i+13]):
                if number > 0:
                    priority = data.iloc[j, 0]
                    if priority < min_priority or (priority == min_priority and number > data.iloc[min_priority_index, i+2]):
                        min_priority = priority
                        min_priority_index = j

            if min_priority_index == -1:
                break

            shifted = False
            for x in list(range(18, 26)) + list(range(2, 6)):
                if shift_device(data, min_priority_index, i+13, x, threshold):
                    shifted = True
                    break

            if not shifted:
                for x in range(6, 12):
                    if shift_device(data, min_priority_index, i+13, x, threshold):
                        shifted = True
                        break

            total_sum = data.iloc[:-1, i+13].sum()

        data.iloc[-1, i+13] = total_sum

    for a in range(2, 26):
        data.iloc[-1, a] = data.iloc[:-1, a].sum()

    temp_file = "Temp.xlsx"
    data.to_excel(temp_file, index=False)


def shift_device(data, device_index, from_col, to_col, threshold):
    current_sum = data.iloc[:-1, to_col].sum()
    device_value = data.iloc[device_index, from_col]

    if data.iloc[device_index, to_col] == 0:
        data.iloc[device_index, to_col] = device_value
        data.iloc[device_index, from_col] = 0
        return True
    return False