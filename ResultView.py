import requests
import json
import operator
File=open('NA_seats_2018.csv').read().split('\n')
local={}
order=[]
for i in range(1,len(File)):
    if len(File[i])>1:
        row=File[i].split(',')
        local[row[0]]=[row[2],row[3]]
        order.append(row[0])

result=requests.get('https://election-res.herokuapp.com/api/results')
result=json.loads(result.content)
seat={}
for i in range(0,len(result)):
    row=result[i]
    seat[row['seat']]=i
    
SortSeat=sorted(seat.keys(),key=operator.itemgetter(1))    
SortSeat.sort()
print("Province",'-',"District",'-',"Constituency",' - ',"Candidate",' - ',"Party",' - ',"Total Votes")
print(" ")
FinalRank={}
listing=[]
for row in order:
    if row in SortSeat:
        L=len(result[seat[row]]['results'])
        if result[seat[row]]['results'][0]['party'] not in FinalRank:
            FinalRank[result[seat[row]]['results'][0]['party']]=0
        FinalRank[result[seat[row]]['results'][0]['party']]+=1    
        for i in range(L):
            print(local[row][1],'-',local[row][0],'-',result[seat[row]]['seat'],' - ',result[seat[row]]['results'][i]['candidate'],' - ',result[seat[row]]['results'][i]['party'],' - ',result[seat[row]]['results'][i]['votes'])
            
        print("Total Votes:",result[seat[row]]['Votes Polled'],"Valid Votes:",result[seat[row]]['Valid Votes'],"Rejected Votes:",result[seat[row]]['Rejected Votes'])
        print(" ")


Ranks=sorted(FinalRank.items(),key=operator.itemgetter(1),reverse=True)            
print('Party - Seats')
for r in Ranks:
    print(r[0],'-',r[1])