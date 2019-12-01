#!/usr/local/bin/python3

import os
import time

correct_password = "$@nt@25"
correct_deactivate = "1891225"

os.system("clear")

def print_menu():
    os.system("clear")
    print("Choose an option from the menu below.")
    print("1. Go to email")
    print("2. Review nice list")
    print("3. Review naughty list")
    print("4. De-activate Sled Auto-Destruct")
    print("5. Log out")

def sleepy_dots(num_seconds):
    for count in range(num_seconds*2):
        print(".", end='', flush=True)
        time.sleep(0.5)

email4 = """
From: Emily
To: Santa
Subject: What I want for Christmas

Dear Santa Claus,
I've been a really good girl this year. My parents said so. I want a stuffed animal 
and a barbie doll. I left you some choco cookies and milk. I left a carrot and some 
homade reindeer food for your reindeers.

Love, Emily
"""

email1 = """
From: Rudolph
To: Santa
Subject: Reindeer Games

Hi Santa,
I just wanted to let you know that I feel kind of left out.  The other 
reindeers won't include me in their games (like Monopoly).  Also they've 
been calling me names (like Pinocchio).
 
Maybe you can do someting about this?  If not that's like totally ok.  

Thanks,
Rudolph
"""

email2 = """
From: Jack
To: Santa Clause
Subject: Chris miss

Deer Santa Clause

I Jack
I wan truk
I wan spasse ship
Sistor wan dol
Momy wan gud nite seep
i lef cokies an milk
i lef carot an rain deer foo
luv Jack
"""

email3 = """
From: Mrs. Clause
To: Santa Clause
Subject: Cell Phone

Hi Honey,

I know how busy you are this time of year. 
If you forget your cell phone combination just remember:

Hope
Joy
Peace

Love,
 Your Christmas Present

P.S.  If you lose your key to the black toolbox again - I taped the spare key under the t&C^%X$##$!X*......  <EMAIL TRANSMISSION INTERRUPTED>

"""

email5 = """
From: The Easter Bunny
To: Santa Claus
Subject: Books

Dear Santa,

I sent you my favorite books. I hope you FIND them as enjoyable as I 
did. Please take a LOOK and let me know what you think: The Fellowship
of the Ring, The Secret Garden, and Miracle on 34th Street.  

- The Easter Bunny
"""

email6 = """
From: Frosty The Snowman
To: Santa Clause
Subject: Puzzles

Dear Santa, 

I sent you two puzzles.
One is a picture of an albino elephant drinking milk in a snowstorm,
and the other is a picture of a Christmas Tree with a star and no ornaments. It has a blue sky.
The one with the Christmas Tree is missing a few pieces and has green stars on the back.
Sorry about it's missing pieces.

- Frosty The Snowman 
""" 
def print_emails():

    #os.system("clear")
    #print(email1)
    #input("\nPress <Enter> to see next email.")
    #os.system("clear")
    #print(email2)
    #input("\nPress <Enter> to see next email.")
    os.system("clear")    
    print(email3)
    input("\nPress <Enter> to see next email.")
    #os.system("clear")
    #print(email4)
    #input("\nPress <Enter> to see next email.")
    os.system("clear")
    print(email5)
    input("\nPress <Enter> to see next email.")
    os.system("clear")
    print(email6)
    input("\nPress <Enter> to go back to menu.")
nicelist = """

    NICE LIST
---------------
  Torin  
  Wendy  
  Oscar  
  Fred   
  Olivia 
  Uma 
  Robin
  Emily
  Ian
  Gary
  Henry
  Tom
"""
    


def print_nicelist():
    os.system("clear")
    print(nicelist)
    input("Press <Enter> to go to the menu.")

naughtylist = """

   NAUGHTY LIST
----------------    
  Enni
  Evens 
  Noe
"""

def print_naughtylist():
    os.system("clear")
    print(naughtylist)
    input("Press <Enter> to go to the menu.")

def check_disable():
    os.system("clear")
    print("Please enter the code to disable self destruct.  (Press <Enter> to go back to the main menu.)")
    disable = input("--> ")
    number_correct = 0
    for index in range(min(len(correct_deactivate), len(disable))):
        if (correct_deactivate[index] == disable[index]):
             number_correct += 1
    if disable == correct_deactivate:
        print(" YOU WON! YOU SAVED CHRISTMAS! CONGRATS!")
        time.sleep(60*10)
    else:
        if (disable != ""):
            print(f" Sorry but your answer is WRONG!")
            print(f" You got {number_correct} out of {len(correct_deactivate)} digits correct.")
            print("  Please wait 20 seconds, and then you will be returned to the main menu.")
            sleepy_dots(20)
        

while(True):
   
    password_entered = ""
    while(password_entered != correct_password):
        os.system("clear")     
        password_entered = input("\nEnter Password to Login: ")
        
        if password_entered == correct_password:
            print("YOU GOT IT!")
        else:
            print("Sorry, but your password is incorrect! Please try again in 20 seconds.")
            sleepy_dots(20)
    menu_choice=""
    while(menu_choice != "5"):
        print_menu()
        menu_choice = input("Your menu choice: ")
        if menu_choice == "1":
            print_emails()
        if menu_choice == "2":
            print_nicelist()
        if menu_choice == "3":
            print_naughtylist()
        if menu_choice == "4":
            check_disable()
