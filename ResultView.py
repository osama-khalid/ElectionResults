import requests
import json
import operator
import time
from bs4 import BeautifulSoup as BS
File=open('NA_seats_2018.csv').read().split('\n')
local={}
order=[]
for i in range(1,len(File)):
    if len(File[i])>1:
        row=File[i].split(',')
        local[row[0]]=[row[2],row[3]]
        order.append(row[0])
slp=0
Total={}
file=open('ElectionResults.csv','w')
for S in order:        
    slp=slp+1
    if slp%50==0:
     	
        time.sleep(4)
    r=requests.post("https://www.geo.tv/election/election_constituency_result", data={'seat':S})
    page=r.content
    soup = BS(page, 'html.parser')
    seat=soup.find('h2').text
    region=local[seat][0]
    province=local[seat][1]
    candidates=soup.find('tbody').find_all('tr')
    flag=1
    for i in range(0,len(candidates)):
        endname=str(candidates[i].find('h5')).find("<s")
        name=candidates[i].find('h5').text[:endname-4]
        party=candidates[i].find('h5').text[endname-4:]
        votes=candidates[i].find_all('td')[1].text
        if i==0:
            if party not in Total:
                Total[party]=0
            Total[party]+=1    
        if votes!="-":
            print(seat,region,province,name,party,votes)
            file.write(seat+","+region+","+province+","+name+","+party+","+votes)
            flag=0
    if flag==0:
        print(" ")        
file.close()        
Ranks=sorted(Total.items(),key=operator.itemgetter(1),reverse=True)            
print('Party - Seats')
for r in Ranks:
    print(r[0],' ',r[1])            