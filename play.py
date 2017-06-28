start = '''
Oh No! You slept in on the day of finals! What should you do?
You really shouldn't of stayed up last night.
'''
coffee='''
You decided to get coffe and dressed, you feel a little better but you're not sure how to get to school.
Mom already left for work and you heard a rumor that the bus was broken.
'''
run='''
You run frantically out of your house in only your pajamas. You're panting heavily and exhausted! At least you made it to to the bus, along with judgement from your neighbors
and peers for your bunny slippers.
'''
pajamas='''
You just realized you're against dress code! The teachers are right next to your classroom talking of their morning gossip, they won't move.
'''
bus='''
Luckily you were able to catch the bus, although the stranger's stares at quite scary the textbook you decided to study and cram for was very compelling!
You feel very determined to ace this test. You finally get there feeling refreshed and get an A, that test was a piece of cake! You hang it up on your wall and show everyone over the summer.
'''
mom='''
You decided to call your mother in the middle of work, she begrudgingly comes back home for you and scolds you heavily for sleeping in.
Your mother's words hit hard and you have trouble concentrating after thinking about how to make it up to her. All that worrying on top of a caffeine rush couldn't get your
mind focused, you end up with a B. Not too bad at least!
'''
long='''
You were terrified those teachers would catch you, and exhausted from running across the school. You barely make it to class and scramble into your desk.
At least it's better than suspension!
It was hard to concentrate and this morning was so hard on you. You end up barely passing the class with a D-
'''
short='''
Those teachers were too busy to care about your pajamas, but your hallway was so busy that you had to push and shove just to get around! A kid pushes you into the
lockers and once you finally make it to class you're too tired to concentrate.
You test and test as much as your tired brain can and get a B-
'''
disrespect='''
This morning was just not a good! You were so sick of the dresscode and gave the teacher a piece of your mind! Apparently it was not as appreciated as you thought it would be...
You earned yourself a detention and a big red F on your final. Maybe next time you can try better! But for now, let's hope your mom forgets about report cards.
'''
print(start)
print("Should you get dressed and some coffee or should you run outside in your pajamas?")
Decision1=input("Type either 'coffee' or 'run'")
while not (Decision1 == "coffee" or Decision1 == "run"):
    Decision1=input("Type either 'coffee' or 'run'")
if Decision1 == "coffee":
    print(coffee)
    print("Should you call mom at work or take your chances with the bus?")

    Decision2=input("Type either 'bus' or 'mom'")
    while not (Decision2 == "bus" or Decision2 == "mom"):
        Decision2=input("Type either 'bus' or 'mom'")
    if Decision2 == "bus":
                print(bus)
    if Decision2 == "mom":
            print(mom)

elif Decision1 == "run":
    print(run)
    print(pajamas)
    print("Should you take the long way to class or try to avoid eye contact?")

    Decision3=input("Type either 'long', 'short' or 'disrespect'")
    while not (Decision3 == "long" or Decision3 == "short" or Decision3 == "disrespect"):
            Decision3=input("Type either 'long', 'short' or 'disrespect'")
    if Decision3 == "long":
        print(long)
    if Decision3 == "short":
        print(short)
    if Decision3 == "disrespect":
        print(disrespect)
