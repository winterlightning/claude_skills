from author import write,ROOT,TARGETS
changes={4:[('(27,40)','(28,40)'),('(27,8)','(28,8)'),('(36,8)','(37,8)'),('(36,40)','(37,40)'),('8,16)','7,16)')],44:[('(26,34)','(26,33)')],77:[('(18,30)','(14,34)')],80:[('(24,16),(38,24),14,8','(24,12),(36,18),12,6'),('(38,24),(24,24),7,4','(36,18),(24,18),6,3')],107:[('(4,40)','(4,35)'),('(19,40)','(19,35)'),('(29,40)','(29,35)'),('(44,40)','(44,35)'),("24,40,5","24,35,5")],109:[('(16,33)','(18,33)'),('(11,24)','(13,24)')],95:[('(6,28)','(6,34)'),('(20,28)','(20,34)'),('(20,18)','(20,26)'),('(34,18)','(34,26)'),('(26,18)','(26,26)')]}
for i,pairs in changes.items():
 path=ROOT/TARGETS[i]['source_path'];s=path.read_text()
 for old,new in pairs:s=s.replace(old,new)
 path.write_text(s)
write(20,'SQUARE','''
p('castle',(6,42),(6,24),(30,24),(30,16),(42,16),(42,42),(6,42))
p('roof',(30,16),(36,6),(42,16))
link('connect','castle','roof')
l('tower',(30,24),(30,42))
link('connect','tower','castle')
p('gate',(14,42),(14,34),(22,34),(22,42))
link('connect','gate','castle')
l('pole',(6,24),(6,6))
p('flag',(6,6),(20,6),(16,14),(6,14))
link('connect','flag','pole')
link('connect','pole','castle')
''','Castle: broad connected wall and tower, clear gateway and a balanced flag.')
write(24,'SQUARE','''
a('face-top',(6,24),(42,24),18)
p('ice',(42,24),(42,34),(36,42),(30,36),(24,42),(18,36),(12,42),(6,34),(6,24))
link('connect','face-top','ice')
l('mouth',(16,27),(32,27))
for x in (20,28):
    self.add_dot(f'eye-{x}',(x,16))
''','Frozen face: circular crown, balanced eyes and an open neutral mouth above the deliberate ice points.')
write(33,'SQUARE','''
p('front',(18,6),(42,6),(42,28),(36,28),(36,36),(28,28),(18,28),(18,6))
p('back',(18,18),(6,18),(6,36),(16,36),(24,42),(24,28))
link('connect','front','back')
''','Overlapping comments: clean visible bubble outlines, with 8-unit panel separation and readable tails.')
write(37,'SQUARE','''
p('front',(6,20),(18,26),(18,42),(6,36),(6,20))
p('middle',(14,12),(28,19),(28,36))
p('back',(26,6),(42,14),(42,30))
''','Compute stack: three regular perspective panels with clear diagonal separation.')
write(38,'SQUARE','''
p('cube',(24,16),(32,20),(32,28),(24,32),(16,28),(16,20),(24,16))
p('edges',(16,20),(24,24),(32,20))
l('vertical',(24,24),(24,32))
link('connect','cube','edges')
link('connect','cube','vertical')
link('connect','edges','vertical')
p('outer-left',(18,42),(6,34),(6,14),(24,6),(30,9))
p('outer-right',(40,15),(42,16),(42,34),(30,42))
''','MediaConnect: equal cube faces inside evenly separated hexagonal brackets.')
write(43,'HRECT_L','''
p('castle',(4,8),(12,8),(12,16),(20,16),(20,8),(28,8),(28,16),(36,16),(36,8),(44,8),(44,24),(38,28),(38,40),(10,40),(10,28),(4,24),(4,8))
''','Fortress: three equal battlements with 8-unit openings and a balanced broad wall.')
write(45,'VRECT_L','''
p('f',(8,20),(8,4),(18,4))
l('f-bar',(8,12),(16,12))
link('connect','f','f-bar')
p('r',(30,20),(30,4),(40,4),(40,12),(30,12),(40,20))
for x in (8,30):
    p(f'e-{x}',(x+10,28),(x,28),(x,44),(x+10,44))
    l(f'bar-{x}',(x,36),(x+8,36))
    link('connect',f'e-{x}',f'bar-{x}')
''','FREE lettering: equal 16-unit letter heights and 8-unit spacing between each horizontal stroke.')
write(69,'SQUARE','''
# Four equal cells keep the pattern legible without nine cramped counters.
for row in range(2):
    for col in range(2):
        x,y=6+24*col,6+24*row
        r(f'cell-{row}-{col}',x,y,x+12,y+12,3)
''','Pattern: four equal rounded cells with generous uniform gaps, replacing nine undersized loops.')
write(75,'VRECT_L','''
p('pot',(16,34),(16,44),(32,44),(32,34),(16,34))
l('stem',(24,34),(24,20))
link('connect','stem','pot')
for side in (-1,1):
    tip=(24+side*16,4)
    a(f'leaf-{side}-a',(24,20),tip,16,sweep=side<0)
    a(f'leaf-{side}-b',tip,(24,20),16,sweep=side<0)
    self.add_contour(f'leaf-{side}',f'leaf-{side}-a',f'leaf-{side}-b',closed=True)
    link('connect',f'leaf-{side}','stem')
    l(f'branch-{side}',(24,32),(24+side*16,26))
    link('connect',f'branch-{side}','stem')
link('connect','leaf--1','leaf-1')
link('connect','branch--1','branch-1')
''','Potted plant: two broad mirrored leaves, a central stem and open lower branches.')
write(83,'SQUARE','''
a('head-top',(10,14),(38,14),14,8)
a('head-bottom',(38,32),(10,32),14,10)
r('goggles',6,14,42,32,4)
link('connect','head-top','goggles')
link('connect','head-bottom','goggles')
''','VR headset: smooth head arcs end at the visor, removing tiny overlap pockets.')
write(84,'SQUARE','''
p('printer-top',(14,34),(6,34),(6,18),(42,18),(42,34),(34,34))
p('paper-in',(12,18),(12,6),(36,6),(36,18))
link('connect','paper-in','printer-top')
p('receipt',(14,26),(14,42),(20,38),(26,42),(34,38),(34,26))
l('slot',(10,26),(38,26))
link('connect','receipt','slot')
link('connect','receipt','printer-top')
''','Receipt printer: clear 8-unit body bands and a paper opening with no hidden edge across the receipt.')
write(94,'HRECT_L','''
p('base',(4,32),(4,40),(36,40),(40,36))
p('lid',(10,8),(44,28),(40,36),(6,16),(10,8))
link('connect','base','lid')
''','Stapler: straight broad lid and open base joined at the rear hinge without a trapped sliver.')
write(110,'CIRCLE','''
c('coin',24,24,20)
l('top',(20,16),(26,16))
a('bowl',(26,16),(26,32),8)
l('bottom',(26,32),(16,32))
l('stem',(16,32),(20,16))
self.add_contour('d','top','bowl','bottom','stem',closed=True)
for x in (20,28):
    l(f'top-tick-{x}',(x,13),(x,20))
    l(f'bottom-tick-{x}',(x,28),(x,35))
    link('connect',f'top-tick-{x}','d')
    link('connect',f'bottom-tick-{x}','d')
''','Digibyte: a smooth closed D and two consistent currency ticks inside a true circular rim.')
write(112,'VRECT_L','''
p('top',(8,12),(24,4),(40,12),(24,20),(8,12))
p('middle',(8,24),(24,32),(40,24))
p('bottom',(8,36),(24,44),(40,36))
''','Layered currency: one clear diamond and two equally spaced lower layers, preserving all three levels.')
