#!/usr/local/bin/python3

import os
import time

os.system("clear")

def print_menu():
    print("Choose an option from the menu below.")
    print("1. Go to email")
    print("2. Review nice list")
    print("3. Review naughty list")
    print("4. Log out")

def sleepy_dots(num_seconds):
    for count in range(num_seconds):
        print(".", end='', flush=True)
        time.sleep(1)

email2 = """
From: Emily
To: Santa
Subject: What I want for Christmas

Dear Santa Claus,
I've been a really good girl this year. My parents said so. I want a stuffed animal 
and a barbie doll. I left you some choco cookies and milk. I left a carrot and some 
homade reindeer food for your reindeers.

Love, Emily
"""

email3 = """
From: Rudolph
To: Santa
Subject: Reindeer Games

Hi Santa,
I just wanted to let you know that I feel kind of left out.  The other 
reindeers won't include me in their games (like Monopoly).  Also they've 
been calling me names. (like Pinocchio)
 
Maybe you can do someting about this?  If not that's like totally ok.  

Thanks,
Rudolph
"""

email4 = """
From: Jack
To: Santa Clause
Subject: Chris miss

Deer Santa Clause

I Jack
I want truk
I want spasse ship
Sistor want dol
Momy want gud nite seep
i lef cokies an milk
i lef carot and rain deer foo
luv Jack
"""

def print_emails():
    print("\nFrom: Head Elf")
    print("To: Santa Claus")
    print("Subject: Tool Chest")
    print("\nHi Santa,")
    print("I locked the tool chest. The combination is your favorite number.")
    print("- Head Elf")
    input("\nPress <Enter> to see next email.")
    print(email2)
    input("\nPress <Enter> to see next email.")
    print(email3)
    input("\nPress <Enter> to see next email.")
    print(email4)
    


correct_password = "Santa"
password_entered = ""
while(password_entered != correct_password):

    password_entered = input("\nEnter Password to Login: ")

    if password_entered == correct_password:
        print("YOU GOT IT!")
    else:
        print("Sorry, but your answer is WRONG! Please try again in 30 seconds.")
        sleepy_dots(30)

print_menu()
menu_choice = input(" Your menu choice: ")
if menu_choice == "1":
    print_emails()
