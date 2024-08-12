import pandas as pd

s_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240812.csv")

red_squirrels = s_data[s_data["Primary Fur Color"] == 'Cinnamon']
grey_squirrels = s_data[s_data["Primary Fur Color"] == 'Gray']
black_squirrels = s_data[s_data["Primary Fur Color"] == 'Black']

data_dict = {
    "fur color" : ["red", "grey", "black"],
    "count" : [len(red_squirrels), len(grey_squirrels), len(black_squirrels)] 
}

s_df = pd.DataFrame(data_dict).sort_values("count", ascending=False)
s_df.to_csv("Central Park Squirrel Color Count.csv")
print(s_df)