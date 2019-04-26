import urllib.request as ureq
from bs4 import BeautifulSoup as soup
uopen=ureq.urlopen("http://quotes.toscrape.com/")
uread=uopen.read()
uopen.close()
usouped=soup(uread,'html.parser')
taglist=usouped.findAll("span",{"class":"tag-item"})
list=[]
for tags in taglist:
    list.append(tags.a["href"])
i=0

for l in list:
    usubopen=ureq.urlopen("http://quotes.toscrape.com"+l)
    i+=1
    usubread=usubopen.read()
    usubopen.close()
    usubsouped=soup(usubread,'html.parser')
    title=l.split("/")
    print("--------------------\n"+title[-2].title()+" Thought:-\n--------------------")
    quotes=usubsouped.findAll("div",{"class":"quote"})
    j=0
    for quote in quotes:
        string_content=quotes[j].text
        list_of_content=string_content.split("\n")
        temp=list_of_content[2].split(" ")
        author_name=" ".join(temp[1:])
        print(list_of_content[1]+"\nAuthor Name:"+author_name+"\n")
        j+=1
    print("****------------------****\n\n")
