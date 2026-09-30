from author import make
make(18,'SQUARE','The rejected worker used a T-shaped torso and rectangular conveyor divisions. Restore rounded shoulders, a separate outlined package and a slim rounded conveyor beneath them.', '''
path('head',(14,6),[('A',(14,14),4,4,True),('A',(14,6),4,4,True)],True)
path('torso',(6,25),[('A',(14,22),8,3,True),('A',(22,25),8,3,True)])
poly('package',(32,26),(32,14),(42,14),(42,26),closed=True)
path('belt',(10,34),[('L',(38,34)),('A',(38,42),4,4,True),('L',(10,42)),('A',(10,34),4,4,True)],True)
''','human_ref/user.svg circular head and curved shoulders; head14 to shoulders22 gives4 ink gap. Roller circles and package tape omitted to retain the conveyor opening.')
