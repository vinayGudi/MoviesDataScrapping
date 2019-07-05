import bs4
from urllib.request import urlopen as uReq
import pandas as pd 
from bs4 import BeautifulSoup as soup
import csv
import sqlalchemy
engine=sqlalchemy.create_engine("mysql+pymysql://root:8146@localhost:3306/movies")



starsList=[]
movieName=[]
runTimeList=[]
ratingList=[]
genreList=[]
starsList=[]
se=[]
o=1
while(True):
    print(o)
    if o>1500:
        break 
    my_url="https://www.imdb.com/search/title/?genres=horror&start="+str(o)+"&explore=title_type&ref_=adv_nxt"
    o=o+50
    uClient=uReq(my_url)
    page_html=uClient.read()
    uClient.close()
    page_soup=soup(page_html,"html.parser")
    s=page_soup.find_all("div",{"class":"lister-item-content"})
    for i in s:
        try:
            movieName.append(i.h3.a.text)
        except:
            movieName.append("NA")
        try:
            ratingList.append(i.div.div.strong.text)
        except:
            ratingList.append(-1)
        try:    
            runtime=[j.text for j in i.findAll('span', {'class': 'runtime'})]
            runTimeList.append(runtime[0])
        except:
            runTimeList.append(-1)
        try:    
            genre=[j.text for j in i.findAll('span', {'class': 'genre'})][0].strip().replace(',','|')
            ## genreList.append(genre[-1]) 
            print(genre)
        except:
            genreList.append("NA")
        try:
            stars=[j.text for j in i.findAll('p', {'class': ''})][0].strip().replace('\n','').replace(',','|')
            se.append(stars)
               # print(ele)
               #print(stars[-1])
        except:
            starsList.append("NA")   

d={"MovieName":movieName,"Rating":ratingList,"Genre":genre,"Runtime":runTimeList,"Stars":se}
#print(len(movieName),len(ratingList),len(genre),len(runTimeList),len(starsList))
df=pd.DataFrame(d)
print(df.head())
print(df.shape)

#df.to_csv("MoviesData.csv")
df.to_sql(name="moviestable",con=engine,index=False,if_exists="replace")

           

            
            
            
    
    
