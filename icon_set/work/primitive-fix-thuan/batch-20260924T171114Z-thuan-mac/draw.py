from author import put,write,ROWS
SOURCE_ICON_ID=tuple(row['source_uuid'] for row in ROWS)
SOURCE_PATH=tuple(row['reference_path'] for row in ROWS)
AUTHOR='gpt-6'
put('hand-swipe-up-gesture-solo','HRECT_L','hand','A side-facing hand with rounded index fingertip and raised thumb sits beneath an upward arrow. Hand anatomy follows the original; shared human-reference guide reviewed; no detached head/body.', '''
path('hand',(4,38),[('L',(4,30)),('C',(7,27),(4,29),(5,28)),('L',(20,22)),('C',(25,24),(23,22),(25,22)),('C',(22,28),(25,26),(23,27)),('L',(40,28)),('A',(40,36),4,4,True),('L',(28,36)),('C',(25,40),(26,36),(27,40)),('L',(7,40)),('A',(4,38),3,2,True)],True)
poly('arrowhead',(18,14),(24,8),(30,14));line('shaft',(24,8),(24,14));join('shaft','arrowhead')
''','Small palm folds omitted.')
put('layer-style','SQUARE','none','Italic f with smooth terminal transitions and a separate symmetric x; crossing halves reuse one node.', '''
path('f',(6,42),[('C',(14,34),(11,42),(13,39)),('L',(18,18)),('L',(19,14)),('C',(28,6),(20,8),(23,6)),('L',(30,6))])
poly('bar',(12,18),(18,18),(23,18));join('bar','f')
# The f stem is split at its actual bar junction below.
poly('x-down',(30,22),(36,30),(42,38));poly('x-up',(30,38),(36,30),(42,22));join('x-down','x-up')
''')
put('message-bubble-with-text','SQUARE','message-circle','A smooth oval chat bubble owns a lower-left tail and three evenly spaced centered text lines.', '''
path('outline',(6,23),[('A',(24,6),18,17,True),('A',(42,23),18,17,True),('A',(24,40),18,17,True),('C',(15,38),(20,40),(17,39)),('L',(7,42)),('L',(10,32)),('C',(6,23),(7,29),(6,26))],True)
for name,y,x0,x1 in [('top',15,20,28),('middle',23,16,32),('bottom',31,20,28)]:line('text-'+name,(x0,y),(x1,y))
''')
for key in ['note-1','note-solo']:
 put(key,'VRECT_L','clipboard','A symmetric blank clipboard uses a centered capsule clip and identical tangent board corners.', '''
path('clip',(20,4),[('L',(28,4)),('A',(32,8),4,4,True),('A',(28,12),4,4,True),('L',(20,12)),('A',(16,8),4,4,True),('A',(20,4),4,4,True)],True)
path('board',(16,8),[('L',(12,8)),('A',(8,12),4,4,False),('L',(8,40)),('A',(12,44),4,4,False),('L',(36,44)),('A',(40,40),4,4,False),('L',(40,12)),('A',(36,8),4,4,False),('L',(32,8))]);join('board','clip')
''')
put('open-paper-booklet','VRECT_M','book-open','A rounded front cover and raised back leaf with a smooth upper corner share the binding nodes.', '''
path('front',(10,16),[('L',(34,16)),('A',(38,20),4,4,True),('L',(38,40)),('A',(34,44),4,4,True),('L',(14,44)),('A',(10,40),4,4,True),('L',(10,16))],True)
path('back',(10,16),[('L',(28,5)),('C',(32,4),(30,4),(31,4)),('C',(34,8),(34,4),(34,6)),('L',(34,16))]);join('front','back')
''')
put('proximity-alert-sensor-strokes','HRECT_M','radar','The source contains only three separated sensor marks; reconstruct those as exact straight runs with the same directions and arrangement.', '''
line('left',(4,14),(4,38))
line('top',(22,10),(28,10))
line('right',(38,21),(44,25))
''','None; intentionally sparse reference preserved.')
put('simple-home-icon','VRECT_L','house','A symmetric closed home-like upward outline has matching 45-degree roof slopes, a smooth rounded apex and equal lower corner radii.', '''
path('home',(8,20),[('L',(22,6)),('C',(24,4),(23,5),(23,4)),('C',(26,6),(25,4),(25,5)),('L',(40,20)),('L',(40,41)),('A',(37,44),3,3,True),('L',(11,44)),('A',(8,41),3,3,True),('L',(8,20))],True)
''')
put('square-speech-bubble-solo','VRECT_L','message-square','Open lower-left speech tail belongs to a rectangular bubble with equal smooth corner radii.', '''
path('bubble',(8,34),[('L',(8,8)),('A',(12,4),4,4,True),('L',(36,4)),('A',(40,8),4,4,True),('L',(40,30)),('A',(36,34),4,4,True),('L',(20,34)),('L',(8,44))])
''')
put('stacked-paper-documents-solo','VRECT_L','files','Two staggered sheets with straight diagonal cut corners and matching rounded outer corners; rear outline stops at the front sheet.', '''
path('front',(11,14),[('L',(24,14)),('L',(32,22)),('L',(32,34)),('L',(32,41)),('A',(29,44),3,3,True),('L',(11,44)),('A',(8,41),3,3,True),('L',(8,17)),('A',(11,14),3,3,True)],True)
path('back',(16,14),[('L',(16,7)),('A',(19,4),3,3,True),('L',(31,4)),('L',(40,13)),('L',(40,31)),('A',(37,34),3,3,True),('L',(32,34))]);join('front','back')
''')
put('spiral-cut-strudel-roll','SQUARE','cylinder','The pastry cross-section is a continuous spiral with tangent quarter-circle corners; a diagonal back surface preserves depth.', '''
path('spiral',(16,30),[('L',(20,30)),('A',(24,26),4,4,False),('L',(24,24)),('A',(16,16),8,8,False),('L',(14,16)),('A',(6,24),8,8,False),('L',(6,34)),('A',(14,42),8,8,False),('L',(26,42)),('A',(34,34),8,8,False),('L',(34,24))])
path('back',(14,16),[('L',(24,6)),('L',(34,6)),('A',(42,14),8,8,True),('C',(40,18),(42,16),(41,17)),('L',(34,24))]);join('back','spiral')
''','One clear spiral turn retained instead of closely nested turns.')
put('rotate-front','SQUARE','rotate-cw','Two overlapping square tiles sit below a double-ended quarter-circle rotation arrow; rounded tile corners and exact shared joins.', '''
path('front',(9,18),[('L',(19,18)),('A',(22,21),3,3,True),('L',(22,31)),('A',(19,34),3,3,True),('L',(16,34)),('L',(9,34)),('A',(6,31),3,3,True),('L',(6,21)),('A',(9,18),3,3,True)],True)
path('back',(22,31),[('L',(39,31)),('A',(42,34),3,3,True),('L',(42,39)),('A',(39,42),3,3,True),('L',(19,42)),('A',(16,39),3,3,True),('L',(16,34))]);join('front','back')
path('rotation',(26,10),[('A',(38,22),12,12,True)])
poly('start',(30,6),(26,10),(30,14));poly('end',(34,18),(38,22),(42,18));join('rotation','start');join('rotation','end')
''')
if __name__=='__main__':write()
