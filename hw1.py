# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '107061235.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
#target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

# Retrive ten data points from the beginning.
    #target_data = data[:10]
count = len(data)
delete = []
for i in range(count):
    if ((data[i]['TEMP'] == '-99.000') or (data[i]['TEMP'] == '-999.000')) :
        delete.append(i)
j=0
for i in delete:
    del(data[i-j])
    j += 1
C0A880_data = list(filter(lambda item: item['station_id'] == 'C0A880', data))
C0F9A0_data = list(filter(lambda item: item['station_id'] == 'C0F9A0', data))
C0G640_data = list(filter(lambda item: item['station_id'] == 'C0G640', data))
C0R190_data = list(filter(lambda item: item['station_id'] == 'C0R190', data))
C0X260_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

C0A880_TEMP = []
C0F9A0_TEMP = []
C0G640_TEMP = []
C0R190_TEMP = []
C0X260_TEMP = []
name = []
name.append('C0A880')
name.append('C0F9A0')
name.append('C0G640')
name.append('C0R190')
name.append('C0X260')
ans = []
for i in range(len(C0A880_data)):
    C0A880_TEMP.append(C0A880_data[i]['TEMP'])
for i in range(len(C0F9A0_data)):
    C0F9A0_TEMP.append(C0F9A0_data[i]['TEMP'])
for i in range(len(C0G640_data)):
    C0G640_TEMP.append(C0G640_data[i]['TEMP'])
for i in range(len(C0R190_data)):
    C0R190_TEMP.append(C0R190_data[i]['TEMP'])
for i in range(len(C0X260_data)):
    C0X260_TEMP.append(C0X260_data[i]['TEMP'])

if len(C0A880_TEMP)>0 :
    ans.append(max(C0A880_TEMP))
else :
    ans.append('NONE')
if len(C0F9A0_TEMP)>0 :
    ans.append(max(C0F9A0_TEMP))
else :
    ans.append('NONE')
if len(C0G640_TEMP)>0 :
    ans.append(max(C0G640_TEMP))
else :
    ans.append('NONE')
if len(C0R190_TEMP)>0 :
    ans.append(max(C0R190_TEMP))
else :
    ans.append('NONE')
if len(C0X260_TEMP)>0 :
    ans.append(max(C0X260_TEMP))
else :
    ans.append('NONE')


#=======================================

# Part. 4
#=======================================
# Print result
    #print(target_data)
final = []
for i in range (5):
    final.append([name[i], ans[i]])
print(final)
# name ans
#========================================