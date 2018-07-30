
# coding: utf-8

# In[20]:


#setup and get htmlDirectory
import requests
import pdfkit

url = "http://www.wuxiaworld.com/novel/child-of-light"
htmlDirectory = requests.get(url)


# In[2]:


#save to a file
directory = open('directory.txt', 'w')
directory.write(htmlDirectory.text)
directory.close()


# In[3]:


#find relevant information from html, save to a list
chapters = []
bookLink = "/novel/child-of-light/"
directory = open('directory.txt', 'r')
for line in directory:
    if ((line.find(bookLink))!= -1):
        _,_,line = line.rpartition('/')
        line = line[:-3]
        chapter = url + '/' + line
        chapters.append(chapter)
directory.close()


# In[18]:

finalHTML = open('final.html', 'w')
finalHTML.write("<meta charset=\"utf-8\" />")
finalHTML.close()


for counter, chapterURL in enumerate(chapters):
    failed = True
    #separate by every 3 chapters in this case
    chapterHTML = requests.get(chapterURL)
    chapterString = "chapter" + str(counter) + ".html"
    chapterFile = open(chapterString, 'w')
    chapterFile.write(chapterHTML.text)
    chapterFile.close()
#find content of chapter
    startHTML1 = "<p><strong><u>"
    startHTML2 = "<p><b><u>"
    startHTML3 = "<p><span><b><u><span>"
    startHTML4 = "<p><span style=\"text-decoration: underline\"><strong>"
    startHTML5 = "<strong><u>"
    startHTML6 = "<p><strong><span style=\"text-decoration: underline\">"
    startHTML7 = "<p><span style=\"text-decoration: underline;\"><strong>"
    startHTML8 = "<p><span style=\"text-decoration: underline\"><b>"
    startHTML9 = "<p><strong>"
    startHTML10= "<p><b>"
    chapterFile = open(chapterString, 'r')
    content = str()
    for line in chapterFile:
        if (((line.find(startHTML1))!= -1) or (line.find(startHTML2)!=-1) or (line.find(startHTML3)!=-1) or (line.find(startHTML4)!=-1) or (line.find(startHTML5)!=-1) or (line.find(startHTML6)!=-1) or (line.find(startHTML7)!=-1) or (line.find(startHTML8)!=-1) or (line.find(startHTML9)!=-1) or (line.find(startHTML10)!=-1)):
            line = line[:-12] + "<br>"
            content = line
            failed = False
    if (failed == True):
            print(chapterString + " failed")
    chapterFile.close()
    finalHTML = open('final.html', 'a')
    finalHTML.write(content)
    finalHTML.close()
open('final.pdf', 'w')
output = pdfkit.from_file('final.html', 'final.pdf')

