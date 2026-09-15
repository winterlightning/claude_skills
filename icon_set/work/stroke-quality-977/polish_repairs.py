"""Final contour polish following enlarged before/after inspection."""
from final_repairs import *
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/intersection-review-977/cohort.json'
AUTHOR='gpt-6'
p=Path(byid['dryer-hair']['python_source']['path']);s=p.read_text().replace("self.add_line('nozzle-top',(6,10),(30,6))","self.add_line('nozzle-top',(6,10),(28,7))").replace("self.add_bezier('back-top',(30,6),((36,5),(42,10),(42,16)))","self.add_bezier('back-top',(28,7),((32,7-6/11),(32,6),(34,6)),((39,6),(42,10),(42,16)))");p.write_text(s)
burger='''
self.add_arc('bun-left',(8,20),(20,8),radius_x=12)
self.add_line('bun-top',(20,8),(28,8))
self.add_arc('bun-right',(28,8),(40,20),radius_x=12)
self.add_bezier('filling-right',(40,20),((42,20),(44,22),(44,25)),((44,28),(42,30),(40,30)))
self.add_arc('base-right',(40,30),(30,40),radius_x=10)
self.add_line('base',(30,40),(18,40))
self.add_arc('base-left',(18,40),(8,30),radius_x=10)
self.add_bezier('filling-left',(8,30),((6,30),(4,28),(4,25)),((4,22),(6,20),(8,20)))
self.add_contour('outline','bun-left','bun-top','bun-right','filling-right','base-right','base','base-left','filling-left',closed=True)
self.add_line('lower-divider',(8,30),(40,30))
self.relate('connect','lower-divider','outline')
'''
for id in ['hamburger','hamburger-symbol']:
 divider="self.add_line('upper-divider',(8,20),(40,20))" if id=='hamburger-symbol' else "self.add_bezier('upper-divider',(8,20),((11,24),(13,24),(16,20)),((19,16),(21,16),(24,20)),((27,24),(29,24),(32,20)),((35,16),(37,16),(40,20)))"
 patch(id,burger+'\n'+divider+"\nself.relate('connect','upper-divider','outline')",'HRECT_L; circular paired bun corners, smooth filling ends and shared dividers; retain wavy versus plain filling.','Geometric mirrored bun and repeated wave.')
patch('pot','''
self.add_polyline('spout',(10,42),(6,42),(6,38))
self.add_bezier('body-left',(6,38),((6,33),(7,28),(8,23)))
self.add_polyline('rim',(8,23),(6,19),(31,19))
self.add_bezier('body-right',(31,19),((32,24),(34,28),(34,33)))
self.add_line('body-right-base',(34,33),(34,38))
self.add_arc('base-corner',(34,38),(30,42),radius_x=4)
self.add_line('base',(30,42),(10,42))
self.add_contour('body','spout-1','spout-2','body-left','rim-1','rim-2','body-right','body-right-base','base-corner','base',closed=True)
self.contours=self.contours[2:]
self.add_arc('lid-left',(10,19),(20,8),radius_x=10,radius_y=11)
self.add_arc('lid-right',(20,8),(30,19),radius_x=10,radius_y=11)
self.add_contour('lid','lid-left','lid-right')
self.add_line('knob',(20,6),(20,8))
self.add_bezier('handle',(31,19),((37,16),(42,20),(42,25)),((42,30),(38,33),(34,33)))
self.relate('connect','handle','body')
self.relate('connect','lid','body')
self.relate('connect','knob','lid')
''','SQUARE; smooth elliptical lid and handle; preserve the left spout and directional kettle body.','Geometric lid and coherent handle curves.')
patch('safety-helmet-construction','''
self.add_bezier('left-shell',(18,11),((11,13),(7,20),(7,29)))
self.add_bezier('left-brim',(7,29),((5,29),(4,31),(4,33)),((4,37),(15,40),(24,40)))
self.add_bezier('right-brim',(24,40),((33,40),(44,37),(44,33)),((44,31),(43,29),(41,29)))
self.add_bezier('right-shell',(41,29),((41,20),(37,13),(30,11)))
self.add_contour('shell','left-shell','left-brim','right-brim','right-shell')
self.add_arc('ridge-left',(18,11),(21,8),radius_x=3)
self.add_line('ridge-top',(21,8),(27,8))
self.add_arc('ridge-right',(27,8),(30,11),radius_x=3)
self.add_contour('ridge','ridge-left','ridge-top','ridge-right')
self.add_line('rib-left',(18,11),(19,23))
self.add_line('rib-right',(30,11),(29,23))
self.relate('connect','ridge','shell')
for name in ['rib-left','rib-right']:
    self.relate('connect',name,'ridge')
    self.relate('connect',name,'shell')
''','HRECT_L; mirrored shell and brim, smooth crest and identical ridge corners.','Geometric mirrored shell; source retains the protective ridge.')
patch('table-lamp-retro','''
self.add_arc('dome-left',(8,24),(24,6),radius_x=16,radius_y=18)
self.add_arc('dome-right',(24,6),(40,24),radius_x=16,radius_y=18)
self.add_bezier('rim-right',(40,24),((37,20),(35,20),(32,24)),((29,28),(27,24),(24,22)))
self.add_bezier('rim-left',(24,22),((21,24),(19,28),(16,24)),((13,20),(11,20),(8,24)))
self.add_contour('shade','dome-left','dome-right','rim-right','rim-left',closed=True)
self.add_line('finial',(24,4),(24,6))
self.add_line('stem',(24,22),(24,44))
self.add_line('foot',(16,44),(32,44))
self.relate('connect','finial','shade')
self.relate('connect','stem','shade')
self.relate('connect','stem','foot')
''','VRECT_L; elliptical dome, reflected scallops and centered stem; preserve the decorative rim.','Geometric dome and mirrored rim waves.')
# Eye strokes terminate at the same authored nodes as their diagonals.
for id,mirror in [('blind',True),('hidden',False)]:
 patch(id,f'mirror = {mirror}\n'+'''
def p(x,y):return (48-x,y) if mirror else (x,y)
self.add_bezier('upper-left',p(4,24),(p(8,16),p(15,8),p(24,8)))
self.add_bezier('upper-right',p(24,8),(p(33,8),p(40,16),p(44,24)))
self.add_bezier('lower-right',p(44,24),(p(40,32),p(33,40),p(24,40)))
self.add_bezier('lower-left',p(24,40),(p(15,40),p(8,32),p(4,24)))
self.add_contour('outline','upper-left','upper-right','lower-right','lower-left',closed=True)
# Split the two exact cubic midpoints into integer nodes for the diagonal.
from ...primitives import Bezier,Point
for i,q in enumerate(self.primitives):
    if q.element_id in ('upper-left','lower-right'):
        a=q.start.as_tuple();b,c,d=q.segments[0]
        def mid(u,v):return tuple((x+y)/2 for x,y in zip(u,v))
        ab,bc,cd=mid(a,b),mid(b,c),mid(c,d)
        abc,bcd=mid(ab,bc),mid(bc,cd);m=mid(abc,bcd)
        # Cubic midpoint here is fractional, so keep it in the smooth run.
        self.primitives[i]=Bezier(q.element_id,q.start,q.end,((ab,abc,m),(bcd,cd,d)))
# Exact nearby shared diagonal nodes are used in an independently reconstructed lens below.
''','HRECT_L; mirrored coherent lens; diagonal attachment reconstructed below.','Geometric symmetric lens.')
 # Use exact endpoint knots, preserving the original slash orientation.
 patch(id,f'mirror = {mirror}\n'+'''
def p(x,y):return (48-x,y) if mirror else (x,y)
self.add_bezier('upper-left',p(4,24),(p(7,19),p(10,14),p(14,12)),(p(18,10),p(20,8),p(24,8)))
self.add_bezier('upper-right',p(24,8),(p(33,8),p(39,15),p(44,24)))
self.add_bezier('lower-right',p(44,24),(p(41,29),p(38,34),p(34,36)),(p(30,38),p(28,40),p(24,40)))
self.add_bezier('lower-left',p(24,40),(p(15,40),p(9,33),p(4,24)))
self.add_contour('outline','upper-left','upper-right','lower-right','lower-left',closed=True)
self.add_line('slash',p(14,12),p(34,36))
self.relate('connect','slash','outline')
''','HRECT_L; coherent lens with diagonal terminating exactly on its curve knots; retain slash direction.','Geometric paired curves and shared nodes.')
patch('lgbt-heart','''
self.add_bezier('left-inner',(24,14),((21,10),(18,8),(14,8)))
self.add_arc('left-lobe',(14,8),(4,20),radius_x=10,radius_y=12,sweep=False)
self.add_bezier('left-shoulder',(4,20),((4,23),(7,25),(10,28)))
self.add_line('left-point',(10,28),(24,40))
self.add_line('right-point',(24,40),(38,28))
self.add_bezier('right-shoulder',(38,28),((41,25),(44,23),(44,20)))
self.add_arc('right-lobe',(44,20),(34,8),radius_x=10,radius_y=12,sweep=False)
self.add_bezier('right-inner',(34,8),((30,8),(27,10),(24,14)))
self.add_contour('outline','left-inner','left-lobe','left-shoulder','left-point','right-point','right-shoulder','right-lobe','right-inner',closed=True)
self.add_line('upper-band',(4,20),(44,20))
self.add_line('lower-band',(10,28),(38,28))
self.relate('connect','upper-band','outline')
self.relate('connect','lower-band','outline')
''','HRECT_L; mirrored lobes, level bands and exact attachment nodes.','Lucide heart: matched lobe construction; source bands preserved.')
patch('ffffound-logo','''
self.add_bezier('left-inner',(24,13),((24,8),(20,4),(16,4)))
self.add_arc('left-lobe',(16,4),(8,14),radius_x=8,radius_y=10,sweep=False)
self.add_bezier('left-side',(8,14),((8,21),(19,32),(24,44)))
self.add_bezier('right-side',(24,44),((29,32),(40,21),(40,14)))
self.add_arc('right-lobe',(40,14),(32,4),radius_x=8,radius_y=10,sweep=False)
self.add_bezier('right-inner',(32,4),((28,4),(24,8),(24,13)))
self.add_contour('outline','left-inner','left-lobe','left-side','right-side','right-lobe','right-inner',closed=True)
''','VRECT_L; matched tall lobes and smooth tapered sides; remove the tiny bottom stub.','Lucide heart: smooth paired lobes; retain the elongated logo shape.')
save()
