# tocCrawler

A web-scraper targeted at a website to download 1000+ chapters of a free web novel and pack it into a pdf file.

This project was interesting because the website was rarely consistent in its use of headers, so further tools to ensure the integrity of downloaded files needed to be created.

The method I used to find the content of a chapter was inefficient, however the website often changed the structure of newly uploaded chapters, so this method was necessary.

Storing every chapter in memory is very ram hungry, and eventually bogs down my CPU. This was a one-off tool, so the time could be spent, however it would be much much faster to recursively merge every file.

This project was created using python and an ipynb notebook. 
