# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default gameend = False

define mc = Character("Lady Elisa", color = "#404040")
define court = Character("Subordinate", color = "#404040")
define king = Character("King Raymond", color = "#404040")
define c_m = Character("Sire Shull", color = "#404040")
define c_w = Character("Mage Kirk", color = "#404040")
define c_f = Character("Lady Sarah", color = "#404040")
define knight = Character("Dame Janet", color = "#404040")
define b = Character("Beggar", color = "#404040")
define prince = Character("Prince Fox", color = "#404040")
define d_u = Character("Demihuman Union Leader Natalie", color = "#404040")

init:
    $ k_happiness = 50 # 100
    $ p_happiness = 50 # 100
    $ influence = 0 # 100
    $ respect = 0 # 100
    $ days = 0

init python:
    import random # Get the random functionality for Python

    def getNumber():
        options = range(28) # Create a list of numbers 0 to 49
        return random.choice(options)

# The game starts here.

label start:
    play music "bgm.ogg" loop volume 0.25
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

    play sound "button_se.ogg" noloop volume 0.5

    show mc fem neutral at center

    "You will need to manage different stats to keep yourself in power."

    play sound "button_se.ogg" noloop volume 0.5

    "{color=#507D7C}King's Happiness{/color}, {color=#6D9F31}People's Happiness{/color}, {color=#9F5E31}Influence{/color}, and {color=#9F3197}Respect{/color}."

    play sound "button_se.ogg" noloop volume 0.5

    "{color=#507D7C}King's Happiness{/color} is how happy the King is based on how well he agrees with your decisions."

    play sound "button_se.ogg" noloop volume 0.5

    "{color=#6D9F31}People's Happiness{/color} is how happy the kingdom's people are with the 'King's' decisions."

    play sound "button_se.ogg" noloop volume 0.5

    "{color=#9F5E31}Influence{/color} is the ability for the kingdom's people to agree, and to help you with your decisions."

    play sound "button_se.ogg" noloop volume 0.5

    "{color=#9F3197}Respect{/color} is how likely your fellow court members are to go along with your court decisions."

    play sound "button_se.ogg" noloop volume 0.5

    "Your decisions will impact your stats positively or negatively. Be sure to keep an eye on them; if either of the happiness' get too low or too high, you will lose your spot on the King's court."

    play sound "button_se.ogg" noloop volume 0.5

    while not gameend:

        call callEncounter
        call callEncounter
        call callEncounter

        if p_happiness >= 100:
            stop music
            play music "death_se.wav" noloop volume 0.5
            call pHighDeath
            $ gameend = True
        elif p_happiness <= 0:
            stop music
            play music "death_se.wav" noloop volume 0.5
            call pLowDeath
            $ gameend = True
        elif k_happiness >= 80:
            stop music
            play music "death_se.wav" noloop volume 0.5
            call kHighDeath
            $ gameend = True
        elif k_happiness <= 20:
            stop music
            play music "death_se.wav" noloop volume 0.5
            call kLowDeath
            $ gameend = True

        if influence < 0:
            $ influence = 0
        
        if respect < 0:
            $ respect = 0

        $ days += 1
        scene bg black
        "End day [days]" 
        " {color=#507D7C}King's Happiness{/color}:⠀⠀⠀[k_happiness]\n
        {color=#6D9F31}People's Happiness{/color}:⠀ [p_happiness]\n
        {color=#9F5E31}Influence{/color}:⠀⠀⠀⠀⠀⠀⠀⠀[influence]\n
        {color=#9F3197}Respect{/color}:⠀⠀⠀⠀⠀⠀⠀⠀⠀[respect]"
        play sound "button_se.ogg" noloop volume 0.5

    # This ends the game.

    return

label shifterfolk1:
    scene bg mc office

    show mc fem neutral at right

    show sub male neutral at left

    court "The shifterfolk are upset. They think they are being opressed."

    play sound "button_se.ogg" noloop volume 0.5

    menu:
        "What shall we do?"

        "They can deal with it themselves.":
            $ p_happiness -= 5 
            $ respect += 5
            play sound "button_se.ogg" noloop volume 0.5

        "They shouldn't have rights anyway!":
            $ influence -= 5
            $ k_happiness += 5
            play sound "button_se.ogg" noloop volume 0.5
            
        "Send the guards to help" if influence > 30:
            $ k_happiness -= 10
            $ p_happiness += 10
            play sound "button_se.ogg" noloop volume 0.5

    return

label shifterfolk2:
    scene bg mc office

    show mc fem neutral at right

    show sub male neutral at left

    court "The shifterfolk are rioting!"
    play sound "button_se.ogg" noloop volume 0.5

    menu:
        "What shall we do?"

        "Give them their rights!":
            $ p_happiness += 5
            $ k_happiness -= 5
            play sound "button_se.ogg" noloop volume 0.5
            
        "Ensure the safety of the people.":
            $ k_happiness -= 5
            $ respect += 5
            play sound "button_se.ogg" noloop volume 0.5

        "Send the guards to disperse the rioters!" if influence > 50:
            $ p_happiness -= 10
            $ respect += 10
            play sound "button_se.ogg" noloop volume 0.5

    return

label shifterfolk3:
    scene bg mc office
    show mc fem neutral at right
    show sub male neutral at left
    
    court "The shifterfolk have been putting on shows, and the people are reporting them as dangerous for the children."
    play sound "button_se.ogg" noloop volume 0.5

    menu:
        "What shall we do?"

        "Stop all the showings.":
            $ p_happiness -= 5
            $ respect += 5
            play sound "button_se.ogg" noloop volume 0.5

        "Increase the guard prescence near the showings.":
            $ influence -= 5
            $ p_happiness += 5
            play sound "button_se.ogg" noloop volume 0.5

        "Tell the people to protect their own children.":
            $ k_happiness -= 5
            $ respect += 5
            play sound "button_se.ogg" noloop volume 0.5

    return

label shifterfolk4:
    scene bg mc office
    show mc fem neutral at right
    show sub male neutral at left

    court "The shifterfolk have been raising concerns about their identity rights."
    play sound "button_se.ogg" noloop volume 0.5

    menu:
        "What shall we do?"

        "They are unworthy of any more rights than they already have!":
            $ influence -= 5
            $ respect += 5
            play sound "button_se.ogg" noloop volume 0.5

        "Make them empty promises.":
            $ k_happiness += 5
            $ respect -= 5
            play sound "button_se.ogg" noloop volume 0.5

    return
            
label demi1:
    scene bg mc office
    show mc fem neutral at right
    show sub male neutral at left

    court "The Church of The Four Nations has declared demihumans sinful. They want us to deal with it."
    play sound "button_se.ogg" noloop volume 0.5

    menu:
        "What shall we do?"

        "I cannot meddle in the church's affairs.":
            $ k_happiness += 5
            $ p_happiness -= 5
            play sound "button_se.ogg" noloop volume 0.5

        "They are still my people, we must protect them!":
            $ p_happiness += 5
            $ respect -= 5
            play sound "button_se.ogg" noloop volume 0.5

        "Well, they /are/ sinful. Remove their rights!" if influence > 40:
            $ p_happiness -= 10
            $ respect += 10
            play sound "button_se.ogg" noloop volume 0.5
    return

label demi2:
    scene bg mc office
    show mc fem neutral at right
    show sub male neutral at left

    court "Tensions are rising between the humans and the demihumans."
    play sound "button_se.ogg" noloop volume 0.5

    menu:
        "What shall we do?"

        "Send envoys to find a peaceful solution.":
            $ influence += 5
            $ k_happiness -= 5
            play sound "button_se.ogg" noloop volume 0.5

        "Deploy troops to quell the people":
            $ k_happiness += 5
            $ p_happiness -= 5
            play sound "button_se.ogg" noloop volume 0.5

        "Impose segregation zones!":
            $ p_happiness -= 5
            $ influence += 5
            play sound "button_se.ogg" noloop volume 0.5
    return

label demi3:
    scene bg mc office
    show mc fem neutral at right
    show demi union at left

    d_u "I am grateful for this opportunity to speak with you. Our union represents a diverse range of demi-human races residing within your land. The matter we urgently wish to address concerns the rights of demi-human workers."
    play sound "button_se.ogg" noloop volume 0.5

    menu:
        "What shall we do?"

        "Ignore their needs.":
            $ influence -= 5
            $ respect += 5
            play sound "button_se.ogg" noloop volume 0.5

        "How does this help my agenda?":
            $ p_happiness -= 5
            $ influence += 5
            play sound "button_se.ogg" noloop volume 0.5

        "Make a few small changes.":
            $ k_happiness += 5
            $ respect -= 5
            play sound "button_se.ogg" noloop volume 0.5
    return

label sub1:
    scene bg mc office
    show mc fem neutral at right
    show sub male neutral at left

    court "Good morning, m'lady, what shall we do today?"
    play sound "button_se.ogg" noloop volume 0.5

    menu:
        "What shall we do?"

        "Put up posters saying how awesome I am.":
            $ influence += 5
            $ respect -= 5
            play sound "button_se.ogg" noloop volume 0.5

        "Host a party for only prestigious guests.":
            $ respect += 5
            $ influence -= 5
            play sound "button_se.ogg" noloop volume 0.5

        "Host an event for my people.":
            $ p_happiness += 5
            $ respect -= 5
            play sound "button_se.ogg" noloop volume 0.5
    return

label sub2:
    scene bg mc office
    show mc fem neutral at right
    show sub male neutral at left

    court "A rare metal was found in the forest near our land."
    play sound "button_se.ogg" noloop volume 0.5

    menu:
        "What shall we do?"

        "What are you waiting for? Order to start digging!":
            $ k_happiness += 5
            $ respect -= 5
            play sound "button_se.ogg" noloop volume 0.5

        "Nature preservation is more important":
            $ k_happiness -= 5
            $ influence += 5
            play sound "button_se.ogg" noloop volume 0.5

        "Exploit it for personal gain.":
            $ p_happiness -= 5
            $ influence += 5
            play sound "button_se.ogg" noloop volume 0.5
    return

label prince1:
    scene bg mc office
    show mc fem neutral at right
    show prince neutral at left

    prince "There have been attacks from the east of my kingdom, and I am looking for help."
    play sound "button_se.ogg" noloop volume 0.5

    menu:
        "What shall we do?"

        "Send supplies.":
            $ p_happiness += 5
            $ respect -= 5
            play sound "button_se.ogg" noloop volume 0.5

        "Send troops.":
            $ p_happiness -= 5
            $ influence += 5
            play sound "button_se.ogg" noloop volume 0.5

        "I will not put my people in danger.":
            $ influence -= 5
            $ respect += 5
            play sound "button_se.ogg" noloop volume 0.5
    return

label sub3:
    scene bg mc office
    show mc fem neutral at right
    show sub male neutral at left

    court "A diplomatic leader from the west is visiting soon. How should we greet them?"
    play sound "button_se.ogg" noloop volume 0.5

    menu:
        "What shall we do?"

        "Show off our military strength.":
            $ k_happiness += 5
            $ p_happiness -= 5
            play sound "button_se.ogg" noloop volume 0.5

        "Hold a grand banquet for them.":
            $ respect -= 5
            $ influence += 5
            play sound "button_se.ogg" noloop volume 0.5

        "Refuse an audience with them.":
            $ k_happiness -= 5
            $ p_happiness += 5
            play sound "button_se.ogg" noloop volume 0.5
    return

label sub4:
    scene bg mc office
    show mc fem neutral at right
    show sub male neutral at left

    prince "The local miners are protesting for higher wages."
    play sound "button_se.ogg" noloop volume 0.5

    menu:
        "What shall we do?"

        "Send the knights to put a stop to this.":
            $ influence += 5
            $ k_happiness -= 5
            play sound "button_se.ogg" noloop volume 0.5

        "Concede until they stop.":
            $ k_happiness -= 5
            $ influence += 5
            play sound "button_se.ogg" noloop volume 0.5

        "Fire the workers and replace them.":
            $ respect -= 5
            $ k_happiness += 5
            play sound "button_se.ogg" noloop volume 0.5
    return

label sub5:
    scene bg mc office
    show mc fem neutral at right
    show sub male neutral at left

    court "Investigations have lead us to find an illegal slave trade."
    play sound "button_se.ogg" noloop volume 0.5

    menu:
        "What shall we do?"

        "Turn a blind in exchange for profit.":
            $ influence += 5
            $ respect -= 5
            play sound "button_se.ogg" noloop volume 0.5

        "Raid and dismantle the network.":
            $ influence -= 5
            $ p_happiness += 5
            play sound "button_se.ogg" noloop volume 0.5

        "Make the slave trade legal." if respect > 40:
            $ respect -= 5
            $ k_happiness += 5
            play sound "button_se.ogg" noloop volume 0.5
    return

label random1:
    scene bg upperclass outdoor    
    show mc fem neutral at right
    show prince neutral at left

    "While taking a stroll, you come across a confused young man. You ask if he needs help, and he introduces himself as the prince of a neighboring kingdom. You ask if he needs help, and he introduces himself as the prince of a neighboring kingdom. He is here to meet with the Princess to unite the nations and work to bring peace"
    play sound "button_se.ogg" noloop volume 0.5
    "back to the Four, but he got lost on his way to the castle and got separated from his guard."
    play sound "button_se.ogg" noloop volume 0.5
    prince "Could you give me directions to the castle?"
    play sound "button_se.ogg" noloop volume 0.5

    menu:
        "What shall I do?"

        "Walk him to the castle myself, even though I have my own duties.":
            $ k_happiness += 5
            $ respect -= 5
            play sound "button_se.ogg" noloop volume 0.5

        "Give him directions.":
            play sound "button_se.ogg" noloop volume 0.5

        "Give him the wrong directions":
            $ k_happiness -= 5
            $ influence -= 5
            play sound "button_se.ogg" noloop volume 0.5
    return

label random2:
    scene bg upperclass outdoor
    show mc fem neutral at right
    show beggar woman neutral at left

    "You come across a beggar in a richer part of the kingdom looking for a job. She is filthy and doesn’t appear to have any skills. She claims she is a great cook, and would do well as a servant to any well-to-do folk who could clothe her and feed her. People walk past her without paying her any attention."
    play sound "button_se.ogg" noloop volume 0.5

    menu:
        "What shall I do?"

        "Give her a job as one your estate's servants.":
            $ p_happiness += 5
            $ respect -= 5
            play sound "button_se.ogg" noloop volume 0.5

        "Give her a small amount of money.":
            $ p_happiness += 5
            $ influence -= 5
            play sound "button_se.ogg" noloop volume 0.5

        "Ignore her":
            $ p_happiness -= 5
            $ respect -= 5
            play sound "button_se.ogg" noloop volume 0.5
    return

label random3:
    scene bg flower day
    show mc fem neutral at right

    "The annual flower festival is approaching and they would like you to attend."
    play sound "button_se.ogg" noloop volume 0.5

    menu:
        "What shall I do?"

        "Send your subordinate to represent you.":
            $ influence += 5
            $ k_happiness -= 5
            play sound "button_se.ogg" noloop volume 0.5

        "Prioritize other matters":
            $ p_happiness += 5
            $ influence -= 5
            play sound "button_se.ogg" noloop volume 0.5

        "Attend.":
            $ k_happiness -= 5
            $ respect -= 5
            play sound "button_se.ogg" noloop volume 0.5
    return

label random4:
    scene bg market day
    show mc fem neutral at right

    "During a visit to the market, you stumble upon the entrance to a thriving black market."
    play sound "button_se.ogg" noloop volume 0.5

    menu:
        "What shall I do?"

        "Discreetly participate in the black market trade":
            $ influence += 5
            $ p_happiness -= 5
            play sound "button_se.ogg" noloop volume 0.5

        "Ignore it for a cut of the money.":
            $ influence += 5
            $ respect -= 5
            play sound "button_se.ogg" noloop volume 0.5

        "Use the black market to gain gossip on the other court members.":
            $ respect -= 5
            $ k_happiness -= 5
            play sound "button_se.ogg" noloop volume 0.5
    return

label random5:
    scene bg upperclass outdoor
    show mc fem neutral at right
    show beggar woman neutral at left

    "A surge of homelessness has gripped the nation, and a beggar approaches you asking for help."
    play sound "button_se.ogg" noloop volume 0.5

    menu:
        "What shall I do?"

        "Criminalize begging.":
            $ k_happiness += 5
            $ influence -= 5
            play sound "button_se.ogg" noloop volume 0.5

        "Fund a homeless shelter.":
            $ p_happiness += 5
            $ respect -= 5
            play sound "button_se.ogg" noloop volume 0.5

        "Ignore the beggar, and her issues.":
            $ respect += 5
            $ influence -= 5
            play sound "button_se.ogg" noloop volume 0.5
    return

label random6:
    scene bg dining day
    show mc fem neutral at right
    show king neutral at left

    "You are hosting a wonderful dinner party for the local nobility when the King approaches you:"
    play sound "button_se.ogg" noloop volume 0.5
    king "This party is great, but I do feel peckish."
    play sound "button_se.ogg" noloop volume 0.5

    menu:
        "What shall I do?"

        "Clap to get the servants' attention.":
            $ respect -= 5
            play sound "button_se.ogg" noloop volume 0.5

        "Grab the closest servant and reprimand them for not serving the King.":
            $ respect += 5
            $ k_happiness -= 5
            play sound "button_se.ogg" noloop volume 0.5

        "Get the King food yourself.":
            $ k_happiness += 5
            play sound "button_se.ogg" noloop volume 0.5
    return

label random7:
    scene bg theatre day
    show mc fem neutral at right
    show king neutral at left

    "You are attending the opening night of a play you funded when the King approaches you:"
    play sound "button_se.ogg" noloop volume 0.5
    king "I heard you were funding this play. Which is it again?."
    play sound "button_se.ogg" noloop volume 0.5

    menu:
        "What shall I do?"

        "Romeo and Juliet.":
            $ respect -= 5
            $ k_happiness += 5
            play sound "button_se.ogg" noloop volume 0.5

        "Hamlet.":
            $ p_happiness += 5
            $ k_happiness -= 5
            play sound "button_se.ogg" noloop volume 0.5

        "A Midsummer Night's Dream.":
            $ p_happiness += 5
            $ respect -= 5
            play sound "button_se.ogg" noloop volume 0.5
    return

label random8:
    scene bg bakery day
    show mc fem neutral at right
    show beggar woman neutral at left

    "While out buying croissants, you catch a beggar stealing bread."
    play sound "button_se.ogg" noloop volume 0.5

    menu:
        "What shall I do?"

        "Ignore the thief.":
            $ influence -= 5
            $ respect += 5
            play sound "button_se.ogg" noloop volume 0.5

        "Scold the woman.":
            $ p_happiness -= 5
            $ respect += 5
            play sound "button_se.ogg" noloop volume 0.5

        "Buy the bread for her.":
            $ p_happiness += 5
            $ influence -= 5
            play sound "button_se.ogg" noloop volume 0.5
    return

label court1:
    scene bg court day
    show mc fem neutral at right
    show king neutral at left
    king "Today's issue: The shifterfolk are asking for the right to change their appearance how they'd like."
    show king neutral at center
    show court member female at left

    c_f "Well, I don’t think them changing their appearance is much of a threat to anyone, right?"

    hide court member female
    show knight head neutral at left
    knight "What if they committed a crime, and then just changed appearances so they could never be caught?"
    hide knight head neutral
    show court mage at left
    c_w "How many do you think would really do that, though? They just want to be happy."
    hide court mage
    show court member male at left
    c_m "I think giving them the right to change appearances gives them too many unfair advantages of us normal folk."
    
    menu:
        "What shall we do?"

        "Give them the right to look how they like.":
            $ p_happiness += 5
            $ influence -= 5
            play sound "button_se.ogg" noloop volume 0.5

        "Don't give them the right to look how they like.":
            $ p_happiness -= 5
            $ influence += 5
            play sound "button_se.ogg" noloop volume 0.5
    return

label court2:
    scene bg court day
    show mc fem neutral at right
    show king neutral at left
    king "Today's issue: Recently, we’ve gotten reports that many people have been selling demihumans as if they were animals. The demihumans are asking for a law to be put into place banning the selling of demihumans, while the humans are comparing it to the cattle industry or pets."
    show king neutral at center
    show court member male at left

    c_m "They are pets though. How many dog demis have you seen get distracted by some inane thing before?"
    hide court member male
    show court member female at left
    c_f "They are still human and of the right mind. Buying and selling them is slavery, and our nation banned slavery many years ago."
    hide court member female
    show knight head neutral at left
    knight "They aren’t human though, by law they are considered non-human, therefore selling them is akin to selling a calf."
    hide knight head neutral
    show court mage at left
    c_w "Well, maybe it's time we looked at our slavery law again."
    
    menu:
        "What shall we do?"

        "Assert that demihumans are more animal than human.":
            $ p_happiness -= 5
            $ influence -= 5
            play sound "button_se.ogg" noloop volume 0.5

        "Agree to look at, and adjust the slavery law to include all sentient, humanoid creatures." if influence > 30:
            $ p_happiness += 5
            $ k_happiness -= 5
            play sound "button_se.ogg" noloop volume 0.5
    return

label court3:
    scene bg court day
    show mc fem neutral at right
    show king neutral at left
    king "Today's issue: We’ve recently spotted battleships of an enemy nation nearing our borders. The people are afraid that this could become an act of war."
    show king neutral at center
    show court member female at left

    c_f "Isn’t that nation at war with the other two of the four nations, and  even themselves?"
    hide court member female
    show knight head neutral at left
    knight "Yes, I heard they’ve recently tried to overthrow their King. A lot of blood spilled that day. I don’t think they were purposely coming after us. Probably just fighting their losing battles against the other two."
    hide knight head neutral
    show court member male at left
    c_m "Shouldn’t we still send a messenger to the border wall to pass along our doubts on their motives?"
    hide court member male
    show knight head neutral at left
    knight "That might be seen as an act of war on our part, though."
    
    menu:
        "What shall we do?"

        "Draft a message for the nation's king.":
            $ p_happiness -= 5
            $ k_happiness -= 5
            play sound "button_se.ogg" noloop volume 0.5

        "Ignore this until they cross borders or attack.":
            $ p_happiness -= 5
            $ influence += 5
            play sound "button_se.ogg" noloop volume 0.5
    return

label court4:
    scene bg court day
    show mc fem neutral at right
    show king neutral at left
    king "Today's issue: The church is asking us to ban sinners from entering a church."
    show king neutral at center
    show court member female at left

    c_f "What does the church consider sinners?"
    hide court member female
    show court member male at left
    c_m "We know they think demihumans are sinners. How long until even us humans are considered sinners?"
    hide court member male
    show court mage at left
    c_w "Isn’t the church just asking for permission to ban those that sin from their properties? That doesn’t mean they are going to ban entire populations."
    hide court mage
    show court member female at left
    c_f "Doesn’t mean they won’t, either."
    
    menu:
        "What shall we do?"

        "Agree to give the church the power to ban sinners.":
            $ p_happiness -= 5
            $ k_happiness += 5
            play sound "button_se.ogg" noloop volume 0.5

        "Agree to ban sinners, but the court gets to decide what constitutes a sinner.":
            $ k_happiness -= 5
            $ influence += 5
            play sound "button_se.ogg" noloop volume 0.5

        "Don’t ban anyone from churches, everyone has a right to religion.":
            $ p_happiness += 5
            $ influence -= 5
            play sound "button_se.ogg" noloop volume 0.5
    return

label court5:
    scene bg court day
    show mc fem neutral at right
    show king neutral at left
    king "Today's issue: A pandemic has been sweeping the nation."
    show king neutral at center
    show knight head neutral at left

    knight "We should just tough it out! Not getting sick isn't that hard."
    hide knight head neutral
    show court member female at left
    c_f "What!? We need to keep everyone separated in their houses."
    hide court member female
    show court member male at left
    c_m "That's too extreme! I need to travel all the time for work."
    hide court member male
    show court mage at left
    c_w "We should just mandate self care, much safer."
    
    menu:
        "What shall we do?"

        "Agree to do nothing.":
            $ p_happiness -= 5
            $ k_happiness += 5
            play sound "button_se.ogg" noloop volume 0.5

        "Agree to keep everyone seperate.":
            $ p_happiness -= 5
            $ influence += 5
            play sound "button_se.ogg" noloop volume 0.5

        "Agree to mandate self care.":
            $ p_happiness += 5
            $ k_happiness -= 5
            play sound "button_se.ogg" noloop volume 0.5
    return

label court6:
    scene bg court day
    show mc fem neutral at right
    show king neutral at left
    king "Today's issue: We recently had a hero find a strong, powerful artifact."
    show king neutral at center
    show court member female at left

    c_f "Its too powerful and should be destroyed immediately!"
    hide court member female
    show knight head neutral at left
    c_f "No, this is too good of an opportunity, we should harness its power to bulk up our defenses."
    hide knight head neutral
    show court mage at left
    c_w "But that could risk a possible arms race with the neighboring nations. We should place the artifact in neutral custody, resulting in no misuse of the artifact."
    hide court mage
    show court member male at left
    c_m "But that risks it falling into someone else's hand and them misusing it."
    
    menu:
        "What shall we do?"

        "Agree to destroy the artifact.":
            $ influence -= 5
            $ p_happiness += 5
            play sound "button_se.ogg" noloop volume 0.5

        "Agree to harness its power.":
            $ p_happiness -= 5
            $ k_happiness += 5
            play sound "button_se.ogg" noloop volume 0.5

        "Agree to place it in neutral custody.":
            $ respect += 5
            $ influence -= 5
            play sound "button_se.ogg" noloop volume 0.5
    return

label court7:
    scene bg court day
    show mc fem neutral at right
    show king neutral at left
    king "Today's issue: The neighboring kingdom has put increased taxes on our goods."
    show king neutral at center
    show court member male at left

    c_m "Well if they are taxing our stuff, lets tax them back."
    hide court member male
    show knight head neutral at left
    knight "What's with that passive aggressive nonsense? Lets just fight them."
    hide knight head neutral
    show court mage at left
    c_w "That's way too reckless. We should just bribe them to lessen the taxes."
    hide court mage
    show court member male at left
    c_m "That shows no power at all!"
    
    menu:
        "What shall we do?"

        "Agree to impose taxes on their goods.":
            $ influence += 5
            $ k_happiness -= 5
            play sound "button_se.ogg" noloop volume 0.5

        "Agree to rally for war.":
            $ influence -= 5
            $ respect += 5
            play sound "button_se.ogg" noloop volume 0.5

        "Agree to bride the nation to lessen taxes.":
            $ k_happiness += 5
            $ respect -= 5
            play sound "button_se.ogg" noloop volume 0.5
    return


label callEncounter:
    $ currentencounter = getNumber()

    if currentencounter == 0:
        call shifterfolk1
    elif currentencounter == 1:
        call shifterfolk2
    elif currentencounter == 2:
        call shifterfolk3
    elif currentencounter == 3:
        call shifterfolk4
    elif currentencounter == 4:
        call demi1
    elif currentencounter == 5:
        call demi2
    elif currentencounter == 6:
        call demi3
    elif currentencounter == 7:
        call sub1
    elif currentencounter == 8:
        call sub2
    elif currentencounter == 9:
        call prince1
    elif currentencounter == 10:
        call sub3
    elif currentencounter == 11:
        call sub4
    elif currentencounter == 12:
        call sub5
    elif currentencounter == 13:
        call random1
    elif currentencounter == 14:
        call random2
    elif currentencounter == 15:
        call random3
    elif currentencounter == 16:
        call random4
    elif currentencounter == 17:
        call random5
    elif currentencounter == 18:
        call random6
    elif currentencounter == 19:
        call random7
    elif currentencounter == 20:
        call random8
    elif currentencounter == 21:
        call court1
    elif currentencounter == 22:
        call court2
    elif currentencounter == 23:
        call court3
    elif currentencounter == 24:
        call court4
    elif currentencounter == 25:
        call court5
    elif currentencounter == 26:
        call court6
    elif currentencounter == 27:
        call court7

    return

label pHighDeath:

    scene bg black
    show mc fem neutral at center

    "The people rioted for you to become king, the king didn't like that."
    play sound "button_se.ogg" noloop volume 0.5

    return

label pLowDeath:

    scene bg black
    show mc fem neutral at center

    "The people grew distastful of royalty and usurped the royal family, you were caught in the crossfire."
    play sound "button_se.ogg" noloop volume 0.5

    return

label kHighDeath:

    scene bg black
    show mc fem neutral at center

    "The court grew jealous of your favor with the king, they got you in the night."
    play sound "button_se.ogg" noloop volume 0.5

    return

label kLowDeath:

    scene bg black
    show mc fem neutral at center

    "The king thought you had no respect for him, and beheaded you immediately."
    play sound "button_se.ogg" noloop volume 0.5

    return
