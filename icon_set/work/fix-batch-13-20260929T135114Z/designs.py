from author import *
D.clear()
add('hand-expansion-touch-gesture','HRECT_L','Rejected hand is a stepped block with no rounded finger or thumb; restore a rounded raised finger and curved palm beneath three direction arrows.','pointer and hand: rounded finger and thumb; arrow-up: shared shaft', '''
path('hand',(18,40),[('L',(14,34)),('C',(20,32),(11,29),(16,29)),('L',(22,34)),('L',(22,28)),('A',(30,28),4,4,True),('L',(30,34)),('L',(32,34)),('L',(32,40)),('L',(18,40))],True)
poly('up',(20,12),(24,8),(28,12));line('up-shaft',(24,8),(24,16));join('up','up-shaft')
poly('left',(8,18),(4,22),(8,26));poly('right',(40,18),(44,22),(40,26))
''','Side arrows retain open heads; short shafts omitted for clearance.')
add('hand-swiping-up-gesture','HRECT_L','Angular polygon hand and faceted contact arc obscure touch gesture. Replace with rounded index, thumb and a smooth contact arc.','hand and pointer: continuous rounded outline', '''
path('hand',(4,38),[('L',(4,30)),('L',(16,23)),('C',(19,29),(24,20),(26,25)),('L',(28,29)),('A',(28,37),4,4,True),('L',(20,37)),('L',(18,40)),('L',(4,38))],True)
path('contact',(36,20),[('A',(36,40),8,10,True)])
poly('arrow',(20,12),(24,8),(28,12));line('shaft',(24,8),(24,14));join('shaft','arrow')
''')
add('happy-chat-bubbles','SQUARE','Foreground reply is too narrow and tails collapse into nubs; restore a square reply and legible diagonal tails.','messages-square: overlapping rounded message contours', '''
path('back',(32,20),[('L',(32,10)),('A',(28,6),4,4,False),('L',(10,6)),('A',(6,10),4,4,False),('L',(6,31)),('A',(10,35),4,4,False),('L',(14,35)),('L',(14,42)),('L',(22,35))])
path('front',(32,20),[('L',(38,20)),('A',(42,24),4,4,True),('L',(42,33)),('A',(38,37),4,4,True),('L',(38,42)),('L',(32,37)),('L',(30,37)),('A',(26,33),4,4,True),('L',(26,24)),('A',(30,20),4,4,True),('L',(32,20))],True);join('front','back')
self.add_dot('eye-left',(15,15));self.add_dot('eye-right',(23,15))
path('smile',(14,24),[('C',(20,24),(16,27),(18,27))])
''','Reply speck omitted; face retained.')
add('keypad-office-telephone','SQUARE','Rejected receiver is a plain arch and keypad has only two dots. Restore handset end pads and a three-key row.','phone: receiver terminals; grip: equal keypad series', '''
path('receiver',(6,18),[('L',(6,14)),('C',(24,6),(6,7),(15,6)),('C',(42,14),(33,6),(42,7)),('L',(42,18)),('L',(34,18)),('L',(31,14)),('L',(17,14)),('L',(14,18)),('L',(6,18))],True)
path('base',(12,26),[('L',(36,26)),('L',(42,42)),('L',(6,42)),('L',(12,26))],True)
for x in (16,24,32):self.add_dot(f'key{x}',(x,34))
''','Nine tiny key marks reduced to a row of three.')
add('interrupted-overlapping-square-outlines','SQUARE','Broken square fragment shrank into a dot-like hook and broad corner radii distort the interlocked outlines. Restore straight equal-size square edges and clear interruptions.','messages-square: overlapping frames; source interruption pattern', '''
path('upper',(30,18),[('L',(30,9)),('A',(27,6),3,3,False),('L',(9,6)),('A',(6,9),3,3,False),('L',(6,27)),('A',(9,30),3,3,False),('L',(18,30)),('L',(18,21)),('A',(21,18),3,3,True),('L',(30,18))])
path('lower',(38,18),[('L',(39,18)),('A',(42,21),3,3,True),('L',(42,39)),('A',(39,42),3,3,True),('L',(21,42)),('A',(18,39),3,3,True)])
poly('overlap',(30,26),(30,30),(26,30))
''','Interruptions widened to preserve 4px clear gaps.')
add('kimono-sash-belt','HRECT_M','Square sharp buckle and thick square hole lose the rounded horizontal belt buckle. Restore rounded buckle corners and wider central slot.','No useful exact match; source rectangular buckle and strap topology.', '''
box('buckle',12,10,36,38,4)
box('opening',20,20,28,28)
poly('left-strap',(12,16),(4,16),(4,32),(12,32));join('left-strap','buckle')
poly('right-strap',(36,16),(44,16),(44,32),(36,32));join('right-strap','buckle')
''')
if __name__=='__main__':
 import author
 author.D=D;generate(sys.argv[1:])
