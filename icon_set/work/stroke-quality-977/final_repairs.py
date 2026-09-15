"""Further individually selected contour reconstructions."""
from more_repairs import *
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/intersection-review-977/cohort.json'
AUTHOR='gpt-6'
# Exact tangent correction at the heart's diagonal flanks, plus clear check spacing.
for id in ['heart-0104273d','heart-romance','hearts-card','heart-check']:
 p=Path(byid[id]['python_source']['path']);s=p.read_text().replace('(7,25)','(6.5,25)').replace('(41,25)','(41.5,25)')
 if id=='heart-check':s=s.replace("(16,22),(22,28),(32,18)","(16,21),(22,27),(31,18)")
 p.write_text(s)
patch('draining-net','''
self.add_arc('handle-top',(20,8),(28,8),radius_x=4)
self.add_line('handle-right',(28,8),(28,22))
self.add_bezier('neck-right',(28,22),((34,23),(40,27),(40,33)))
self.add_arc('bowl',(40,33),(8,33),radius_x=16,radius_y=11)
self.add_bezier('neck-left',(8,33),((8,27),(14,23),(20,22)))
self.add_line('handle-left',(20,22),(20,8))
self.add_contour('outline','handle-top','handle-right','neck-right','bowl','neck-left','handle-left',closed=True)
''','VRECT_L; matched handle walls and smooth mirrored bowl; remove degenerate tip dots.','Geometric capsule and ellipse with paired shoulders.')
dress='''
self.add_line('left-strap',(16,4),(16,9))
self.add_bezier('left-bodice',(16,9),((14,12),(18,17),(17,20)))
self.add_bezier('left-skirt',(17,20),((15,26),(10,34),(8,40)))
self.add_bezier('hem',(8,40),((13,42),(18,44),(24,44)),((30,44),(35,42),(40,40)))
self.add_bezier('right-skirt',(40,40),((38,34),(33,26),(31,20)))
self.add_bezier('right-bodice',(31,20),((30,17),(34,12),(32,9)))
self.add_line('right-strap',(32,9),(32,4))
self.add_contour('dress','left-strap','left-bodice','left-skirt','hem','right-skirt','right-bodice','right-strap')
'''
for id in ['dress-00ccbf9d','dress-clothes']:
 neckline="self.add_polyline('neckline',(16,9),(24,14),(32,9))" if id=='dress-00ccbf9d' else "self.add_bezier('neckline',(16,9),((20,9),(21,10),(24,12)),((27,10),(28,9),(32,9)))"
 patch(id,dress+'\n'+neckline+"\nself.relate('connect','neckline','dress')",'VRECT_L; paired straps, mirrored bodice, flowing skirt and centered hem.','Geometric mirrored garment; retain V versus sweetheart neckline distinction.')
patch('dryer-hair','''
self.add_line('nozzle-top',(6,10),(30,6))
self.add_bezier('back-top',(30,6),((36,5),(42,10),(42,16)))
self.add_bezier('back-bottom',(42,16),((42,21),(38,23),(36,28)))
self.add_line('handle-right',(36,28),(31,38))
self.add_bezier('handle-base',(31,38),((30,40),(29,42),(26,42)),((24,42),(23,41),(22,40)))
self.add_line('handle-left',(22,40),(27,26))
self.add_polyline('nozzle-bottom',(27,26),(6,22),(6,10))
self.add_contour('outline','nozzle-top','back-top','back-bottom','handle-right','handle-base','handle-left','nozzle-bottom-1','nozzle-bottom-2',closed=True)
self.contours.pop(0)
''','SQUARE; smooth motor housing and rounded handle base, retaining directional nozzle.','Geometric smooth housing; no close Lucide hairdryer match.')
# Full ring contacts use integer 3-4-5 points instead of mismatched diagonal stubs.
patch('help-wheel',circle+'''
circle('outer',24,24,20)
circle('inner',24,24,10)
for i,(sx,sy) in enumerate([(-1,-1),(1,-1),(1,1),(-1,1)]):
    self.add_line(f'bridge-{i}',(24+sx*6,24+sy*8),(24+sx*12,24+sy*16))
    self.relate('connect',f'bridge-{i}','outer')
    self.relate('connect',f'bridge-{i}','inner')
''','CIRCLE; concentric rings and four reflected bridges ending exactly on both circles.','Geometric circles and exact radial contacts.')
patch('ice-cream-cone-food','''
self.add_bezier('crown-left',(8,18),((8,10),(14,4),(24,4)))
self.add_bezier('crown-right',(24,4),((34,4),(40,10),(40,18)))
self.add_bezier('right-scallop',(40,18),((40,22),(35,24),(32,21)))
self.add_bezier('center-scallop',(32,21),((28,25),(20,25),(16,21)))
self.add_bezier('left-scallop',(16,21),((13,24),(8,22),(8,18)))
self.add_contour('scoop','crown-left','crown-right','right-scallop','center-scallop','left-scallop',closed=True)
self.add_polyline('cone',(16,21),(24,44),(32,21))
self.relate('connect','cone','scoop')
''','VRECT_L; mirrored scoop and cone, smooth crown and three deliberate scallops.','Geometric paired curves; retain the scoop and cone.')
patch('ladle','''
self.add_arc('hook',(30,9),(40,9),radius_x=5)
self.add_line('handle',(26,33),(30,9))
self.add_arc('bowl',(8,33),(26,33),radius_x=9,radius_y=11,sweep=False)
self.add_line('rim',(26,33),(8,33))
self.add_contour('cup','bowl','rim',closed=True)
self.add_contour('handle-run','handle','hook')
self.relate('connect','cup','handle-run')
''','VRECT_L; one clean hook and elliptical bowl, straight handle and exact rim attachment.','Geometric ellipse and circular hook.')
patch('liras','''
self.add_bezier('crest',(40,12),((40,7),(35,4),(29,4)),((23,4),(18,7),(18,12)))
self.add_line('stem',(18,12),(18,34))
self.add_arc('foot-turn',(18,34),(8,44),radius_x=10)
self.add_contour('run','crest','stem','foot-turn')
self.add_line('foot',(8,44),(40,44))
for i,y in enumerate((19,33)):
    self.add_line(f'bar-{i}',(9,y),(30,y))
    self.relate('connect',f'bar-{i}','run')
self.relate('connect','foot','run')
''','VRECT_L; coherent rounded crest and foot, straight shared stem.','Geometric tangent crest and circular foot turn.')
patch('peso-money','''
self.add_polyline('stem',(14,42),(14,6),(33,6))
self.add_arc('bowl',(33,6),(33,24),radius_x=9)
self.add_line('bar',(33,24),(6,24))
self.add_contour('run','stem-1','stem-2','bowl','bar')
self.contours.pop(0)
''','SQUARE; one semicircular P bowl meets horizontal top and crossbar.','Geometric letter construction with tangent bowl.')
patch('neck-pillow','''
self.add_bezier('outer-left',(14,40),((7,40),(4,30),(4,24)),((4,13),(13,8),(24,8)))
self.add_bezier('outer-right',(24,8),((35,8),(44,13),(44,24)),((44,30),(41,40),(34,40)))
self.add_bezier('right-tip',(34,40),((31,40),(29,38),(29,35)),((29,32),(32,28),(32,24)))
self.add_bezier('inner',(32,24),((32,20),(28,18),(24,18)),((20,18),(16,20),(16,24)))
self.add_bezier('left-tip',(16,24),((16,28),(19,32),(19,35)),((19,38),(17,40),(14,40)))
self.add_contour('outline','outer-left','outer-right','right-tip','inner','left-tip',closed=True)
''','HRECT_L; exact mirrored arms, smooth crown and round ends; preserve the U opening.','Geometric paired curves; no useful neck-pillow reference.')
patch('playstation-vr','''
self.add_arc('headband',(5,27),(43,27),radius_x=19,radius_y=19)
self.add_bezier('visor-top-left',(4,32),((4,23),(15,21),(24,21)))
self.add_bezier('visor-top-right',(24,21),((33,21),(44,23),(44,32)))
self.add_bezier('visor-right',(44,32),((44,36),(43,40),(39,40)),((34,40),(30,38),(24,38)))
self.add_bezier('visor-left',(24,38),((18,38),(14,40),(9,40)),((5,40),(4,36),(4,32)))
self.add_contour('visor','visor-top-left','visor-top-right','visor-right','visor-left',closed=True)
self.relate('connect','headband','visor')
''','HRECT_L; symmetric visor, smooth top and bottom rails and a circular headband.','Geometric paired visor curves.')
patch('phone-with-starburst','''
self.add_bezier('outer-left',(4,35),((4,25),(13,23),(24,23)))
self.add_bezier('outer-right',(24,23),((35,23),(44,25),(44,35)))
self.add_arc('right-corner',(44,35),(39,40),radius_x=5)
self.add_line('right-end',(39,40),(36,40))
self.add_arc('right-inner',(36,40),(32,36),radius_x=4)
self.add_line('right-neck',(32,36),(32,33))
self.add_line('inner',(32,33),(16,33))
self.add_line('left-neck',(16,33),(16,36))
self.add_arc('left-inner',(16,36),(12,40),radius_x=4)
self.add_line('left-end',(12,40),(9,40))
self.add_arc('left-corner',(9,40),(4,35),radius_x=5)
self.add_contour('receiver','outer-left','outer-right','right-corner','right-end','right-inner','right-neck','inner','left-neck','left-inner','left-end','left-corner',closed=True)
self.add_line('ray-center',(24,8),(24,14))
for side in [-1,1]:self.add_line('ray-'+str(side),(24+side*13,10),(24+side*10,15))
''','HRECT_L; mirrored receiver ends and centered signal rays; smooth outer arch.','Geometric receiver construction.')
for id in ['refresh','refresh-interface-essential']:
 patch(id,'''
self.add_arc('lower',(42,24),(6,24),radius_x=18)
self.add_arc('upper-left',(6,24),(24,6),radius_x=18)
self.add_bezier('upper-right',(24,6),((31,6),(35,10),(40,16)))
self.add_contour('turn','lower','upper-left','upper-right')
self.add_polyline('head',(40,6),(40,16),(30,16))
self.relate('connect','head','turn')
''','SQUARE; continuous circular lower turn and smooth transition into arrowhead.','Lucide undo-2: circle-to-curve tangency.')
patch('rotation-y-axis','''
self.add_line('axis',(24,6),(24,42))
self.add_bezier('left-turn',(14,17),((9,18),(6,21),(6,24)),((6,30),(15,32),(24,32)))
self.add_bezier('right-turn',(24,32),((33,32),(42,30),(42,24)),((42,20),(38,17),(34,16)))
self.add_contour('rotation','left-turn','right-turn')
self.add_polyline('head',(40,15),(34,16),(35,22))
self.relate('connect','axis','rotation')
self.relate('connect','head','rotation')
''','SQUARE; centered axis and one smooth orbital sweep with intentional arrow gap.','Geometric ellipse-like orbit and clean attachment.')
patch('server-choose','''
# Three connected courses share their dividers, avoiding doubled strokes.
levels=(8,19,29,40)
for i,y in enumerate(levels):self.add_line(f'rail-{i}',(10,y),(38,y))
for side,mirror in [('left',False),('right',True)]:
    def p(x,y):return (48-x,y) if mirror else (x,y)
    for i,(t,b) in enumerate(zip(levels,levels[1:])):
        mid=(t+b)//2
        self.add_bezier(f'{side}-{i}',p(10,t),(p(6,t),p(4,t+2),p(4,mid)),(p(4,b-2),p(6,b),p(10,b)))
        self.relate('connect',f'{side}-{i}',f'rail-{i}')
        self.relate('connect',f'{side}-{i}',f'rail-{i+1}')
        if i:self.relate('connect',f'{side}-{i}',f'{side}-{i-1}')
''','HRECT_L; shared level rails and mirrored tangent rounded ends.','Geometric repeated capsule construction.')
patch('tracker-smartwatch',box+'''
box('face',8,13,40,35,4)
for name,mirror in [('top',False),('bottom',True)]:
    def p(x,y):return (x,48-y) if mirror else (x,y)
    self.add_line(name+'-left',p(14,13),p(14,8))
    self.add_arc(name+'-corner-left',p(14,8),p(18,4),radius_x=4,sweep=not mirror)
    self.add_line(name+'-end',p(18,4),p(30,4))
    self.add_arc(name+'-corner-right',p(30,4),p(34,8),radius_x=4,sweep=not mirror)
    self.add_line(name+'-right',p(34,8),p(34,13))
    self.add_contour(name,name+'-left',name+'-corner-left',name+'-end',name+'-corner-right',name+'-right')
    self.relate('connect',name,'face')
self.add_polyline('pulse',(8,24),(17,24),(22,19),(28,29),(33,24),(40,24))
self.relate('connect','pulse','face')
''','VRECT_L; one symmetric case, identical strap ends, waveform exactly attached to the case.','Geometric rounded rectangle and repeated straps.')
patch('undo','''
self.add_polyline('head',(8,4),(8,16),(18,16))
self.add_bezier('crest',(8,16),((12,11),(17,8),(23,8)),((33,8),(40,16),(40,27)))
self.add_bezier('lower',(40,27),((40,34),(36,41),(30,44)))
self.add_contour('turn','crest','lower')
self.relate('connect','head','turn')
''','VRECT_L; a few flowing curves and a clear right-angle arrowhead.','Lucide undo-2: coherent turning stroke.')
patch('warp-fish','''
self.add_bezier('upper-left',(4,24),((4,15),(10,8),(18,8)))
self.add_bezier('upper-neck',(18,8),((27,8),(28,20),(35,20)),((39,20),(42,16),(44,12)))
self.add_line('tail',(44,12),(44,36))
self.add_bezier('lower-neck',(44,36),((42,32),(39,28),(35,28)),((28,28),(27,40),(18,40)))
self.add_bezier('lower-left',(18,40),((10,40),(4,33),(4,24)))
self.add_contour('outline','upper-left','upper-neck','tail','lower-neck','lower-left',closed=True)
''','HRECT_L; mirrored neck and rounded left mass; preserve the fish warp silhouette.','Geometric mirrored cubic construction.')
patch('water-level','''
self.add_line('left',(4,8),(4,35))
self.add_arc('left-bottom',(4,35),(9,40),radius_x=5,sweep=False)
self.add_line('bottom',(9,40),(39,40))
self.add_arc('right-bottom',(39,40),(44,35),radius_x=5,sweep=False)
self.add_line('right',(44,35),(44,8))
self.add_contour('vessel','left','left-bottom','bottom','right-bottom','right')
for row,y in enumerate((14,25)):
    points=(4,17,31,44)
    for i,(a,b) in enumerate(zip(points,points[1:])):
        self.add_bezier(f'wave-{row}-{i}',(a,y),(((a+b)/2-2,y+5),((a+b)/2+2,y+5),(b,y)))
    self.add_contour(f'water-{row}',*(f'wave-{row}-{i}' for i in range(3)))
    self.relate('connect',f'water-{row}','vessel')
''','HRECT_L; repeated matching water scallops and identical base corners.','Geometric repeated wave construction.')
patch('wind-state','''
# One repeated wave definition owns the curve flow and line spacing.
for i,y in enumerate((8,21,34)):
    self.add_bezier(f'wave-{i}',(4,y+3),((8,y+1),(10,y),(14,y)),((22,y),(24,y+6),(34,y+6)),((39,y+6),(44,y+5),(44,y+1)))
''','HRECT_L; one coherent repeated wave with equal line spacing; retain directional lifted tips.','Geometric repeated cubic flow.')
# Rounded frame was visibly wavy on this vertical ellipsis.
patch('three-dots',box+"\nbox('frame',8,4,40,44,3)\nfor y in (13,24,35):self.add_dot('dot-'+str(y),(24,y))",'VRECT_L; straight parallel walls, matching corners and centered repeated dots.','Geometric rounded rectangle.')
save()
