# Name->Anshh Chaturvedi
# Roll Number->102003665
# Subgroup-> 3CO26
# # Mashup Assignment (UCS654->Predictive Analytics)
# email->anshh1010@gmail.com
# pw->Hello@123
from flask import Flask, render_template,request,redirect,url_for
from flask_bootstrap import Bootstrap
import pandas as pd
import numpy as np
import sys
import os
import youtube_dl 
import glob 
import os 
import sys 
from pydub import AudioSegment 
from pytube import YouTube
import zipfile
from youtubesearchpython import VideosSearch
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
app=Flask(__name__)
Bootstrap(app)
formData={}

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/", methods=['POST'])
def home():
    name=request.form.get("name", False)
    n=request.form.get("n", False)
    time=request.form.get("time", False)
    email=request.form.get("email", False)
    main(name,n,time,email)
    return "<h1><center>Thanks</center></h1>"


def main(name,n,time,email):
    n=int(n)
    time=int(time)
    print(name)
    print(n)
    print(time)
    # name=sys.argv[1]
    # n=int(sys.argv[2])
    # time=sys.argv[3]
    # output=sys.argv[4]
    print(email)
    output="102003665"
    from youtubesearchpython import VideosSearch

    videosSearch = VideosSearch(name, limit = n)

    print(videosSearch.result())
    print(type(videosSearch.result()))
    print(videosSearch.result()["result"][0]["link"])
    links=[]
    for i in range(n):
        links.append(videosSearch.result()["result"][i]["link"])
    print(links)
    for i in range(len(links)):
        download_audio(links[i])
    initial = "0:00"
    final = "00:"+str(time)
    list_of_mp3s = glob.glob('./*.mp3')
    for i in range(n):
        filename = list_of_mp3s[i]
        trimmed_file = get_trimmed(filename, initial, final)
        trimmed_filename = "audio"+str(i)+".mp3"
        print("Process concluded successfully. Saving trimmed file as ", trimmed_filename)
        trimmed_file.export(trimmed_filename, format="mp3")
    sound1=AudioSegment.from_mp3("./audio0.mp3")
    for i in range(1,n):
        audio_file="./audio"+ str(i)+".mp3"
        sound2=AudioSegment.from_mp3(audio_file)
        sound1=sound1.append(sound2)
        os.remove(audio_file)
    sound1.export("./"+output+".mp3",format="mp3")
    zip = zipfile.ZipFile(output+".zip", "w", zipfile.ZIP_DEFLATED)
    zip.write("./102003665.mp3")
    zip.close()
    fromaddr ="aaabb29072002@gmail.com"
    toaddr = email
    msg = MIMEMultipart()

# instance of MIMEMultipart

# storing the senders email address
    msg['From'] = fromaddr

# storing the receivers email address
    msg['To'] = toaddr

# storing the subject
    msg['Subject'] = "Mashup from 102003665"

# string to store the body of the mail
    body = "Heylo, this is my submission for Assignment 2, Mashup"

# attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

# open the file to be sent
    filename = "102003665.zip"
    attachment = open("./102003665.zip", "rb")

# instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

# To change the payload into encoded form
    p.set_payload((attachment).read())

# encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# attach the instance 'p' to instance 'msg'
    msg.attach(p)

# creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
    s.starttls()

# Authentication
    s.login(fromaddr, "utqbdsoeenjdgkum")

    text = msg.as_string()

# sending the mail
    s.sendmail(fromaddr, toaddr, text)

# terminating the session
    s.quit()
    # os.remove("audio0.mp3")
    # os.remove(output)

def download_audio(yt_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([yt_url])

def get_video_time_in_ms(video_timestamp):
    vt_split = video_timestamp.split(":")
    if (len(vt_split) == 3): 
        hours = int(vt_split[0]) * 60 * 60 * 1000
        minutes = int(vt_split[1]) * 60 * 1000
        seconds = int(vt_split[2]) * 1000
    else: 
        hours = 0
        minutes = int(vt_split[0]) * 60 * 1000
        seconds = int(vt_split[1]) * 1000

    return hours + minutes + seconds


from pydub import AudioSegment
def get_trimmed(mp3_filename, initial, final = ""):
    if (not mp3_filename):
        
        raise Exception("No MP3 found in local directory.")
    
    sound = AudioSegment.from_mp3(mp3_filename)
    t0 = get_video_time_in_ms(initial)
    print("Beginning trimming process for file ", mp3_filename, ".\n")
    print("Starting from ", initial, "...")
    if (len(final) > 0):
        print("...up to ", final, ".\n")
        t1 = get_video_time_in_ms(final)
        return sound[t0:t1] 
    return sound[t0:] 




# name=sys.argv[1]
#     n=int(sys.argv[2])
    # time=sys.argv[3]
if __name__=="__main__":
    app.run(debug=True)

