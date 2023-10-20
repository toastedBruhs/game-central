import random

bubble_lines = ['But what are they?', 'And what do they do?', '*nom*', 'I got it, boss! *licks*', 'And how do they-', 'Ha Ha Ha Ha', '*silence*', "Made with all the love I'm legally allowed to give"]

name = input("Hello and welcome to the Bubble Chatbot, where you can talk with everyone's favorite Amazing Digital Circus character, Bubble! Before we begin, please enter your username: ")
print('Oh, here comes Bubble now! Enjoy! (Say "(changelog) to see the changelog. You will have to then reload the site to chat)')

print("bubbleBussy123:")
print(" hi")

while True:
    print(f"{name}:")
    user_response = input(" ")
    if "~" in user_response:
        print("bubbleBussy123:")
        print(" kill yourself")
    elif user_response == "(changelog)":
        print("10/19/23: Site created, pilot lines added")
        break
    else:
        print("bubbleBussy123:")
        print(" " + random.choice(bubble_lines))
