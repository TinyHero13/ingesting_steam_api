from transform import clean_data
from bs4 import BeautifulSoup
import fireducks.pandas as pd
import requests
from functools import reduce
def extract_apps():
    all_games = clean_data()
    print(all_games.count)

    all_games = all_games.head(7)

    count = 0

    all_dfs = []

    nested_columns = ['support_info', 'pc_requirements', 'mac_requirements', 'linux_requirements', 'developers', 'publishers', 'price_overview', 'packages', 'platforms', 'categories', 'genres',
                      'release_date',	'content_descriptors',	'ratings', 'package_groups'
]

    for ids in all_games['appid']:
        response = requests.get(f'https://store.steampowered.com/api/appdetails?appids={ids}').json()[f'{ids}']
             
        if response['success']:

            df = pd.DataFrame.from_dict(response['data'], orient='index')
            df = df.transpose()

            df = df.drop(columns=['movies', 'screenshots', 'background', 'background_raw', 'header_image', 'capsule_image', 'capsule_imagev5'], errors='ignore')
            
            for col in nested_columns:
                try:
                    normalized = pd.json_normalize(df[col])
                    normalized.columns = [f"{col}.{sub_col}" for sub_col in normalized.columns]  
                    df = pd.concat([df.drop(columns=[col]), normalized], axis=1)
                except:
                    continue 


            all_dfs.append(df)

    final_df = pd.concat(all_dfs, ignore_index=True)        
    print(final_df)
extract_apps()
