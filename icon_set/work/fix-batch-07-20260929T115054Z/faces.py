from designs import *
HUMAN='Shared human_ref/user.svg: circular jaw and broad smooth shoulders; the bust uses touching head/body ink. Source supplies facial identity.'
spec(2,'VRECT_L','The current bald man has no eyes and a small face with prominent side spikes. No written feedback. Enlarged the circular head, restored two eyes and a smile, and reduced the side hair to short tufts above broad shoulders.', '''
circle('head',24,18,14)
line('hair-left',(10,18),(8,12));line('hair-right',(38,18),(40,12));join('head','hair-left','hair-right')
for x in (20,28):self.add_dot('eye'+str(x),(x,14))
bez('smile',(22,22),((23,24),(25,24),(26,22)))
arc('body-left',(8,44),(24,36),16,8);arc('body-right',(24,36),(40,44),16,8)
join('head','body-left');join('head','body-right')
''',HUMAN,extra='human_construction = "bust"')
spec(3,'VRECT_L','The rejected bob haircut is reduced to two outward ticks and the face has no eyes. No written feedback. Rebuilt a parted rounded hair crown, larger circular jaw, eyes and smile above a broad bust.', '''
arc('jaw',(10,18),(38,18),14,14,False)
path('hair',(10,18),[('C',(18,4),(10,9),(12,4)),('C',(24,9),(21,4),(22,9)),('C',(30,4),(26,9),(27,4)),('C',(38,18),(36,4),(38,9))]);join('jaw','hair')
for x in (18,30):self.add_dot('eye'+str(x),(x,15))
bez('smile',(22,23),((23,24),(25,24),(26,23)))
arc('body-left',(8,44),(24,36),16,8);arc('body-right',(24,36),(40,44),16,8)
join('jaw','body-left');join('jaw','body-right')
''',HUMAN,extra='human_construction = "bust"')
spec(4,'SQUARE','The rejected boy has a square lower face and a rigid symmetric fringe. No written feedback. Restored a circular lower jaw and an asymmetric swept hairline with clear eyes and smile; ears and eyebrows are omitted.', '''
path('head',(6,24),[('L',(6,18)),('A',(18,6),12),('L',(30,6)),('A',(42,18),12),('L',(42,24)),('A',(6,24),18)],True)
bez('fringe',(6,18),((14,18),(23,14),(28,14)),((33,14),(34,18),(42,18)));join('head','fringe')
for x in (18,30):self.add_dot('eye'+str(x),(x,25))
bez('smile',(22,32),((23,34),(25,34),(26,32)))
''','Shared human_ref/user.svg: circular lower jaw; source supplies the swept fringe and smile.')
spec(5,'SQUARE','The current cap is flattened sideways and the eyes are missing. No written feedback. Restored a taller rounded lower face, a domed cap, paired eyes and a clear smile; ears are omitted.', '''
arc('cap',(6,15),(42,15),18,9)
line('brim',(6,15),(42,15));join('cap','brim')
path('face',(42,15),[('L',(42,24)),('A',(6,24),18),('L',(6,15))]);join('face','brim')
for x in (16,32):self.add_dot('eye'+str(x),(x,24))
bez('smile',(20,32),((22,34),(26,34),(28,32)))
''','Shared human_ref/user.svg: circular jaw. Source supplies domed cap and broad smile.')
spec(6,'VRECT_L','The current superhero has a blank small head and a generic arched body. No written feedback. Enlarged the head to restore a smile and rebuilt angular cape shoulders with a simple chest chevron; tiny eyes and the enclosed emblem are omitted for spacing.', '''
circle('head',24,14,10)
bez('smile',(22,14),((23,16),(25,16),(26,14)))
path('body',(8,44),[('L',(8,38)),('C',(24,28),(8,31),(17,28)),('C',(40,38),(31,28),(40,31)),('L',(40,44))]);join('head','body')
poly('emblem',(20,38),(24,42),(28,38))
''',HUMAN,extra='human_construction = "bust"')
spec(7,'SQUARE','The rejected upright phone and short hand mark lose the hugging gesture. No written feedback. Tilted the phone and rebuilt the cheek and forearm as a continuous embracing contour while retaining the happy face.', '''
path('face-hand',(8,16),[('C',(24,6),(11,9),(17,6)),('C',(42,24),(34,6),(42,14)),('C',(30,42),(42,34),(38,42)),('C',(22,36),(24,42),(22,40)),('C',(30,32),(22,32),(27,32))])
poly('phone',(6,24),(18,24),(22,36),(24,42),(12,42),closed=True);join('phone','face-hand')
for x in (20,30):self.add_dot('eye'+str(x),(x,16))
bez('smile',(27,25),((29,27),(31,27),(33,24)))
''','Source establishes tilted device and hug. Shared circular facial vocabulary; no useful local smile reference was found.')
spec(8,'VRECT_L','The current flame has disconnected short upper marks with little upward motion. No written feedback. Restored long flowing outer wisps and an inner curl around the open smiling face.', '''
path('flame',(16,8),[('C',(8,28),(8,16),(8,21)),('A',(24,44),16,16,False),('A',(40,28),16,16,False),('L',(40,16)),('C',(40,4),(40,10),(37,8))])
bez('wisp',(26,4),((22,6),(22,10),(22,12)))
for x in (18,30):self.add_dot('eye'+str(x),(x,18))
path('mouth',(17,27),[('L',(31,27)),('A',(17,27),7,8,True)],True)
''','Lucide flame: flowing open flame tip; supplied reference owns eyes and open smile.')
spec(9,'SQUARE','The current glasses are filled-looking dots and the hair is a rectangular cap. No written feedback. Enlarged the round lenses, connected real temples and bridge, and restored a round jaw beneath a bun; small smile is retained.', '''
path('face',(6,24),[('L',(6,20)),('A',(12,14),6),('L',(36,14)),('A',(42,20),6),('L',(42,24)),('A',(6,24),18)],True)
arc('bun',(16,14),(32,14),8,8);join('bun','face')
for x in (15,33):circle('lens'+str(x),x,24,5)
line('bridge',(20,24),(28,24));join('bridge','lens15','lens33')
line('temple-left',(6,24),(10,24));line('temple-right',(38,24),(42,24));join('temple-left','face','lens15');join('temple-right','face','lens33')
bez('smile',(22,34),((23,35),(25,35),(26,34)))
''','Lucide glasses: actual round lenses and bridge. Shared human circular jaw; source supplies bun and expression.')
if __name__=='__main__':
 for i in map(int,sys.argv[1:]):make(i)
