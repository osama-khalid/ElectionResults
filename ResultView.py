import requests
import json
import operator
File=open('NA_seats_2018.csv').read().split('\n')
local={}
for i in range(1,len(File)):
    if len(File[i])>1:
        row=File[i].split(',')
        local[row[0]]=[row[2],row[3]]

result=requests.get('https://election-res.herokuapp.com/api/results')
result=json.loads(result.content)
seat={}
for i in range(0,len(result)):
    row=result[i]
    seat[row['seat']]=i
    
SortSeat=sorted(seat.keys(),key=operator.itemgetter(0))    

listing=[]
for row in SortSeat:
    L=len(result[seat[row]]['results'])
    for i in range(L):
        print(local[row][1],'-',local[row][0],'-',result[seat[row]]['seat'],' - ',result[seat[row]]['results'][i]['candidate'],' - ',result[seat[row]]['results'][i]['party'],' - ',result[seat[row]]['results'][i]['votes'])
        
    print(" ")