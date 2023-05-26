from datetime import datetime 
import random
time=datetime.today()

def handle_responses(message)-> str:
    if(message.lower()=="hii"):
        return 'Namaste'
    elif(message.lower()=="who are u"):
        return 'Mein Baborao Ganpatrao Apte'
    elif(message.lower()=="how to earn 30 lakhs in 30 days?"):
        return 'ARE BABA RE BABA YEH BAHUT KAAM TIME NAHI HO GAYA AKHIR 30 SAAL KA TIME TO DENA CHAHIYE NA!!'
    elif(message.lower()=="what is the time now"):
        return 'Time to tera kharap chal raha hai '
    elif(message.lower()=='roll a dice'): 
        return str(random.randint(1,6))
    elif(message.lower()== 'time please'):
        return str(time)
    else:
        return 'kahana kya caha rahe ho yaar'