import pandas

dictionary = {
    "student": ["Shailesh", "Anubhav", "Sudhanshu"],
    "scores": [100, 100, 100]
}

std_dataframe = pandas.DataFrame(dictionary)
print(std_dataframe)

std_data = {}
for (index, row) in std_dataframe.iterrows():
    # print(type(row.student))
    std_data[row.student] = row.scores

print(std_data)