#GMAT Initial Assignment - Part 1 - 2 (Error Handling)
#Muhammad Nafal Zakin Rustanto

error_list = ['Container descent rate failure', 'Science Payload descent rate failure', 'Container position failure', 'Science Payload position failure', 'Release failure'] #array to store error list
error_input = int(input()) #get input
error_code = bin(error_input)[2:].zfill(5) #converting input into 5 bit binary error code using bin() function, zfill is use to make the binary into 5 bits

if error_code=='00000':
  print('no error')
else:
  for i in range(5): #looping to get error list from error code, using index of error list array and index of error code
    if error_code[i] == '1':
      print(error_list[i])
