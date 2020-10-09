import requests as req
import pandas as pd

data1 = []
data2 = []
for j in range(50):
    response = req.get("http://3.95.249.159:8000/random_company")
    total = response.text
    sentence = total.split("\n")
    for i in sentence:
        if 'Name: ' in i:
            name = i[22:-5]
            data1.append(name)
        if 'Purpose: ' in i:
            purpose = i[25:-5]
            data2.append(purpose)


result = pd.DataFrame({"Name": data1, "Purpose": data2})
result.to_csv('Assignment_2.csv')

####### Review for Aniruddh's code : I would suggest creating a single list and appending both Name and purpose to it instead of 2 lists. I review it as 4.5/5.
# Reviewed by Simran Jariwala
