    index = lower_alphabets.index(item)
            message_index = message.index(item)
            decode_index = index - shift
            if(decode_index >= 0):
                decrypted_list[message_index] = lower_alphabets[decode_index]
            else:
                decode_index = index - shift + 25
        