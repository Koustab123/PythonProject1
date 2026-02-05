#1----importing random module
import random
#2-- --create subjects
subjects = [
    "sharukh khan",
    "rohit sharma",
    "Lionel Messi",
    "neymar jr",
    "narendra modi",
    "Cristiano Ronaldop",
    " a group of chapris "
]
actions = [
    "launches",
    "drinking",
    "dances with",
    "playing",
    "declares wars with",
    "celebrates their defeat"
]
places_or_things = [
    "at red fort",
    "at bathroom",
    "at the bed",
    "in ahmedabad",
    "at the park"
]
# start the headline generation line
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f"BREAKING NEWS {subject} {action} {place_or_thing}"
    print("---------FAKE NEWS GENERATOR------- ")
    print(headline)

    user_input = input("\nDo you want another headline? (yes/no)").strip().lower()
    if user_input == "no":
        break

print("Thankyou for using FAKE NEWWS GENERATOR :)))) VISIT AGAINNNNNNNNNN !!! ❤️❤️❤️")