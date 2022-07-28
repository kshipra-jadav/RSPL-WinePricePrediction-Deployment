import pickle
import pandas as pd

def process(winery_name, wine_name, region_name):
    infile = open('winery_enc', "rb")
    winery_encoder = pickle.load(infile)
    infile.close()
    infile = open('wine_enc', 'rb')
    wine_encoder = pickle.load(infile)
    infile.close()
    infile = open('region_enc', 'rb')
    region_encoder = pickle.load(infile)
    infile.close()

    winery_processed = winery_encoder.transform([[winery_name]])
    wine_processed = wine_encoder.transform([[wine_name]])
    region_processed = region_encoder.transform([[region_name]])

    print([winery_processed, wine_processed, region_processed])

    return [winery_processed, wine_processed, region_processed]

def makeDF(winery, wine, rating, region, body):
    my_dict = {
        'winery': winery,
        'wine': wine,
        'rating': rating,
        'region': region,
        'body': body
    }

    df = pd.DataFrame(my_dict, index=[0])
    print(df)
    return df

def predict(X_values):
    infile = open('regressorModel', 'rb')
    model = pickle.load(infile)
    infile.close()

    price = model.predict(X_values)
    print(f'Price:- {price}')
    return price




def start(winery, wine, rating, region, body):
    winery_processed, wine_processed, region_processed = process(winery, wine, region)
    X_vals = makeDF(winery_processed[0][0], wine_processed[0][0], rating, region_processed[0][0], body)
    return(predict(X_vals))




