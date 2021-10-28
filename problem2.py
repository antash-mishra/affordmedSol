def compress(message):
    encoded_string = ""
    i = 0
    while (i <= len(message)-1):
        count = 1
        ch = message[i]
        j = i
        while (j < len(message)-1): 
            if (message[j] == message[j + 1]): 
                count = count + 1
                j = j + 1
            else: 
                break
        encoded_string = encoded_string + str(count) + ch
        i = j + 1
    return encoded_string

def decompressor(our_message):
	decoded_message = ""
	i=0
	j=0
	while (i <= len(our_message)-1):
		run_count = int(our_message[i])
		run_word = our_message[i + 1]
		for j in range(run_count):
			decoded_message = decoded_message+run_word
			j = j + 1
		i = i + 2
	return decoded_message

def display():
	our_message = "Hello World"
	encoded_message=compress(our_message)
	decoded_message=decompressor(encoded_message)
	print("Original string: ["+our_message+"]\nEncoded string: ["+encoded_message+"]\nDecoded string: ["+decoded_message+"]\n")

display()
    
