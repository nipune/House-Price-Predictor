import json
import pickle
import numpy as np

__suburb = None
__data_columns = None
__model = None

def get_estimated_price(suburb,rooms,distance,bathroom,car,sqm):
    try:
        sub_index = __data_columns.index(suburb.lower())
    except:
        sub_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = rooms
    x[1] = distance
    x[2] = bathroom
    x[3] = car
    x[4] = sqm

    if sub_index >= 0:
        x[sub_index] = 1

    return round(__model.predict([x])[0],2)

def get_suburb_names():
    return __suburb

def load_saved_artifacts():
    print("Loading saved artifacts..start..")
    global __data_columns
    global __suburb

    with open('./artifacts/column.json', 'r') as f:
        __data_columns = json.load(f)['data columns']
        __suburb = __data_columns[5:]

    global __model
    with open('./artifacts/melb_house_price_model.pickle', 'rb') as f:
        __model = pickle.load(f)
    print("Loading saved artifacts..done..")

if __name__ == '__main__':
    load_saved_artifacts()
    #print(get_suburb_names())
    #print(get_estimated_price('Doncaster',5,12.4,3,3,930))