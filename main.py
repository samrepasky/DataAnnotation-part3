#opens text file and reads it's contents to message_file
file = open('./coding_qual_input.txt')
message_file = file.read()
file.close()


#puts message file in dictionary
def organize(message_file):
    lines = message_file.split('\n') 
    my_dict = {} 

    for line in lines: 
        key, value = line.split(' ') 
        my_dict[key.strip()] = value.strip() 
    
    return(my_dict)


#gets the keys from the pyrimid
def pyramid(length):
    pyramid_keys = []
    count = 1
    iter = 0
    prev = 0
    for i in range(1,length):
        if i == 1:
            pyramid_keys.append(i)
        else:
            pyramid_keys.append(i+prev)
        prev = prev + i 

        if prev+i >= length:
            break
    return(pyramid_keys)

#reads the keys and decodes the message
def decode(my_dict, keys):
    final = []
    for i in keys:
        c = str(i)
        final.append(my_dict[c])
        string = " ".join(final)
    print(string)
  
my_dict = organize(message_file)
length = len(organize(message_file))
keys = pyramid(length)
decode(my_dict, keys)
