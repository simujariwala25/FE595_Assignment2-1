import requests as req
import pandas as pd

for j in range(50):
    response = req.get("http://3.95.249.159:8000/random_company")
    total = response.text
    sentence = total.split("\n")
    extract = pd.DataFrame
    for i in sentence:
        if 'Name: ' in i:
            n = i[16:-5]
            print("({0}){1}".format(j+1, n))
        if 'Purpose: ' in i:
            p = i[16:-5]
            print("({0}){1}".format(j+1, p))
