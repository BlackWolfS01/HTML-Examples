import random
'''
****** Change Log *******
Wednesday, March 4, 2020:
Chapter 1 Section Test and Bug Tracking
Checked logic and step-by-step run through
Thursday, March 5, 2020
Final Version
Features: Opening Story Intro, Randomized Obstacles,Selectable Player Responses

'''
# List of Campus Buildings
buildings = ['klotsche','union','nwq','cunnningham','library','mellencamp','norris','mitchell']
# List of Player Actions
actions = ['walking','talking','driving','riding','class']
# List of possible Events
events = []
# List of potential Obsticles
obsticles = ['swarm','pen','nap','accident','snow']
# Player Name
name = ''
# Current Player Location
location = ''

# Dictionary of potential Obstacles; Easily expandable
obsticle = {
  'swarm': "You hear a thundering whir as you step out of Union. You turn your head to see a mob of green and black scooters gliding en mass down the street, riders drunk on the power of a small electric motor. One. After. The. Other. They zip past, blocking you from crossing. The stream has no end in sight; just an endless wall of scooters.",
  'pen': "Pen guy is back, and thank goodness, you forgot your pens. You’ve heard the lore, but never spoke to him before. “I’ll just pop over quick and ask for one.” One pen and 20 minutes later, you detangle yourself from the conversation.",
  'nap': "You walk past the couches in the [building], and their siren song calls to you. “I can just sit for a moment and check my phone.” Your eyes fly open and you look at the time, its 3:24pm. You fell asleep!",
  'snow': "As you walk outside, a snowflake gently lands on your nose. Then another. “Huh, I didn’t know it was going to snow”. You step into the newly fallen powder to have your feet sink up to your knees. “This is not good..” you mumble, trudging forward at a snail’s pace.",
  'accident': "You look both ways before stepping into the crosswalk. You know how crazy some students can drive, having one too many near misses.. It’s clear, so you put a foot into the street cautiously when from the corner of your eye, you see a blur and turn your head to see a low and red car charges out from a pocket dimension barrelling down the road. “Oh eff me…"
}


while True:
  # Intro prompt for players
  # Provides basic instructions on how to play the game
  print("If you wish to quit, type 'quit'")
  playerInput = input("Please Enter your Name:")
  name = playerInput

  print("Hello, "+ name + ". It's currently 3:00pm in the Student Union. And your Application Development class is at 3:30 in the Cunningham Hall. You leave for class and")
  
  # Randomly selects an obstacle. Could easily rewritten to actually use the number of keys aavailable in obsticles dictionary. The .keys() class method basically return a list of all of keys in the dictionary
  i = random.randint(0, 4)
  o = obsticles[i]
  # 
  for obst in obsticle.keys():
    if o == obst:
      print(obsticle[obst])


  r = {
    'avoid': "You avoid the trouble",
    'fight': "You fight through it"
  }

  # Listing of available responses for the player
  print("Player Responses: ")
  for key in r.keys():
    print(key)
  print()

  playerInput = input("What will you do? ")

  # Checks player's response against what's available in the dictionary. Could easily be expand to cover multiple responses. Even being determined by the type of obstacle the player is dealing with
  for resp in r.keys():
    # This is a conditional check technique. Instead of a '==' double equals sign check. You use an is nnot check, '!='. An exclamation symbol and equals sign.
    if playerInput != resp:
      print("Please select a proper action")
      continue
    else:
      print(r[resp])
      print("That was close. You made it to class.")
      break
      


  if playerInput == 'quit':
    print("Closing out program.\n Goodbye")
    break
