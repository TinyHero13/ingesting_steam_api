from extract_all import extract_data
from bs4 import BeautifulSoup
import fireducks.pandas as pd

def clean_data():
    games = extract_data()

    df = pd.DataFrame(games)
    df = df[['appid', 'name']]
    
    df['name'] = df['name'].replace(['test2', 'test3'], ' ')
    df = df[df['name'].str.strip().astype(bool)]

    return df