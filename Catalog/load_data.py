from .models import Products
import pandas as pd
from VanderVliet.settings import BASE_DIR
from pathlib import Path

def load_data():
    df = pd.read_excel(Path(BASE_DIR,'Catalog','data_vandervliet.xlsx')).drop('Prijs_oud', axis='columns')

    for index, row in df.iterrows():
        data = row.to_dict()
        Products.objects.get_or_create(Typenummer=row['Typenummer'], defaults=data)
