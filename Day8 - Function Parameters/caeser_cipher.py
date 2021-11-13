import string
task = input("Type 'encode' for encryption, 'decode' for descryption : ")

lower_alphabets = list(string.ascii_lowercase)

message = input("Type your message: ")
message = message.lower()
message = list(message)
shift = int(input("Type the shift number : "))

# Encryption Function
def encryption(message):

    encrypeted_result = []
    for i in message:
        encrypeted_result.append(i)

    for item in message:
        if(item in lower_alphabets):
            index = lower_alphabets.index(item)
            message_index = message.index(item)
            encode_index = index + shift
            if(encode_index <= 25):
                encrypeted_result[message_index] = lower_alphabets[encode_index]
                message[message_index] = 0
            else:
                encode_index = index + shift - 25
                encrypeted_result[message_index] = lower_alphabets[encode_index]
                message[message_index] = 0

    for encryption in encrypeted_result:
        print(encryption, end="")

# Decryption Function
def decryption(message):
    decrypted_list = message

    for item in message:
        if(item in lower_alphabets):
            index = lower_alphabets.index(item)
            message_index = message.index(item)
            decode_index = index - shift
            if(decode_index >= 0):
                decrypted_list[message_index] = lower_alphabets[decode_index]
            else:
                decode_index = index - shift + 25
                decrypted_list[message_index] = lower_alphabets[decode_index]

    for decryption in decrypted_list:
        print(decryption, end="")


if(task == "encode"):

    encryption(message)

elif(task == "decode"):

    decryption(message)