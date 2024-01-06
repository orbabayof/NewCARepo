num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]
count = 0
for idx ,item in enumerate(num_list):
     #print(item)
     if item > 45:
          print(item , " Over 45")
     else:
          print(item , " Under 45")
     if item == 36:
          print("number found in postion", idx)
          break
     count+= 1
print(count)