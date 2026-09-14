from author import write,TARGETS,ROOT
# Small local changes preserve each symbol's shared construction.
replacements={11:[('(22,36)','(22,35)')],4:[('(28,40)','(27,40)'),('(28,8)','(27,8)')],10:[('(28,26)','(24,26)'),('(28,42)','(24,42)')],28:[('(22,31)','(22,32)'),('(29,31)','(29,32)')],26:[('(10,18)','(10,15)'),('(38,18)','(38,15)'),('(24,18)','(24,15)'),('x,21,3','x,18,3')],12:[("p('neck',(44,18),(44,40),(34,36),(26,32),(10,32))","l('neck-a',(44,18),(44,40))\n        l('neck-b',(44,40),(34,36))\n        l('neck-c',(34,36),(26,32))\n        l('neck-d',(26,32),(10,32))"),("'neck','jaw'","'neck-a','neck-b','neck-c','neck-d','jaw'")],24:[("self.add_contour('face','face-top','ice',closed=True)","link('connect','face-top','ice')")]}
for i,pairs in replacements.items():
 path=ROOT/TARGETS[i]['source_path'];s=path.read_text()
 for old,new in pairs:s=s.replace(old,new)
 path.write_text(s)
for i in (14,67):
 write(i,'VRECT_L','''
a('crown',(8,20),(40,20),16)
a('shoulder-r',(40,20),(32,28),8)
a('neck-r',(32,28),(28,32),4,sweep=False)
l('base-r',(28,32),(28,42))
a('base-br',(28,42),(26,44),2)
l('base-bottom',(26,44),(22,44))
a('base-bl',(22,44),(20,42),2)
l('base-l',(20,42),(20,32))
a('neck-l',(20,32),(16,28),4,sweep=False)
a('shoulder-l',(16,28),(8,20),8)
self.add_contour('bulb','crown','shoulder-r','neck-r','base-r','base-br','base-bottom','base-bl','base-l','neck-l','shoulder-l',closed=True)
l('seam',(20,34),(28,34))
link('connect','bulb','seam')
''','Light bulb: tangent circular crown and reverse-curved shoulders, with a balanced open base.')
write(9,'SQUARE','''
p('sails',(24,6),(8,26),(40,26),(24,6))
l('mast',(24,6),(24,34))
p('hull',(6,34),(12,42),(36,42),(42,34),(6,34))
link('connect','mast','sails')
link('connect','mast','hull')
''','Sailboat: balanced triangular sails, an upright mast and an 8-unit-deep hull.')
write(20,'SQUARE','''
p('castle',(6,42),(6,26),(14,26),(14,30),(30,30),(30,16),(42,16),(42,42),(6,42))
p('roof',(30,16),(36,6),(42,16))
link('connect','castle','roof')
l('tower',(30,30),(30,42))
link('connect','tower','castle')
p('gate',(14,42),(14,34),(22,34),(22,42))
link('connect','gate','castle')
l('flagpole',(6,26),(6,6))
p('flag',(6,6),(20,6),(16,14),(6,14))
link('connect','flag','flagpole')
link('connect','flagpole','castle')
''','Castle: one connected wall and tower, a broad gateway, and a clean flag.')
write(30,'VRECT_L','''
r('shell',14,12,34,40,10)
l('seam',(24,12),(24,40))
link('connect','seam','shell')
for side in (-1,1):
    for j,y in enumerate((22,31,40)):
        # End at the same side of the shell; the bottom leg meets its apex.
        start=(14 if side<0 else 34,y) if j<2 else (24,40)
        end=(8 if side<0 else 40, y-6 if j==0 else (44 if j==2 else y))
        l(f'leg-{side}-{j}',start,end)
        link('connect',f'leg-{side}-{j}','shell')
        if j==2:
            link('connect',f'leg-{side}-{j}','seam')
    l(f'antenna-{side}',(24,12),(24+side*10,4))
    link('connect',f'antenna-{side}','shell')
    link('connect',f'antenna-{side}','seam')
link('connect','antenna--1','antenna-1')
link('connect','leg--1-2','leg-1-2')
''','Beetle: a smooth capsule shell with a central seam and symmetric single-stroke appendages.')
