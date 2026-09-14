from author import write
for i in (6,7):
 write(i,'SQUARE', '''
r('case',6,16,42,38,4)
p('handle',(16,16),(16,6),(32,6),(32,16))
link('connect','handle','case')
for x in (14,34):
    l(f'wheel-{x}',(x,38),(x,42))
    link('connect',f'wheel-{x}','case')
''','Suitcase: balanced rounded case, equal wheels, and a 10-unit handle opening.')
write(8,'HRECT_L', '''
r('frame',4,8,44,40,6)
for x in (14,24,34):
    l(f'bar-{x}',(x,18),(x,30))
''','Barcode: three evenly spaced bars in a smooth frame, with 10-unit border clearance.')
write(11,'VRECT_L', '''
r('body',8,14,40,44,4)
p('terminal',(16,14),(16,4),(32,4),(32,14))
link('connect','terminal','body')
p('charge',(26,23),(18,30),(29,30),(22,36))
''','Charging battery: spacious terminal and a clear lightning stroke inside a balanced body.')
write(13,'VRECT_L', '''
r('engine',16,4,40,20,4)
l('tiller',(8,16),(16,16))
link('connect','tiller','engine')
p('shaft',(24,20),(24,40),(28,44),(32,44),(32,20))
link('connect','shaft','engine')
l('propeller',(32,36),(40,36))
l('propeller-end',(40,30),(40,42))
link('connect','shaft','propeller')
link('connect','propeller','propeller-end')
''','Outboard motor: tangent engine corners, an 8-unit drive shaft and clear propeller.')
for i in (14,67):
 write(i,'VRECT_L', '''
a('bulb-top',(8,20),(40,20),16)
a('bulb-right',(40,20),(32,34),16)
l('base-right',(32,34),(32,40))
a('base-br',(32,40),(28,44),4)
l('base-bottom',(28,44),(20,44))
a('base-bl',(20,44),(16,40),4)
l('base-left',(16,40),(16,34))
a('bulb-left',(16,34),(8,20),16)
self.add_contour('bulb','bulb-top','bulb-right','base-right','base-br','base-bottom','base-bl','base-left','bulb-left',closed=True)
l('base-seam',(16,34),(32,34))
link('connect','base-seam','bulb')
''','Light bulb: circular crown, equal shoulders and a base with a 10-unit interior height.')
write(15,'SQUARE', '''
p('main',(6,42),(6,6),(30,6),(30,42),(6,42))
p('annex',(30,22),(42,22),(42,42),(30,42))
link('connect','annex','main')
for x in (14,22):
    l(f'window-{x}',(x,14),(x,18))
p('door',(14,42),(14,30),(22,30),(22,42))
link('connect','door','main')
''','Two buildings: consistent verticals, an 8-unit doorway and aligned foundation.')
for i in (17,18,19):
 write(i,'HRECT_L', '''
p('engine',(12,24),(12,16),(28,16),(34,22),(44,22),(44,40),(22,40),(16,32),(4,32))
l('intake',(4,20),(4,36))
l('intake-top',(4,24),(12,24))
link('connect','intake-top','intake')
link('connect','intake-top','engine')
link('connect','intake','engine')
l('cap',(16,8),(28,8))
l('cap-neck',(22,8),(22,16))
link('connect','cap-neck','cap')
link('connect','cap-neck','engine')
''','Engine silhouette: deliberate mechanical corners with 8-unit inlet and cap clearances.')
write(27,'VRECT_L', '''
a('euro',(40,4),(40,44),20,20,sweep=False)
l('upper',(8,20),(30,20))
l('lower',(8,28),(30,28))
link('connect','euro','upper')
link('connect','euro','lower')
''','Euro: one smooth semicircle with parallel crossbars 8 units apart.')
for i in (31,32):
 body="""
p('frame',(8,44),(8,4),(40,4),(40,44))
p('leaf',(40,4),(20,12),(20,36),(40,44))
link('connect','frame','leaf')
self.add_dot('knob',(30,25))
"""
 write(i,'VRECT_L',body,'Open door: straight perspective edges, a balanced leaf and a clear handle.')
write(34,'SQUARE', '''
p('cabinet',(6,38),(6,6),(42,6),(42,38),(6,38))
l('seam',(24,6),(24,38))
link('connect','seam','cabinet')
for x in (15,33):
    l(f'handle-{x}',(x,20),(x,24))
for x in (10,38):
    l(f'foot-{x}',(x,38),(x,42))
    link('connect',f'foot-{x}','cabinet')
''','Wardrobe: symmetric doors and handles, with consistent clearance from the centre seam.')
for i in (41,42):
 write(i,'SQUARE', '''
l('fork-left',(6,6),(6,18))
a('fork-bottom',(6,18),(22,18),8,sweep=False)
l('fork-right',(22,18),(22,6))
self.add_contour('fork','fork-left','fork-bottom','fork-right')
l('middle-tine',(14,6),(14,26))
l('fork-handle',(14,26),(14,42))
link('connect','middle-tine','fork')
link('connect','fork-handle','fork')
link('connect','middle-tine','fork-handle')
p('knife',(34,42),(34,6),(42,22),(42,30),(34,30))
''','Cutlery: equal 8-unit tine spacing, smooth fork bowl and a clear 8-unit knife blade.')
write(54,'VRECT_L', '''
r('case',8,14,40,40,4)
p('handle',(16,14),(16,4),(32,4),(32,14))
link('connect','handle','case')
for x in (12,36):
    l(f'wheel-{x}',(x,40),(x,44))
    link('connect',f'wheel-{x}','case')
''','Luggage: smooth equal corners, widened handle opening and matching feet.')
for i in (57,58):
 write(i,'VRECT_L', '''
r('capsule',17,4,31,28,7)
l('support-left',(8,22),(8,24))
a('support-bottom',(8,24),(40,24),16,sweep=False)
l('support-right',(40,24),(40,22))
self.add_contour('support','support-left','support-bottom','support-right')
l('stem',(24,40),(24,44))
link('connect','stem','support')
''','Microphone: circular capsule ends, a concentric cradle and no cramped grille ticks.')
for i in (59,60):
 write(i,'HRECT_L', '''
r('screen',4,8,44,30,4)
l('stand',(24,30),(24,40))
l('foot',(14,40),(34,40))
link('connect','stand','screen')
link('connect','stand','foot')
''','Television: natural wide screen, smooth corners and 10 units between screen and foot.')
write(64,'SQUARE', '''
r('paper',6,14,42,42,3)
for x in (14,24,34):
    l(f'ring-{x}',(x,6),(x,18))
    link('connect',f'ring-{x}','paper')
''','Notepad: matched binder strokes, smooth paper corners and 8-unit top spacing.')
write(65,'HRECT_L', '''
p('folder',(4,40),(4,8),(16,8),(24,16),(44,16),(44,40),(4,40))
l('seam',(4,24),(44,24))
link('connect','seam','folder')
''','Sealed folder: clean folder tab and an 8-unit band without wavy fitted edges.')
write(72,'HRECT_L', '''
r('field',4,8,44,40,4)
for x in (14,24):
    l(f'digit-{x}',(x,28),(x+1,28))
l('cursor',(34,18),(34,30))
''','PIN field: even entry spacing, smooth frame and an upright cursor.')
write(78,'SQUARE', '''
r('board',6,6,42,30,3)
l('header',(6,14),(42,14))
link('connect','header','board')
l('stem',(24,30),(24,42))
p('legs',(14,42),(24,30),(34,42))
link('connect','stem','board')
link('connect','legs','board')
link('connect','legs','stem')
''','Presentation board: even header band, rounded board and a symmetric tripod.')
write(87,'VRECT_L', '''
p('scanner',(8,44),(8,4),(40,4),(40,44))
l('header',(8,12),(40,12))
link('connect','header','scanner')
''','Security scanner: straight, symmetric portal with an 8-unit header.')
for i in (88,102,103):
 write(i,'SQUARE', '''
p('body',(8,16),(12,42),(36,42),(40,16))
l('rim',(6,16),(42,16))
p('handle',(16,16),(16,6),(32,6),(32,16))
link('connect','body','rim')
link('connect','handle','rim')
''','Tapered basket: symmetric sides, a clear handle and a single clean rim.')
write(96,'SQUARE', '''
r('plate',6,6,42,42,4)
r('switch',16,16,32,32,3)
l('seam',(16,24),(32,24))
link('connect','switch','seam')
''','Switch plate: centered rocker, consistent corner radii and equal 8-unit rocker halves.')
write(98,'SQUARE', '''
r('page',6,6,42,42,3)
for y,end in ((15,33),(24,33),(33,27)):
    l(f'text-{y}',(15,y),(end,y))
''','Task list: three straight baselines with even 9-unit spacing and balanced margins.')
write(99,'SQUARE', '''
l('left',(12,6),(12,22))
a('bowl',(12,22),(36,22),12,sweep=False)
l('right',(36,22),(36,6))
self.add_contour('letter','left','bowl','right')
l('underline',(6,42),(42,42))
''','Underlined U: a true semicircular bowl with 8 units above the underline.')
write(101,'VRECT_L', '''
r('carriage',8,4,40,34,6)
p('door',(20,34),(20,20),(28,20),(28,34))
link('connect','door','carriage')
l('track',(8,44),(40,44))
for x in (16,32):
    l(f'wheel-{x}',(x,34),(x,44))
    link('connect',f'wheel-{x}','carriage')
    link('connect',f'wheel-{x}','track')
''','Train rear: balanced carriage, clear doorway and evenly spaced running gear.')
write(105,'VRECT_L', '''
p('arrow',(16,34),(16,18),(8,18),(24,4),(40,18),(32,18),(32,34))
for x in (16,32):
    l(f'dash-{x}',(x,42),(x,44))
''','Upload arrow: centered arrowhead and shaft; detached dashes retain 8-unit spacing.')
write(106,'HRECT_L', '''
p('arrow',(18,30),(18,20),(10,20),(24,8),(38,20),(30,20),(30,30),(18,30))
p('tray',(4,32),(4,40),(44,40),(44,32))
''','Upload tray: symmetric arrow with a spacious shaft and 10-unit tray clearance.')
