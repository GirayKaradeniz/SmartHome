import matplotlib.pyplot as plt

def creating_load_graph(data):
    if data.shape[1] >= 20:
        load = data.iloc[-1, 2:].values
        timeOfTheDay = data.columns[2:]
        print("Load:", load)
        print("Time of the day:", timeOfTheDay)

        if len(load) != len(timeOfTheDay):
            print("Mismatch in the number of data points and labels.")
            return None




        return load, timeOfTheDay
    else:
        print("DataFrame does not have enough columns.")
        return None