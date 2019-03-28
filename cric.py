import time
import keyboard
from selenium import webdriver
options=webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome('C:\\Users\\bellapukonda\\Desktop\\auto\\chromedriver.exe',options=options)
driver.get('https://www.cricbuzz.com/live-cricket-full-commentary/21654/afg-vs-ire-only-test-afghanistan-v-ireland-in-india-2019')
runs=driver.find_elements_by_class_name('cb-com-ovr-sum-itm')
over=driver.find_elements_by_class_name('cb-font-18')
a=[]
teamscore=[]
Wickets=[]
for i in runs:
    if('Runs Scored' in i.text):
        s=i.text
        s=s.split('\n')
        s=s[0]
        s.split(':')
        s=s[-1]
        s.strip()
        a.append(s)
    if('Score after' in i.text):
        #print(i.text)
        ss=i.text
        ss=ss.split('\n')
        ss=ss[1]
        #print(ss)
        ss=ss.split()
        TeamName=ss[0]
        ss=ss[1]
        ss=ss.split('-')
        wic=ss[-1]
        teamscore.append(ss[0])
        Wickets.append(wic)
        
over=over[2:]
print(len(over),len(teamscore),len(Wickets))
for i in range(len(over)):
    print(over[i].text,a[i],teamscore[i],Wickets[i])


