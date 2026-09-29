from author_more import *
# Refine symmetry and literal junctions in fresh runs.
for i in (4,5):
 SPECS[i]['body']=SPECS[i]['body'].replace("((34,39),(33,36),(32,34))","((34,40),(33,44-12),(32,34))") if False else SPECS[i]['body']
 # Bottom half mirrors the top exactly around y=24.
 SPECS[i]['body']="""curve(self,'handset',(26,4),((18,4),(14,14),(14,24)),((14,34),(18,44),(26,44)),((31,44),(34,44),(34,41)),((34,40),(33,36),(32,34)),((31,31),(28,34),(26,31)),((23,28),(23,20),(26,17)),((28,14),(31,17),(32,14)),((33,12),(34,8),(34,7)),((34,4),(31,4),(26,4)),closed=True)"""
SPECS[6]['exception']='Exact 4-unit ink clearance between the straight liquid column and tube; preserve the analytical 8-unit centerline gap despite the curved-contour certification warning.'
SPECS[18]['body']=SPECS[18]['body'].replace('(14,34),(24,14),(34,14),(24,34)','(14,33),(24,15),(34,15),(24,33)')
SPECS[9]['body']=SPECS[9]['body'].replace("self.add_polyline('pac-mouth',(22,21),(16,15),(22,9));", "self.add_line('pac-mouth-1',(22,21),(16,15));self.add_line('pac-mouth-2',(16,15),(22,9));").replace('(44,24),(38,29)','(44,24),(37,30)')
# Drone rotor shafts meet exactly at the body's upper ends; pod attaches at lower silhouette points.
SPECS[2]['body']=SPECS[2]['body'].replace('(9,39)','(4,44)').replace('(x-4,16),(x+4,16)','(max(4,x-4),16),(min(44,x+4),16)')
SPECS[2]['body']=SPECS[2]['body'].replace("(15,34),((15,37),(15,42),(19,42)),((22,42),(26,42),(29,42)),((33,42),(33,37),(33,34))", "(4,31),((10,31),(14,35),(14,39)),((14,44),(34,44),(34,39)),((34,35),(38,31),(44,31))")

define(13,'VRECT_M','The rejected figure has a tiny head and an exaggerated wide stride; its straight angular arms read as running.','Restored a proportionate circular head, gently leaning torso, relaxed opposite arm swing and natural walking step.', '''
# Human reference: full_body_ref.png. Head r5; junction (27,22): 22-(9+5)=8 centerline, 4 ink.
circle(self,'head',27,9,5)
curve(self,'torso',(27,22),((27,27),(23,29),(23,32)))
self.add_polyline('back-arm',(27,22),(20,25),(15,33))
self.add_polyline('front-arm',(27,22),(32,28),(37,31))
self.add_line('rear-leg',(23,32),(13,44))
self.add_polyline('front-leg',(23,32),(31,43),(35,43))
for part in ('back-arm','front-arm','rear-leg','front-leg'):self.relate('connect','torso',part)
self.relate('connect','back-arm','front-arm');self.relate('connect','rear-leg','front-leg')
self.mark_human_figure('person',head='head',torso='torso-curve',torso_junction='start')
''','human_ref/full_body_ref.png: circular outlined head and coherent round-ended torso/limbs','A relaxed walking pose has a narrower natural envelope than the prescribed rectangle. Preserve 4px human strokes and the exact 4px detached head gap.')

define(14,'VRECT_M','A tiny head, disconnected-looking diagonal trunk and squat stance obscure the upright raised-arm warrior pose.','Restored the upright raised arm, proportionate head, curved torso and a long rear leg with bent forward knee.', '''
# Human reference: full_body_ref.png. (23,22)-(18,10)=(5,12); distance13 minus r5=8 centerline gap.
circle(self,'head',18,10,5)
curve(self,'torso',(23,22),((25,27),(24,29),(24,31)))
self.add_polyline('raised-arm',(23,22),(32,22),(32,4))
self.add_line('rear-leg',(24,31),(10,44))
self.add_polyline('front-leg',(24,31),(36,34),(38,44))
self.relate('connect','torso','raised-arm','rear-leg','front-leg')
self.mark_human_figure('person',head='head',torso='torso-curve',torso_junction='start')
''','human_ref/full_body_ref.png: head proportion, round-ended limbs; supplied original: raised arm and lunge','The analytically exact head-to-torso gap is 4px (5-12-13 triangle, r5 head); preserve the pose and its curve-distance advisory rather than distorting the head placement.')

define(15,'SQUARE','A cross replaced the sun and the detached cloud and pin no longer overlap as a weather-location composition.','Restored a round sun behind a cloud with a foreground location pin and clear circular pin opening.', '''
# Sun rays are three short radial strokes; the disk is partially covered by the cloud.
self.add_arc('sun',(10,23),(23,12),radius_x=9,large_arc=True)
self.add_line('ray-top',(14,3),(14,5))
self.add_line('ray-left',(3,15),(5,15))
self.add_line('ray-diagonal',(5,6),(7,8))
curve(self,'cloud',(23,37),((17,37),(8,38),(6,32)),((2,26),(8,20),(14,21)),((16,11),(29,10),(33,20)),((38,20),(42,22),(43,27)))
# Foreground pin interrupts the cloud; a deliberate occlusion, not spurious contact.
curve(self,'pin',(35,44),((31,39),(26,34),(26,30)),((26,18),(44,18),(44,30)),((44,34),(39,39),(35,44)),closed=True)
circle(self,'pin-hole',35,29,3)
''','cloud-sun: overlapping disk/cloud lobes and short rays; original supplies foreground location pin','Keep the sun/cloud/pin overlap and the circular marker opening at 48px. Compact foreground spacing is needed for the complete weather-location composition.')

define(16,'SQUARE','The wheelchair body and arm merged into a heavy block and the flag looked like a rectangular loop.','Separated the seated figure from its wheel and restored an outstretched hand holding a gently waving flag.', '''
# Shared human reference: circular r5 head and exact 4px gap at torso junction y23.
circle(self,'head',17,10,5)
self.add_line('torso',(17,23),(17,31))
self.add_polyline('leg',(17,31),(28,31),(37,43))
self.add_line('arm',(17,23),(34,23))
self.relate('connect','torso','leg','arm')
curve(self,'wheel',(9,25),((2,28),(3,39),(10,43)),((17,47),(27,42),(27,35)))
self.add_line('flagpole',(34,4),(34,27))
curve(self,'flag',(34,4),((38,7),(41,1),(44,4)),((44,7),(44,11),(44,14)),((40,11),(38,17),(34,14)))
self.relate('connect','flagpole','flag');self.relate('connect','flagpole','arm')
self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
''','human_ref/full_body_ref.png: head/torso proportions; accessibility: open rear wheel and seated leg','Retain a seated person, separate visible wheel and waving flag in one 48px scene. Compact wheel/body spacing is visually clear; the detached head gap stays exactly 4px.')

define(17,'SQUARE','The seal became a ghost-like bell with a nose dot; its tail and paired flippers disappeared.','Restored the smooth seal body, curled side tail, two outward flippers and paired whiskers; omitted facial detail absent from the original.', '''
# One curved animal body; the front flippers and rear tail remain separate readable lobes.
curve(self,'body',(14,16),((12,3),(34,2),(34,16)),((34,25),(37,34),(43,40)),((44,44),(35,43),(31,39)),((26,44),(18,44),(13,39)),((9,44),(3,44),(5,40)),((11,34),(13,25),(14,16)),closed=True)
curve(self,'left-flipper',(13,39),((17,36),(18,33),(18,31)))
curve(self,'right-flipper',(31,39),((27,36),(26,33),(26,31)))
self.relate('connect','body','left-flipper');self.relate('connect','body','right-flipper')
self.add_polyline('tail',(7,36),(3,27),(8,28),(10,23),(12,29))
self.relate('connect','tail','body')
for name,a,b in [('left-top',(14,18),(7,16)),('left-low',(13,22),(6,24)),('right-top',(34,18),(41,16)),('right-low',(35,22),(42,24))]:
    self.add_line(name,a,b)
    self.relate('connect','body',name)
''','No useful Lucide seal match; use coherent smooth contours and the supplied reference silhouette.','The seal needs both front flippers, a side tail and two whiskers on each side. Preserve these compact attached features with fixed 4px strokes.')

define(19,'SQUARE','Circular rings replaced the earbuds and the charging lightning symbol became a dot.','Restored shaped earbud heads with stems entering the case and an explicit lightning bolt on the case.', '''
# Mirrored earbud housings retain their downward stems; shared geometry maintains equal proportions.
for side in (-1,1):
    def p(x,y):return (24+side*x,y)
    curve(self,'earbud-'+str(side),p(4,24),(p(4,20),p(4,13),p(4,11)),(p(4,1),p(20,1),p(20,10)),(p(20,15),p(14,16),p(10,14)),(p(10,18),p(10,21),p(10,24)))
# The stems join the case rim; rounded lower corners give a familiar charging case silhouette.
self.add_line('rim',(6,24),(42,24))
curve(self,'case',(42,24),((42,28),(42,34),(42,37)),((42,44),(35,44),(31,44)),((27,44),(21,44),(17,44)),((13,44),(6,44),(6,37)),((6,34),(6,28),(6,24)))
self.relate('connect','rim','case')
for side in (-1,1):self.relate('connect','rim','earbud-'+str(side))
self.add_polyline('charge',(25,29),(19,36),(24,36),(23,41),(30,33),(25,33),closed=True)
''','ear: smooth earbud lobes; original: paired stems, rounded case and central lightning bolt','A recognizable charging case needs its lightning bolt and shaped earbuds. Preserve compact bolt counter and stem spacing, all at 4px stroke.')

if __name__=='__main__':
 for i in map(int,sys.argv[1:]):write(i,'03' if i in (4,5,6,18) else '02' if i in (2,3,8,9,10,11) else '01')
