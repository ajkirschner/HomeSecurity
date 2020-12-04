#python3
import ezgmail
from datetime import date
from datetime import datetime
import glob 
import os

def main():
    # get path to motion clip screenshot
    day = date.today().strftime("%m-%d-%Y")
    time = datetime.now().strftime("%H:%M")
    path = '/mnt/tpshare/Motion Clips/' + day
    jpegfilelist = glob.glob(path + '/*.jpg')
    print(jpegfilelist[0])

    # send email with attached screenshot
    ezgmail.init(tokenFile='/home/pi/Documents/tokens/token.json',credentialsFile='/home/pi/Documents/tokens/credentials.json')
    #ezgmail.send(recipient, subject, body, attachments=None, sender=None, cc=None, bcc=None, mimeSubtype='plain', _threadId=None)
    ezgmail.send('ajkirschner16@gmail.com','Motion Detected At ' + time,jpegfilelist[0],attachments=jpegfilelist[0],sender='Alex Kirschner')

    # delete the screenshot
    os.remove(jpegfilelist[0])

if __name__ == '__main__':
    main()


