import random
class Art:
    
    introArt = """
════════════════════════════════════════════════════════════════════════════════════
       ◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘
       ◘◘     ◘◘◘     ◘◘◘◘◘◘  ◘◘◘◘◘    ◘◘◘◘      ◘◘      ◘◘◘◘◘   ◘◘◘◘      ◘◘        
       ◘◘  ◘◘  ◘◘  ◘◘  ◘◘◘◘    ◘◘◘  ◘◘◘  ◘◘◘◘  ◘◘◘◘◘◘  ◘◘◘◘◘  ◘◘◘  ◘◘  ◘◘◘◘◘◘
       ◘◘     ◘◘◘     ◘◘◘◘  ◘◘  ◘◘  ◘◘◘◘◘◘◘◘◘  ◘◘◘◘◘◘  ◘◘◘◘◘  ◘◘◘◘◘◘◘     ◘◘◘
       ◘◘  ◘◘◘◘◘◘  ◘◘  ◘◘◘      ◘◘  ◘◘◘  ◘◘◘◘  ◘◘◘◘◘◘  ◘◘◘◘◘  ◘◘◘  ◘◘  ◘◘◘◘◘◘
       ◘◘  ◘◘◘◘◘◘  ◘◘◘  ◘◘  ◘◘  ◘◘◘    ◘◘◘◘◘◘  ◘◘◘◘      ◘◘◘◘    ◘◘◘◘      ◘◘
       ◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘
════════════════════════════════════════════════════════════════════════════════════
    WELCOME to interactive operator prep. 

    We do hope that you enjoy this practice and that it helps you. This prcatice
    contains both multiple choice and short/fill in the blank answers. Everything
    must be entered exactly correct to be counted. 

    Good Luck!

    Loading your quiz...
"""

    asciiart = [
    ("""
    ╔════════════════════════════════════════════════╗
    ║ Would you like to load a quiz? (<enter> or y:) ║
    ╚════════════════════════════════════════════════╝
        \          __====-_  _-====__
         \  _--^^^#####//      \\\####^^^--_
           _-^########// (    ) \\\########^-_ 
          -##########//  |\^^/|  \\\##########-
       _/###########//   (0::0)   \\\###########\_
      /############((     \\\//     ))############\\ 
    //##############\\\    (oo)    //###############\\\       
   //########### ####\\\  /▼\/▼\  //#################\\\ 
  ((##### #####'  '###\\\/▼▼▼▼▼▼\//##### ###### #######))
   \##''##  ###'   '####(▼▼▼▼▼▼▼▼)####'   ####'  '##''#/ 
    )' '#'' '#    '#''##(▼▼▼/\▼▼▼)##      '#'   '#    (
                      \_(|▼|  |▼|)_/                     
                       /▼|▼|  |▼|▼\                  
                     <(▼▼|▼|  |▼|▼▼)>   
                    <▼▼\▼|▼|  |▼|▼\▼▼>  
                    ^^^^ ^^^  ^^^ ^^^^
                                                            
    """),
    ("""    
╔════════════════════════════════════════════════╗
║ Would you like to load a quiz? (<enter> or y:) ║
╚════════════════════════════════════════════════╝
      \ 
       \ 
                                      .::!!!!!!!:.
    .!!!!!:.                        .:!!!!!!!!!!!!
    ~~~~!!!!!!.                 .:!!!!!!!!!UWWW$$$
        :$$NWX!!:           .:!!!!!!XUWW$$$$$$$$$P
        $$$$$##WX!:      .<!!!!UW$$$$"  $$$$$$$$#
        $$$$$  $$$UX   :!!UW$$$$$$$$$   4$$$$$*
        ^$$$B  $$$$\     $$$$$$$$$$$$   d$$R"
          "*$bd$$$$      '*$$$$$$$$$$$o+#"
               \"\"\"\"          \"\"\"\"\"\"\"
    """),

    ("""
╔════════════════════════════════════════════════╗
║ Would you like to load a quiz? (<enter> or y:) ║
╚════════════════════════════════════════════════╝  
  \            .    .     .
   \      .  . .     `  ,
    \    .; .  : .' :  :  : .
     \   i..`: i` i.i.,i  i .
      \   `,--.|i |i|ii|ii|i:
           UooU\.'@@@@@@`.||'
           \__/(@@@@@@@@@@)'
                (@@@@@@@@)
                `YY~~~~YY'
                 ||    ||
    """),
    ("""
╔═════════════════════════════════════════════════════════════╗
║ Would you like to load a quiz, or be eaten? (<enter> or y:) ║
╚═════════════════════════════════════════════════════════════╝  
                       \                    ^    /^
                        \                  / \  // \ 
                         \   |\___/|      /   \//  .\ 
                          \  /O  O  \__  /    //  | \ \           *----*
                            /     /  \/_/    //   |  \  \          \   |
                            @___@`    \/_   //    |   \   \         \/\ \ 
                           0/0/|       \/_ //     |    \    \         \  \ 
                       0/0/0/0/|        \///      |     \     \       |  |
                    0/0/0/0/0/_|_ /   (  //       |      \     _\     |  /
                 0/0/0/0/0/0/`/,_ _ _/  ) ; -.    |    _ _\.-~       /   /
                             ,-}        _      *-.|.-~-.           .~    ~
            \     \__/        `/\      /                 ~-. _ .-~      /
             \____(oo)           *.   }            {                   /
             (    (--)          .----~-.\        \-`                 .~
             //__\\  \__ Ack!   ///.----..<        \             _ -~
            //    \\               ///-._ _ _ _ _ _ _{^ - - - - ~
    """),
    ("""
╔════════════════════════════════════════════════╗
║ Would you like to load a quiz? (<enter> or y:) ║
╚════════════════════════════════════════════════╝ 
          \ 
           \ 
            \          __---__
                    _-       /--______
               __--( /     \ )XXXXXXXXXXX\\v.
             .-XXX(   O   O  )XXXXXXXXXXXXXXX-
            /XXX(       U     )        XXXXXXX\ 
          /XXXXX(              )--_  XXXXXXXXXXX\ 
         /XXXXX/ (      O     )   XXXXXX   \XXXXX\ 
         XXXXX/   /            XXXXXX   \__ \XXXXX
         XXXXXX__/          XXXXXX         \__---->
 ---___  XXX__/          XXXXXX      \__         /
   \-  --__/   ___/\  XXXXXX            /  ___--/=
    \-\    ___/    XXXXXX              '--- XXXXXX
       \-\/XXX\ XXXXXX                      /XXXXX
         \XXXXXXXXX   \                    /XXXXX/
          \XXXXXX      >                 _/XXXXX/
            \XXXXX--__/              __-- XXXX/
             -XXXXXXXX---------------  XXXXXX-
                \XXXXXXXXXXXXXXXXXXXXXXXXXX/
                  ""VXXXXXXXXXXXXXXXXXXV""

    """),
    ("""
╔════════════════════════════════════════════════╗
║ Would you like to load a quiz? (<enter> or y:) ║
╚════════════════════════════════════════════════╝     
    \     ____________
     \    |__________|
         /           /\ 
        /           /  \ 
       /___________/___/|
       |          |     |
       |  ==\ /== |     |
       |   O   O  | \ \ |
       |     <    |  \ \|
      /|          |   \ \ 
     / |  \_____/ |   / /
    / /|          |  / /|
   /||\|          | /||\/
       -------------|
           | |    | |
          <__/    \__>
    """),
    ("""
╔════════════════════════════════════════════════╗
║ Would you like to load a quiz? (<enter> or y:) ║
╚════════════════════════════════════════════════╝     
   \                             .       .
    \                           / `.   .' "
     \                  .---.  <    > <    >  .---.
      \                 |    \  \ - ~ ~ - /  /    |
           ┌─────┐          ..-~             ~-..-~
           │     │   \~~~\.'                    `./~~~/
          ─┼─────┼─   \__/                        \__/
         .'  O   '\     /               /       \  "
        (_____,    `._.'               |         }  \/~~~/
         `----.          /       }     |        /    \__/
               `-.      |       /      |       /      `. ,~~|
                   ~-.__|      /_ - ~ ^|      /- _      `..-'
                        |     /        |     /     ~-.     `-. _  _  _
                        |_____|        |_____|         ~ - . _ _ _ _ _>

    """),
    
    ("""
╔════════════════════════════════════════════════╗
║ Would you like to load a quiz? (<enter> or y:) ║
╚════════════════════════════════════════════════╝ 
    \                                  ___-------___
     \                             _-~~             ~~-_
      \                         _-~                    /~-_
             /^\__/^\         /~  \                   /    \ 
           /|  O|| O|        /      \_______________/        \ 
          | |___||__|      /       /                \          \ 
          |          \    /      /                    \          \ 
          |   (_______) /______/                        \_________ \ 
          |         / /         \                      /            \ 
           \         \^\\         \                  /               \     /
             \         ||           \______________/      _-_       //\__//
               \       ||------_-~~-_ ------------- \ --/~   ~\    || __/
                 ~-----||====/~     |==================|       |/~~~~~
                  (_(__/  ./     /                    \_\      \.
                         (_(___/                         \_____)_)
    """),
    ("""
╔════════════════════════════════════════════════╗
║ Would you like to load a quiz? (<enter> or y:) ║
╚════════════════════════════════════════════════╝ 
   \ 
    \ 
               |    .
           .   |L  /|
       _ . |\ _| \--+._/| .
      / ||\| Y J  )   / |/| ./
     J  |)'( |        ` F`.'/
   -<|  F         __     .-<
     | /       .-'. `.  /-. L___
     J \      <    \  | | O\|.-'
   _J \  .-    \/ O | | \  |F
  '-F  -<_.     \   .-'  `-' L__
 __J  _   _.     >-'  )._.   |-'
 `-|.'   /_.           \_|   F
   /.-   .                _.<
  /'    /.'             .'  `\ 
   /L  /'   |/      _.-'-\ 
  /'J       ___.---'\|
    |\  .--' V  | `. `
    |/`. `-.     `._)
       / .-.\ 
       \ (  `\ 
        `.\ 

    """)
    ]
    
    def ranArt():
        random.shuffle(Art.asciiart)
        return print(Art.asciiart[0])
    #print(Art.asciiart[0])

    goodbye_quotes = [
        ("""
There's a sad sort of clanging from the clock in the hall
And the bells in the steeple too
And up in the nursery an absurd little bird
Is popping out to say 'cuckoo'
Cuckoo, cuckoo
Regretfully they tell us Cuckoo, cuckoo
But firmly they compel us Cuckoo, cuckoo

To say goodbye...
Cuckoo!
...to you
So long, farewell, auf Wiedersehen, good night
I hate to go and leave this pretty sight
So long, farewell, auf Wiedersehen, adieu
Adieu, adieu, to yieu and yieu and yieu
So long, farewell, au revoir, auf Wiedersehen

I'd like to stay and taste my first champagne
So long, farewell, auf Wiedersehen, goodbye
I leave and heave a sigh and say goodbye -- Goodbye!
I'm glad to go, I cannot tell a lie

I flit, I float, I fleetly flee, I fly
The sun has gone to bed and so must I
So long, farewell, auf Wiedersehen, goodbye
Goodbye, goodbye, goodbye
Goodbye!

        """),
        ("In the event I don't make it back, I want you to know you've\nbeen a real friend to me R2. My best one, in fact."),
        ("I can't lie to you about your chances...but, you have my sympathies"),
        ("Clever girl..."),
        ("No, not the bees! NOT THE BEES! AAAAAAAAAAAAAGH! THEY'RE IN MY EYES! MY EYES! AAAAAAAAAAAAAAGH!"),
        ("Right! Silly little bleeder! One rabbit stew coming right up!"),
        ("You can't win Darth. If you strike me down, I shall become more\npowerful than you can possibly imagine."),
        ("Ah, you cursed brat! Look what you've done! I'm melting! Melting!\nOhhhhh... What a world, what a world! Who ever thought a little\ngirl like you could destroy my beautiful wickedness?!\nAh, I'm going! Ahhhh!"),
        ("I'll see you in another life. When we are both cats."),
        ("I'll be back"),
        ("""
Maybe this will help a little, or maybe it won't. I don't know!

╔═══╤═══╗
║ 0 │ A ║
╟───┼───╢
║ 1 │ B ║
╟───┼───╢
║ 2 │ C ║
╟───┼───╢
║ 3 │ D ║
╟───┼───╢
║ 4 │ E ║
╟───┼───╢
║ 5 │ F ║
╟───┼───╢
║ 6 │   ║
╟───┼───╢
║ 7 │   ║
╟───┼───╢
║ 8 │   ║
╟───┼───╢
║ 9 │   ║
╔═╩═╦═╧═╦═╩═╗
║256║ 16║ 1 ║
╚═══╩═══╩═══╝
╔═════╦════╦═══╦═══╗
║ 512 ║ 64 ║ 8 ║ 1 ║
╚═════╩════╩═══╩═══╝
╔═════╦═════╦═════╦═════╦═════╦═════╦═════╦═════╗
║ 128 ║ 192 ║ 224 ║ 240 ║ 248 ║ 252 ║ 254 ║ 255 ║
╟─────╫─────╫─────╫─────╫─────╫─────╫─────╫─────╢
║ 128 ║  64 ║  32 ║  16 ║  8  ║  4  ║  2  ║  1  ║
╚═════╩═════╩═════╩═════╩═════╩═════╩═════╩═════╝

        """)

    ]

    goodbye_art2 = """
                    \/,                          /
         \),          \`-._                     /
         /\            \   `-.                 /
        /  \            | .(                  /
       /,.  \           ; ( `                /
          ), \         / ;``                /
         /_   \     __/_(_                 /
           '. ,`..-'      `-.    \  /     /
             )__ `.          `-. .\/.    /
            /   `. `            `-._______m          _,
  ,.----.-.'                , ____________/  _,-_,'"`/__,-.
 /  =--  ;                  `.`._    V V V        -=-'"#==._ 
|. \____/|      UuUu_,......__   `-.__A_A_    -. ._ ,--._ ",`` `-
|' )     :    uUuUu,'         `'--...____/       `" `".   ` 
 \/_     \    UuUu: 
 (_3      \    UuUu`-._
           `._   uUuUu `-.
              `-._  uUu   `._
                  ``-._      `.
                       `-._    `.
                           `.    \ 
                             )   ;
                            /   /
             `.        |\ ,'   /  
               ",_A_/\-| `   ,'
                 `--..,_|_,-'\ 
                        |     \ 
                        |      \__
                        |__
"""
def ranbg():
  A1 = Art()
  random.shuffle(A1.goodbye_quotes)
  return A1.goodbye_quotes[0]

def boxThis(quote, tabs):
  length = 0
  l1 = quote.splitlines()
  for line in l1:
    if len(line) > length:
      length = len(line)

  box = str("\t" * tabs) + "╔" + str("═" * (length + 2)) + "╗"
  for line in l1:
    if len(line) < length:
      spacesNeed = length - len(line)
      if spacesNeed % 2 == 1:
        box += "\n" + str("\t" * tabs) + "║" + str(" " * (int(spacesNeed / 2) + 1))
        box += line
        box += str(" " * (int(spacesNeed / 2) + 2)) + "║"
      else:
        box += "\n" + str("\t" * tabs) + "║" + str(" " * (int(spacesNeed / 2) + 1))
        box += line
        box += str(" " * (int(spacesNeed / 2) + 1)) + "║"

    else:
      box += "\n" + str("\t" * tabs) + "║ " + line + " ║"

  #botoom
  box += "\n" + str("\t" * tabs) + "╚" + str("═" * (length + 2)) + "╝"

  return box


def finishIt():
  A1 = Art()
  output = str("\n" * 3) 
  output += boxThis(ranbg(), 4) + "\n" + str(A1.goodbye_art2)
  return output

finishIt()