print("Hello! I am an Ai Bot. What's your name?: ")
name = input()

print(f"Hi Nice to met you {name}!")

print("How are you feeling today? (good/bad)")
mood = input().lower()

if mood == "good":
    print("I'm happy to here that!")
elif mood == "bad":
    print("I'm sorry to hear that, everyone has bad days, so I completely understand!")
else:
    print("I get that it's difficult to explain your emotions, and you feel muddled, but that's alright!")

print(f"It was nice chatting with you {name}. Goodbye!")