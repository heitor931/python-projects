# Build a simple script to count the amount of grey, black and cinnamon squirel

import pandas as pd
data_from_csv = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_sq = data_from_csv["Primary Fur Color"]

counts = gray_sq.value_counts()
# Count occurrences of each value
new_dataframe = pd.DataFrame(counts)
csv_data = new_dataframe.to_csv()
excel_data = new_dataframe.to_excel

my_data = [
    {"name": ["Heitor", "Zánia", "Hélio", "Ayla", "Heloísa"]},
    {"age": [34, 32, 6, 2, 0 ]},
]

data_frame = pd.DataFrame(my_data,index=[0, 1,2,3])
print(data_frame)

#data_frame1.to_excel("my_data.xlsx")









