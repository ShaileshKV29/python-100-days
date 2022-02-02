import pandas

data = pandas.read_csv("./Squirrel Census/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color_data = data["Primary Fur Color"]
fur_color_list = fur_color_data.to_list()
gray_squirrel = fur_color_list.count("Gray")
cinnamon_squirrel = fur_color_list.count("Cinnamon")
black_squirrel = fur_color_list.count("Black")

fur_count = {
    "Fur Color": ["gray", "cinnamon", "black"],
    "Count": [gray_squirrel, cinnamon_squirrel, black_squirrel]
}


fur_data = pandas.DataFrame(fur_count)
fur_data.to_csv("./Squirrel Census/fur_data.csv")