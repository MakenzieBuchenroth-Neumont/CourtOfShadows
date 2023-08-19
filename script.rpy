# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default gameend = False

define mc = Character("Lady Elisa")
define court = Character("Subordinate")
define king = Character("King Raymond")
define c_m = Character("Sire Shull")
define c_w = Character("Mage Kirk")
define c_f = Character("Lady Sarah")
define knight = Character("Dame Janet")
define b = Character("Beggar")
define prince = Character("Prince Fox")

init:
    $ k_happiness = 50 # 100
    $ p_happiness = 50 # 100
    $ influence = 30     # 100
    $ respect = 0 # 100
    $ days = 0

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg corridor day

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show mc fem neutral at left

    # These display lines of dialogue.

    "In this game, you take the role of 'Lady Elisa', a member of the King's Court."

    show mc fem neutral at center

    "You will need to manage different stats to keep yourself in power."

    "{color=#507D7C}King's Happiness{/color}, {color=#6D9F31}People's Happiness{/color}, {color=#9F5E31}Influence{/color}, and {color=#9F3197}Respect{/color}."

    "{color=#507D7C}King's Happiness{/color} is how happy the King is based on how well he agrees with your deecisions."

    "{color=#6D9F31}People's Happiness{/color} is how happy the kingdom's people are with the 'King's' decisions."

    "{color=#9F5E31}Influence{/color} is the ability for the kingdom's people to agree, and to help you with your decisions."

    "{color=#9F3197}Respect{/color} is how likely your fellow court members are to go along with your court decisions."

    "Your decisions will impact your stats positively or negatively. Be sure to keep an eye on them; if either of the happiness' get too low or too high, you will lose your spot on the King's court."

    while not gameend:

        call callEncounter
        call callEncounter
        call callEncounter

        if p_happiness >= 100:
            call pHighDeath
            $ gameend = True
        elif p_happiness <= 0:
            call pLowDeath
            $ gameend = True
        elif k_happiness >= 80:
            call kHighDeath
            $ gameend = True
        elif k_happiness <= 20:
            call kLowDeath
            $ gameend = True

        $ days += 1
        scene bg black
        "End day [days]" 
        " {color=#507D7C}King's Happiness{/color}:⠀⠀⠀[k_happiness]\n
        {color=#6D9F31}People's Happiness{/color}:⠀ [p_happiness]\n
        {color=#9F5E31}Influence{/color}:⠀⠀⠀⠀⠀⠀⠀⠀[influence]\n
        {color=#9F3197}Respect{/color}:⠀⠀⠀⠀⠀⠀⠀⠀⠀[respect]"

    # This ends the game.

    return

label shifterfolk1:
    scene bg mc office

    show mc fem neutral at right

    show sub male neutral at left

    court "The shifterfolk are upset. They think they are being opressed."

    menu:
        "What shall we do?"

        "They can deal with it themselves.":
            $ p_happiness -= 5 
            $ respect += 5

        "They shouldn't have rights anyway!":
            $ influence -= 5
            $ k_happiness += 5
            
        "Send the guards to help" if influence > 30:
            $ k_happiness -= 10
            $ p_happiness += 10

    return

label shifterfolk2:
    scene bg mc office

    show mc fem neutral at right

    show sub male neutral at left

    court "The shifterfolk are rioting!"

    menu:
        "What shall we do?"

        "Give them their rights!":
            $ p_happiness += 5
            $ k_happiness -= 5
            
        "Ensure the safety of the people.":
            $ k_happiness -= 5
            $ respect += 5

        "Send the guards to disperse the rioters!" if influence > 50:
            $ p_happiness -= 10
            $ respect += 10

    return

label callEncounter:
    $ currentencounter = renpy.random.randint(0, 1)

    if currentencounter == 0:
        call shifterfolk1
    elif currentencounter == 1:
        call shifterfolk2

    return

label pHighDeath:

    show mc fem neutral at center

    "The people rioted for you to become king, the king didn't like that."

    return

label pLowDeath:

    show mc fem neutral at center

    "The people grew distastful of royalty and usurped the royal family, you were caught in the crossfire."

    return

label kHighDeath:

    show mc fem neutral at center

    "The court grew jealous of your favor with the king, they got you in the night."

    return

label kLowDeath:

    show mc fem neutral at center

    "The king thought you had no respect for him, and beheaded you immediately"

    return
