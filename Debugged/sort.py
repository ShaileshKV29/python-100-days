import string
print("Type 'encode' for encryption, 'decode' for descryption : ")
task = input()

lower_alphabets = list(string.ascii_lowercase)

message = input("Type your message: ")
message = message.lower()
message = list(message)
print("Type the shift number : ")
shift = int(input())

if(task == "encode"):

    encrypeted_result = []

    for item in message:
        index = lower_alphabets.index(item)
        encode_index = index + shift
        if(encode_index <= 26):
            encrypeted_result.append(lower_alphabets[encode_index])
        else:
            encode_index = index + shift - 27
            encrypeted_result.append(lower_alphabets[encode_index])

print(encrypeted_result)