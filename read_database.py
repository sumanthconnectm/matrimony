


import sqlite3
import json


# ======================== get ecu details ========================
conn = sqlite3.connect('matrimony.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM brides;")
rows = cursor.fetchall()

columns = [description[0] for description in cursor.description]
data = [dict(zip(columns, row)) for row in rows]

json_data = json.dumps(data, indent=4)
brides_data_json = json.loads(json_data)

print(brides_data_json)

class Database:
    def __init__(self):
        super().__init__()

        self.brides_data_json = brides_data_json

    

    def brides(self):
        brides_list = []
        for bride in self.brides_data_json:
            brides_list.append(BrideDetails(bride['id'], bride['dob'], bride['star'], bride['padam'], bride['time'], bride['sign']))

        return brides_list

class BrideDetails:
    def __init__(self, id, dob, star, padam, time,sign ):
        self.id = id
        self.dob = dob
        self.star = star
        self.padam = padam
        self.time = time
        self.sign = sign

        


    


