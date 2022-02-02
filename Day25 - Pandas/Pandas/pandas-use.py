import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# temp_list = data["temp"].to_list()
# print(temp_list)
# print(sum(temp_list)/len(temp_list))
# print(data["temp"].mean())
# print(data["temp"].max())

# Get Data Row
# print(data[data.condition == "Sunny"])
# print(data[data.temp == data.temp.max()])

# Scratch Data to Dataframe
data_scratch = {
    "names": ["Shailesh", "Sudhanshu", "Anubhav"],
    "scores": [90, 89, 88]
}

data = pandas.DataFrame(data_scratch)
print(data)
# data.to_csv("new_data.csv")