from flask import Flask
import time 
import random
from AppOpener import open
import pywhatkit as kit


app = Flask(__name__)
print()
print("HLW I AM A CHAT BOT")
print()
@app.route('/')

def hello_world():
    return 'Hello World'
# app.add_url_rule(‘/’)
def help():
    print("YOU CAN CHAT WITH THE FOLLOWING:")
    print()
    print("1: hii")
    print()
    print("2: what are you")
    print()
    print('3: How are you')
    print()
    print("4: what is the time")
    print()
    print('5: roll a dice')
    print()
    print("6: open application")
    print()
    print('7: play song')
    print()
    print('8: google search')
    print()
    print("9: weather")
    print()
    print('10: play games')
    print()

print()
print('TYPE START TO START THE BOT OR END FOR THE BOT TO STOP')
print()
start=input('START/END: ')
print()
#print("To see the commands list you can type HELP ")

def games():
    print('BOT: ')
    print('1: Tic Tac Toe')
    print()
    print('2: Pac man')
    print()
    print('3: Earth day quiz')
    print()
    print('4: Snake')
    print()
    print('5: Minesweeper')
    print()
    gname=input('BOT: ENTER YOUR CHOICE: ')
    if(gname =='1'):
        print("BOT: Opening Tic Tac Toe")
        time.sleep(1)
        kit.search('google tic tac toe')
    elif(gname=='2'):
        print("BOT: Opening Pac Man")
        time.sleep(1)
        kit.search('google Pac Man')
    elif(gname=='3'):
        print("BOT: Opening Earth day quiz")
        time.sleep(1)
        kit.search('Google earth day quiz')
    elif(gname=='4'):
        print("BOT: Opening Snake")
        time.sleep(1)
        kit.search('google snake')
    elif(gname=='5'):
        print("BOT: Opening Minesweeper")
        time.sleep(1)
        kit.search('google minesweeper')
def weather():
    print("BOT: Fetching Weather")
    time.sleep(1)
    kit.search('weather')
def worng(msg):
    time.sleep(1)
    kit.search(msg)
def search():
    search=input("BOT: What do you want to search: ")
    print('BOT: SEARCHING',search)
    time.sleep(1)
    kit.search(search)
def yt():
    sname=input('BOT: Enter song name: ')
    print('BOT: NOW PLAYING',sname)
    time.sleep(1)
    kit.playonyt(sname)
def app():
    nm=input("BOT:  APP NAME: ")
    time.sleep(1)
    open(nm.lower(),match_closest=True)
def countdown(t):
    print()
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print()
def decide(start):
    if(start=='start'):
        countdown(3)
        print()    
        print('BOT: WELCOME..')
        print()
    elif(start=='end'):
        countdown(3)
        print()
        print("BOT: SIGNING OUT...")           
if(start.lower()=='end'):
    decide("end")
else:
    
    print("LET'S  DIVE IN....")
    decide("start")
    print("To see the commands list you can type HELP ")
    while(start.lower()=='start'):
        msg=input('YOU: ')
        if(msg.lower()=='hii' or msg == '1'):
            print("BOT: Hey There..")
            print()
        elif(msg.lower()=='help'):
            help()
            print()
        elif(msg.lower()=='what are you' or msg == '2'):
            print('BOT: I am a Narrow AI who can do a limited no. of tasks.')
            print()
        elif(msg.lower()=='how are you' or msg=='3'):
            print("BOT: I am perfectly fine and hope u too")
            print()
        elif(msg.lower()=='what is the time'or msg == '4'):
            ctime=time.strftime("%H:%M:%S")
            print("BOT: ",ctime)
            print()
        elif(msg.lower()=='roll a dice'or msg == '5'):
            print("BOT: ",str(random.randint(1,6)))
            print()
        elif(msg.lower()=='open application' or msg == '6'):
            app()
            print()
        elif(msg.lower()=='play song'or msg=='7'):
            yt()
            print()
        elif(msg.lower()=='google search'or msg=='8'):
            search()
            print()
        elif(msg.lower()=="weahther"or msg == "9"):
            weather()
            print()
        elif(msg.lower()==' play tic tac toe' or msg == '10'):
            games()
        elif(msg.lower()=='end'):
            print('BOT: Bye Bye....')
            print()
            break
        else:
            print('BOT: Sorry didn\'t get it....')
            print("BOT: Searching For Solution On The Internet")
            time.sleep(1)
            worng(msg)
            print()
    decide('end')
    print()


if __name__ == '__main__':
 
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()


 
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.

# ‘/’ URL is bound with hello_world() function.

 
# main driver function
