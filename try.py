import requests
from io import StringIO
import pandas as pd

orig_url='https://drive.google.com/file/d/1F7nQC4OV-WqCiZrDV-EQUVoz22f_DDds/view?usp=sharing'
file_id = orig_url.split('/')[-2]
dwn_url='https://drive.google.com/uc?export=download&id='+ file_id
url = requests.get(dwn_url).text
csv_raw = StringIO(url)

data = pd.read_csv(csv_raw)
print(data)