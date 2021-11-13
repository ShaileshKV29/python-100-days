progtamming_dictionary = {
    "Python" : "Easy to learn and very powerfull",
    "HTML" : "NO!, It's not a programming language",
    "PHP" : "People hate it, but it gets the work done"
}

print(progtamming_dictionary.values())

for i in range(10):
    progtamming_dictionary[i] = i*10

key = "Name"
value = "Shailesh"

progtamming_dictionary[key] = value

print(progtamming_dictionary)

nested_dictionary = {
    "Key" : {"cities" : ["Paris", "Berlin"]}
}

print(nested_dictionary["Key"]["cities"][0])