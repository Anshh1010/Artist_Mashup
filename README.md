# Artist_Mashup
##  Make a mashup of your favourite Artist's music
This is a python project that takes asks the user about their favourite artist, the number of songs and the length of each song that they want in the mashup.   
Implemented using flask and HTML.   

##   Libraries used:  
1) Flask(Flask, flask_bootstrap render_template,request,redirect,url_for)   
2) Pandas  
3) Numpy    
4) Sys    
5) OS   
6) Glob   
7) Pydub(AudioSegment)    
8) Pytube(YouTube)    
9) Zipfile    
10) smtplib   
11) email.mine(MIMEMultipart,MIMEText,MIMEBase,encoders)        
I've used the youtubesearchpython package, which I got from pypi.org(https://pypi.org/project/youtube-search-python/).    
## System Requirements     
1) Python Version 3 or above
2) Installation of aforementioned libraries
3) ffmpeg and ffprobe      
## Working    
The program works in the following steps:  
### -> The user enters the artist's name, the number of songs, the trim time, i.e how long do they want each song to be in the mashup and their email ID.  
<img width="659" alt="Screenshot 2023-02-13 at 12 04 46 AM" src="https://user-images.githubusercontent.com/72307339/218330045-66cda9a2-b725-4558-a084-e3e965fa8a1f.png">

### -> The code takes these inputs from the HTML form and runs it's search on Youtube.    
### -> The URLS of the artist's videos are retrieved.   
<img width="1224" alt="Screenshot 2023-02-13 at 12 07 31 AM" src="https://user-images.githubusercontent.com/72307339/218330183-ce1845bf-b1d6-45ca-bd63-228d7b1cedf9.png">. 
### -> The songs are downloaded from these URLS from YouTube, then they are trimmed.    
<img width="1119" alt="Screenshot 2023-02-13 at 12 09 21 AM" src="https://user-images.githubusercontent.com/72307339/218330254-c07a3be1-1aa7-42a0-9ee3-70d5e4344ee1.png">   

### -> After trimming, they are merged and put into a ZIP file and mailed to the user.    
<img width="485" alt="Screenshot 2023-02-13 at 12 09 58 AM" src="https://user-images.githubusercontent.com/72307339/218330285-2481cdf3-d035-4dba-9002-916e2fc76c33.png">
<img width="914" alt="Screenshot 2023-02-13 at 12 11 18 AM" src="https://user-images.githubusercontent.com/72307339/218330335-1afe4a9c-7ccc-4ed6-bacc-b6f0ad8c1054.png">
   
### Powered by Coffee
