#GMAT Initial Assignment - Part 1- 1 (Parse CSV Data)
#Muhammad Nafal Zakin Rustanto

#function to checking validity of time data in the packet
def check_time(time_str):
  try:
    hours, minutes, seconds = map(int, time_str.split(':'))
    return 0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60 #hours is must less than 24, minutes and seconds must less than 60
  except:
    return False

#function checking validity of all data in the packet
def check_data(team_id, packet):
  if not packet.endswith(';'): #packet is end with ;
    return False

  data = packet[:-1].split(',') #spliting input (string) with , as a spliting

  if len(data) != 6: #amount of data ias exactly 6
    return False

  if data[0] != team_id: #data[0] should be same as team id
    return False

  if not check_time(data[1]): #checking validity of data[1]/time using our previous function
    return False

  if any(field.strip() == '' for field in data[2:]): #check for empty
    return False

  return True

#get input dan print output
team_id = str(input().strip())
if not len(team_id) == 0:
  print('YES')
else:
  print('NO')

n = int(input().strip())
if n>0:
  print('YES')
else:
  print('NO')

for i in range(n):
  packet = input().strip()
  if check_data(team_id, packet):
    print("YES")
  else:
    print("NO")
