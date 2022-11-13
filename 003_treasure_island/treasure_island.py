# a little text based story game

from rich.prompt import Prompt
from random import randint

img_forest : str = """               ,@@@@@@@,
       ,,,.   ,@@@@@@/@@,  .oo8888o.
    ,&%%&%&&%,@@@@@/@@@@@@,8888\\88/8o
   ,%&\\%&&%&&%,@@@\\@@@/@@@88\\88888/88'
   %&&%&%&/%&&%@@\\@@/ /@@@88888\\88888'
   %&&%/ %&%%&&@@\\ V /@@' `88\\8 `/88'
   `&%\\ ` /%&'    |.|        \\ '|8'
       |o|        | |         | |
       |.|        | |         | |
jgs \\\\/ ._\\//_/__/  ,\\_//__\\\\/.  \\_//__/_"""

img_house : str = """____
                  _           |---||            _
                  ||__________|SSt||___________||
                 /_ _ _ _ _ _ |:._|'_ _ _ _ _ _ _\\`.
                /_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\\:`.
               /_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\\::`.
              /:.___________________________________\\:::`-._
          _.-'_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _`::::::`-.._
      _.-' _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ `:::::::::`-._
    ,'_:._________________________________________________`:_.::::-';`
     `.'/ || |:::::`.'/::::::::`.'/::::::::`.'/::::::|.`.'/.|     :|
      ||  || |::::::||::::::::::||::::::::::||:::::::|..||..|     ||
      ||  || |  __  || ::  ___  || ::  __   || ::    |..||;||     ||
      ||  || | |::| || :: |:::| || :: |::|  || ::    |.|||:||_____||__
      ||  || | |::| || :: |:::| || :: |::|  || ::    |.|||:||_|_|_||,(
      ||_.|| | |::| || :: |:::| || :: |::|  || ::    |.'||..|    _||,|
   .-'::_.:'.:-.--.-::--.-:.--:-::--.--.--.-::--.--.-:.-::,'.--.'_|| |
    );||_|__||_|__|_||__|_||::|_||__|__|__|_||__|__|_|;-'|__|_(,' || '-
    ||||  || |. . . ||. . . . . ||. . . . . ||. . . .|::||;''||   ||:'
    ||||.;  _|._._._||._._._._._||._._._._._||._._._.|:'||,, ||,,
    '''''           ''-         ''-         ''-         '''  '''"""

img_island : str = """                             .       .
                                                    \\     /
                                                 ._  '   '  _.
                                                   '  o@o  '
                                                     o@@@o
                                                 .-'  o@o  '-.
                                                     .   .
                                                    /     \\
                                                   .       .

                             'Xx  xX*,
                          ,*xXXx_xXx
                            _xXXXXXxx*,
                          ,*XXx@x@Xx
                            X @|@@ `x
                            '  ||    '
                               ||
                               ||
                               ||
                               ||
                            /ssssssss.
                      /sssssssSSSSssssssssss.
        /\\         /sssssSSSSSSSSSSSSSSSssssssssssss.              Dani
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~"""

img_skull : str = """
      _.--,_
   .-'      '-.   [nabis]
  /            \\
 '          _.  '
 \\      "" /  ~(
  '=,,_ =\\__ `  &
        "  "'; \\\\"""

img_chest : str = """
            __________
        / \\____;;___\\
       | /         /
       `. ())oo() .
        |\\(%()*^^()^\\
       %| |-%-------|
      % \\ | %  ))   |
      %  \\|%________|
ejm97  %%%%"""

img_explosion : str = """____
                     __,-~~/~    `---.
                   _/_,---(      ,    )
               __ /        <    /   )  \\___
- ------===;;;'====------------------===;;;===----- -  -
                  \\/  ~"~"~"~"~"~\\~"~)~"/
                  (_ (   \\  (     >    \\)
                   \\_( _ <         >_>'
                      ~ `-i' ::>|--"
                          I;|.|.|
                         <|i::|i|`.
                        (` ^'"`-' ")"""
                        

print("Welcome to the treasure_island text base story game !!!!!!")
print(img_forest)
print("""You have found yourself in a deep forest. You are standing on an almost unrecognizable path and
in front of you there is a crossroads. You have two options, you can either go left, into a pleasantly looking
part of the forest, or you can choose the path on you right, which seems to guide you to a dark and scary
area.""")
if Prompt.ask("Which way will you go?", choices=["left", "right"]) == "left":
    print("You have chosen to go left, you are walking the path and the sun warms your back.")
    input("Continue [Enter]")
    print("""As you walk and walk you forget, that you are in a hostile area and start enjoying yourself too much.
So much that you do not pay attention to the path you are walking and steps into a trap that triggers a mechanism,
which throws a log with spikes directly at your body, as you don't have time to dodge it, you get completely penetrated
by the spikes and as you are slowly loosing blood you think, that you should have probably gone right at the crossroads.""")
    print(img_skull)
    input("Game over [Enter]")
    exit()

print("""You have chosen to follow the path on your right and entered a dark and deep forest. You are getting scared
And each sound you hear sends an ice-cold feeling through your spine.""")
input("Continue [Enter]")
print("""You feel like if you were walking for hours in the forest, yet you have walked only for a few minutes. When you
finally see light beams several metres in front of you, you feel relieved. After a minute you reach the edge of the forest
and find yourself on lake shore. In the center of the lake you see an island and it seems that there is a house as well
You desperately want to get to the island and look inside the house. It seems you have two options, you can either swim
through the lake and get to the island in no time or you can walk around the shore and look for a different way to get there,
though this could take some time.""")
print(img_island)
if Prompt.ask("What will you decide?", choices=["swim", "walk"]) == "swim":
    print("""You have decided to swim to the island, as you enter the water you have a weird feeling, but you strengthen yourself
and continue swimming. It seems easy, after a few seconds you are already halfway there, yet the weird feeling intensifies and now
your whole body's skin seems to be in pain, you quickly look at your left arm and hand and you see that it is disintegrating!!
you quickly look at the other hand and you see the same. Your whole body is disintegrating, and it seems that the longer you are in
the lake the faster it goes. You decide to quickly swim to the island, yet after a few seconds as you have almost reached the island shore
you can not continue and in pain you think, whether you shouldn't have looked for a different way to the island""")
    print(img_skull)
    input("Game over [Enter]")
    exit()
print("""You have chosen to walk around the shore, after few minutes you see that behind the island might be a bridge, so you continue
walking to get there. After a quater of hour you get to the bridge and cross it. Now you are on the island and you stand before a house.""")
print(img_house)
input("Continue [Enter]")
print("""You enter the house and find yourself in front of a table with a computer. On the table you see an interestingly
looking vr-headset. A type you have never seen before. There is also an inscription 'Courtesy of Palmer Luckey', Then you look on the wall behind
the table and see a infographic with rules. The rules say: You have reached the end of your path.
Now in order to get the treasure you must win in a vr game. You have to wear the headset and play the game.
But play your best as your destiny might depend on it!""")
input("Continue [Enter]")
print("""You have decided to give the game a try. You calmly take the headset and put it on your head. An initialization sequence takes place
And you see a text saying that with this headset you will enter a new level of immersion and that it raises the stakes, as you reach the end of the text
you read 'If you die in game, you die in real life, .... I planted three explosive charges in the headset, these are now at your forehead.
If your character die, these will explode .... Your Palmer Luckey'. You get scared and try to take off the headset but you can't!! It sits
firmly on your head and is secured by several rubber bands around your head, which somehow appeared there without you noticing. As you try to lift it off
A new text appears before your eyes 'You can't take off the headset!! I have taken care of that. But if you will continue trying, the headset will
blow immediately Your Palmer L.'. You stop trying to take it off and you strengthen your thougths. You say to yourself 'I will win, I know it'.
Even though ye are really scared and already feel the stakes.""")
input("Continue [Enter]")
print("""After few seconds the game starts, and you are extremely scared. You are afeared of making any mistake. You seem to be in a large room
with many obstacles. Suddenly sou see an enemy in front of you but it is too fast and you don't manage to fire in time. It is hidden behind
a box that is several metres in front of you. You have two options, you can either prepare yourself to shoot on left side (he showed there before) or on
right side of the box.""")
side : str = Prompt.ask("What will you do? Prepare at left or at right side of the box?", choices=["left", "right"])
if randint(0, 1):
    print(f"You have chosen to be ready at the {side} side of the box and the enemy really shows up there and you immediately shoot him.")
    print("""You continue fighting with it for many more minutes, but thanks to the initial shot the enemy is weakend and after a while you win the game.
At the same time you feel like if the bands around your head weaken in strength and you try to take off the headset. You easily take it off and
put it on the table, at the same time you hear a click on your right. You look there and you see that the wall opened and there is a treasure.""")
    print(img_chest)
    print("You have won!!")
    exit()
else:
    print(f"""You prepare yourself at the {side} side of the box, but the enemy doesn't show there. Instead it shows on the other side
and shoots you. You start to fear even more and after the shot you feel weak and desoriented. You continue fighting for many more minutes,
but you are getting more and more shots, and are weaker and weaker. Then you get two direct hits to your chest and you loose all your strength,
you fall on your knees and your weapon slides from your hands, after a few seconds you fall on the ground completely. Then you see less and less and
after a moment a Game over screen shows in front of you. It flashes red and the charges on your forehead explode.""")
    print(img_explosion)
    input("Game over [Enter]")
    exit()