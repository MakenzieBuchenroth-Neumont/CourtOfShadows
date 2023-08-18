# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("Lady Elisa")
define court = Character("Male Court Member")


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

    define l_happiness = 100
    define p_happiness = 100
    define influence = 0
    define respect = 0

    "{color=#507D7C}Leader's Happiness{/color}, {color=#6D9F31}People's Happiness{/color}, {color=#9F5E31}Influence{/color}, and {color=#9F3197}Respect{/color}."

    "Your decisions will impact your stats positively or negatively. Be sure to keep an eye on them; if either of the happiness' get too low, you will lose your spot on the King's court."

    scene bg court day

    show mc fem neutral at right

    show court member male at left

    court "The shifterfolk are upset. They think they are being opressed. What shall we do?"

    menu:
        "What shall we do?"

        "We will show them opression."

    # This ends the game.

    return
