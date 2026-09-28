from _author import *
design(0,'SQUARE','Mirrored pointed crab claws above a broad curved carapace, with paired raised arms and two pairs of splayed legs.', '''
p('shell',(12,27),[('C',(24,23),(16,23),(20,23)),('C',(36,27),(28,23),(32,23)),('C',(33,35),(36,30),(35,33)),('C',(24,42),(30,39),(27,42)),('C',(15,35),(21,42),(18,39)),('C',(12,27),(13,33),(12,30))],True)
for side in (-1,1):
 m=lambda x,y:(24+side*x,y)
 p('claw-'+str(side),m(9,6),[('C',m(18,12),m(14,6),m(18,8)),('C',m(13,17),m(18,16),m(16,17)),('C',m(6,12),m(9,17),m(7,14)),('L',m(10,12)),('L',m(6,8)),('C',m(9,6),m(6,7),m(7,6))],True)
 p('arm-'+str(side),m(13,17),[('C',m(12,27),m(13,22),m(13,24))]);join('arm-'+str(side),'claw-'+str(side));join('arm-'+str(side),'shell')
 line('upper-leg-'+str(side),m(12,27),m(18,32));line('lower-leg-'+str(side),m(9,35),m(18,42))
 join('upper-leg-'+str(side),'shell');join('upper-leg-'+str(side),'arm-'+str(side));join('lower-leg-'+str(side),'shell')
''','No useful Lucide crab match; mirrored coherent contour construction.','Reduce three leg pairs to two, preserving large claws and the tapered shell.')
design(1,'SQUARE','Copper IUD with mirrored curled arms, a banded stem, and a visible terminal ring on a short thread.', '''
for side in (-1,1):
 m=lambda x,y:(24+side*x,y)
 p('arm-'+str(side),m(12,17),[('C',m(18,12),m(17,17),m(18,15)),('C',m(12,6),m(18,8),m(16,6)),('C',(24,14),m(6,6),m(3,8))])
p('stem',(20,16),[('A',(22,14),2,2,True),('L',(24,14)),('L',(26,14)),('A',(28,16),2,2,True),('L',(28,22)),('L',(28,28)),('A',(26,30),2,2,True),('L',(24,30)),('L',(22,30)),('A',(20,28),2,2,True),('L',(20,22)),('L',(20,16))],True)
line('band',(20,22),(28,22));join('band','stem');join('arm--1','stem');join('arm-1','stem');join('arm--1','arm-1')
p('terminal',(24,36),[('A',(24,42),3,3,True),('A',(24,36),3,3,True)],True)
line('thread',(24,30),(24,36));join('thread','stem');join('thread','terminal')
''','No exact Lucide IUD match; paired smooth curls and round terminal from the supplied reference.','Reduce two stem bands to one for clean 8-unit spacing.')
design(2,'VRECT_L','Symmetric tapered glue bottle with a distinct cap collar, smoothly rounded base and a tapered rounded nozzle.', '''
p('body',(14,22),[('L',(34,22)),('C',(37,26),(36,22),(37,24)),('L',(40,38)),('A',(34,44),6,6,True),('L',(14,44)),('A',(8,38),6,6,True),('L',(11,26)),('C',(14,22),(11,24),(12,22))],True)
p('collar',(14,22),[('L',(14,14)),('L',(18,14)),('L',(30,14)),('L',(34,14)),('L',(34,22))]);join('collar','body')
p('nozzle',(18,14),[('L',(21,6)),('C',(24,4),(22,4),(23,4)),('C',(27,6),(25,4),(26,4)),('L',(30,14))]);join('nozzle','collar')
''','Lucide milk: a continuous bottle silhouette with deliberately joined cap sections.')
design(3,'SQUARE','Three-lobed squash with a full-height central oval rib and smooth paired outer lobes, replacing disconnected short marks.', '''
p('center',(24,12),[('A',(24,42),9,15,True),('A',(24,12),9,15,True)],True)
p('outside',(24,12),[('C',(6,25),(12,7),(6,15)),('C',(24,42),(6,38),(15,42)),('C',(42,25),(33,42),(42,38)),('C',(24,12),(42,15),(36,7))],True);join('center','outside')
p('stem',(24,12),[('C',(28,6),(24,8),(25,6))]);join('stem','center');join('stem','outside')
''','Lucide apple: coherent organic silhouette and curved attached stem.')
design(4,'VRECT_L','Man head and shoulders as a single smooth open outline with a continuous neck, circular jaw arcs and rounded shoulder sweeps.', '''
p('portrait',(8,44),[('C',(12,36),(8,40),(9,38)),('L',(20,32)),('L',(20,28)),('A',(14,16),14,14,True),('A',(34,16),10,12,True),('A',(28,28),14,14,True),('L',(28,32)),('L',(36,36)),('C',(40,44),(39,38),(40,40))])
''','Human user.svg and full_body_ref.png: smooth head/shoulder construction. The original has a continuous neck, not a detached head.','Omit tiny ear bumps; preserve the uninterrupted neck and open shoulder baseline.')
design(5,'VRECT_L','Woman portrait with a smooth circular jaw, center-parted fringe, bobbed hair and broad curved shoulders. Preserve the naturally connected neck.', '''
p('face',(16,18),[('C',(24,13),(19,17),(22,15)),('C',(32,18),(26,15),(29,17)),('A',(24,26),8,8,True),('A',(16,18),8,8,True)],True)
p('hair',(12,29),[('C',(8,28),(10,29),(9,29)),('L',(10,18)),('C',(24,4),(10,9),(16,4)),('C',(38,18),(32,4),(38,9)),('L',(40,28)),('C',(36,29),(39,29),(38,29))])
p('shoulders',(8,44),[('C',(14,35),(8,39),(10,36)),('L',(20,32)),('L',(20,25))])
p('shoulders-right',(28,25),[('L',(28,32)),('L',(34,35)),('C',(40,44),(38,36),(40,39))])
join('shoulders','face');join('shoulders-right','face')
''','Human user.svg and full_body_ref.png: rounded jaw and paired shoulders, with natural continuous neck from the source.','No facial microdetail; hair tips separated from the shoulders.')
design(6,'VRECT_L','Long-haired woman with a center-parted fringe and round lower face, neck, and broad closed bust; retain recognizable hairstyle rather than a circle inside an arch.', '''
p('face',(16,18),[('C',(24,13),(20,17),(23,15)),('C',(32,18),(25,15),(28,17)),('A',(24,26),8,8,True),('A',(16,18),8,8,True)],True)
p('hair',(12,31),[('L',(8,31)),('L',(10,18)),('C',(24,4),(10,9),(16,4)),('C',(38,18),(32,4),(38,9)),('L',(40,31)),('L',(36,31))])
p('bust',(20,25),[('L',(20,33)),('C',(8,42),(14,35),(8,36)),('L',(8,44)),('L',(40,44)),('L',(40,42)),('C',(28,33),(40,36),(34,35)),('L',(28,25))]);join('bust','face')
''','Human user.svg and full_body_ref.png: circular jaw and smooth shoulder curvature; source has an attached anatomical neck.')
design(7,'SQUARE','Two diagonally arranged hearts with smooth lobes and coherent tapered sides. Restore the larger heart upper-right lobe and preserve the small upper-right heart.', '''
p('large',(18,24),[('C',(12,19),(16,21),(15,19)),('C',(6,25),(8,19),(6,21)),('C',(18,42),(6,31),(12,37)),('C',(30,29),(25,36),(30,32))])
p('large-right-lobe',(18,24),[('C',(23,19),(20,20),(22,19))]);join('large','large-right-lobe')
p('small',(33,10),[('C',(28,6),(31,7),(30,6)),('C',(24,11),(25,6),(24,8)),('C',(33,22),(24,14),(28,18)),('C',(42,11),(38,18),(42,14)),('C',(38,6),(42,8),(41,6)),('C',(33,10),(36,6),(35,7))],True)
''','Lucide heart: smooth lobes flowing into tapered sides.','The large upper-right edge remains partially occluded behind the smaller heart; no detached hook substituted.')
design(8,'VRECT_L','Seven pointed cannabis lobes around a tall narrow center leaflet. Mirror tapered curves while retaining deliberate sharp valleys and a short stem.', '''
self.mirror('leaf',(24,4),[('C',(27,24),(29,12),(29,18)),('C',(38,14),(31,19),(35,15)),('C',(31,29),(38,21),(34,26)),('C',(40,32),(35,29),(38,30)),('C',(30,35),(37,35),(33,36)),('C',(32,41),(31,37),(32,39)),('C',(24,37),(28,41),(26,39))])
line('stem',(24,37),(24,44));join('stem','leaf')
''','Lucide cannabis: seven coherent pointed lobes; taller central leaflet preserves the original proportions.')
# Additional designs appended as references finish staging.
for i,closed in ((5,False),(6,True)):
 key,plan,body,ref,omit=D[i]
 body='''
p('face',(14,20),[('C',(24,16),(18,19),(22,17)),('C',(34,20),(26,17),(30,19)),('A',(30,28),10,10,True),('A',(18,28),10,10,True),('A',(14,20),10,10,True)],True)
p('hair',(6,26),[('L',(6,20)),('A',(24,6),18,14,True),('A',(42,20),18,14,True),('L',(42,26))])
p('left-neck',(18,28),[('L',(18,34)),('C',(6,42),(12,36),(6,36))]);join('left-neck','face')
p('right-neck',(30,28),[('L',(30,34)),('C',(42,42),(36,36),(42,36))]);join('right-neck','face')
'''
 if closed:body += "line('base',(6,42),(42,42));join('base','left-neck');join('base','right-neck')\n"
 design(i,'SQUARE',plan,body,ref,omit)
key,plan,_,ref,omit=D[7]
design(7,key,plan, '''
p('large',(27,19),[('C',(18,24),(23,17),(20,19)),('C',(12,19),(16,21),(15,19)),('C',(6,25),(8,19),(6,21)),('C',(18,42),(6,31),(12,37)),('C',(30,22),(26,35),(32,27))])
p('small',(33,10),[('C',(28,6),(31,7),(30,6)),('C',(24,11),(25,6),(24,8)),('C',(27,19),(24,14),(25,17)),('L',(30,22)),('L',(33,25)),('C',(42,11),(38,20),(42,15)),('C',(38,6),(42,8),(41,6)),('C',(33,10),(36,6),(35,7))],True)
join('large','small')
''',ref,'The large heart edge is occluded between two shared points on the smaller heart.')
design(9,'SQUARE','Four circular proton/network nodes linked by three diagonal bonds; restore circular nodes and explicit shared attachment points.', '''
def ring(n,x,y,r,extras=()):
 import math
 points=[(x,y-r),(x+r,y),(x,y+r),(x-r,y)]+list(extras)
 points.sort(key=lambda q:math.atan2(q[1]-y,q[0]-x))
 p(n,points[0],[('A',q,r,r,True) for q in points[1:]+points[:1]],True)
ring('center',24,25,5,((21,21),(20,28),(28,22)))
ring('upper',11,11,5,((14,15),))
ring('lower',10,37,5,((14,34),))
ring('right',38,14,4)
for n,a,b,outer in [('up',(14,15),(21,21),'upper'),('down',(20,28),(14,34),'lower'),('right-bond',(28,22),(34,14),'right')]:
 line(n,a,b);join(n,'center');join(n,outer)
''','Lucide disc-3: circular construction, with source arrangement and bond directions.')
design(10,'SQUARE','An exact symmetric diamond divided horizontally at its widest points; remove small off-grid jogs and the uneven top seam.', '''
poly('diamond',(6,24),(24,6),(42,24),(24,42),closed=True)
line('divider',(6,24),(42,24));join('divider','diamond')
''','No useful exact Lucide rate symbol; use a shared center and equal diamond diagonals.')
design(11,'SQUARE','Turntable with a rounded square deck, circular platter, and diagonal tonearm. Consistent corner radii replace flattened elliptical deck corners.', '''
p('deck',(10,6),[('L',(38,6)),('A',(42,10),4,4,True),('L',(42,38)),('A',(38,42),4,4,True),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,10)),('A',(10,6),4,4,True)],True)
p('platter',(24,14),[('A',(34,24),10,10,True),('A',(24,34),10,10,True),('A',(18,32),10,10,True),('A',(14,24),10,10,True),('A',(24,14),10,10,True)],True)
poly('tonearm',(24,24),(18,32),(16,34));join('tonearm','platter')
''','Lucide disc-3: circular platter; Lucide smartphone: consistent rounded housing corners.','Spindle reduced to tonearm endpoint; omit tiny lower-right indicator to keep the deck clear.')
design(12,'VRECT_L','Redo arrow made from two tangent quarter-circle arcs and one smooth shoulder, with a right-angle arrowhead.', '''
p('sweep',(26,44),[('A',(8,26),18,18,True),('A',(26,8),18,18,True),('C',(40,14),(32,8),(36,10))])
poly('arrowhead',(40,4),(40,14),(30,14));join('arrowhead','sweep')
''','Lucide redo: coherent curved shaft with an explicit arrowhead junction.')
design(13,'HRECT_M','Low roadster with two equal wheels, rounded hood and a broader triangular windscreen; wheel rims remain uninterrupted at body joins.', '''
for n,x in [('rear',12),('front',36)]:oval(n,x,32,6,6)
p('body',(6,32),[('L',(4,32)),('L',(4,26)),('A',(9,21),5,5,True),('L',(20,21)),('L',(34,21)),('C',(44,29),(39,21),(44,25)),('L',(44,32)),('L',(42,32))])
line('chassis',(18,32),(30,32))
for n in ('rear','front'):join('body',n);join('chassis',n)
poly('windscreen',(20,21),(16,10),(34,21));join('windscreen','body')
''','Lucide car (inspected in prior batch): coherent side body and shared wheel attachment nodes.')
design(14,'SQUARE','A rising chart with two smooth dips; use a few coherent cubic curves instead of compressed short arc fragments.', '''
p('axes',(6,6),[('L',(6,38)),('A',(10,42),4,4,False),('L',(42,42))])
p('data',(15,33),[('C',(22,23),(18,28),(19,19)),('C',(27,28),(24,24),(25,28)),('C',(35,14),(30,28),(30,14)),('C',(40,21),(37,14),(38,21)),('C',(42,18),(41,21),(42,20))])
''','Lucide chart-line: sparse readable axes; the source requires a smooth data curve.')
design(15,'SQUARE','Sputnik satellite with an exact circular body and three long antenna rods attached at integer points on that circle.', '''
p('sphere',(29,6),[('A',(42,19),13,13,True),('A',(41,24),13,13,True),('A',(29,32),13,13,True),('A',(17,24),13,13,True),('A',(16,19),13,13,True),('A',(24,7),13,13,True),('A',(29,6),13,13,True)],True)
for n,a,b in [('upper',(6,14),(24,7)),('lower-left',(6,42),(17,24)),('lower-right',(36,42),(41,24))]:
 line(n,a,b);join(n,'sphere')
''','Lucide satellite: coherent body/antenna attachments; source determines spherical Sputnik body and unequal directional rods.')
design(16,'VRECT_L','Stomach outline with a broad smooth gastric sac, a narrowed upper tube and an open lower outlet; replace abrupt elbow-like contours.', '''
p('inner',(16,4),[('L',(16,12)),('C',(20,22),(16,17),(18,19)),('C',(12,30),(20,28),(16,29)),('C',(8,38),(8,31),(8,35)),('L',(8,44))])
p('outer',(26,4),[('L',(26,10)),('C',(30,14),(26,14),(28,15)),('C',(40,24),(36,12),(40,18)),('C',(26,40),(40,34),(34,40)),('C',(21,38),(23,40),(23,39)),('C',(17,40),(18,36),(17,37)),('L',(17,44))])
''','No useful Lucide stomach match; source supplies anatomy, with long coherent tangent curves.')
design(17,'SQUARE','Two rotationally matched synchronization arrows, each a smooth broad arc ending in an open right-angle head.', '''
for j,flip in enumerate((False,True)):
 m=lambda q:(48-q[0],48-q[1]) if flip else q
 p('arc-'+str(j),m((6,26)),[('A',m((24,6)),18,20,True),('C',m((40,14)),m((31,6)),m((36,9)))])
 poly('head-'+str(j),m((38,6)),m((40,14)),m((32,14)));join('head-'+str(j),'arc-'+str(j))
''','Lucide refresh-cw: rotationally matched smooth arcs and clear open arrowheads.')
design(18,'SQUARE','Circular synchronization arrows with a diagonal magnifying handle; use a circular lower-right arc and an exact handle attachment point.', '''
p('left-arc',(22,6),[('A',(7,21),15,15,False),('A',(10,30),15,15,False)])
poly('left-head',(10,22),(10,30),(6,30));join('left-head','left-arc')
p('right-arc',(34,12),[('A',(37,21),15,15,True),('A',(31,33),15,15,True),('A',(22,36),15,15,True)])
poly('right-head',(34,20),(34,12),(42,12));join('right-head','right-arc')
line('handle',(31,33),(42,42));join('handle','right-arc')
''','Lucide refresh-cw and search: smooth circular arrows and a handle with a true shared node.')
design(19,'SQUARE','Three matched pointed droplets arranged in a triangle; smoothly curved shoulders meet round lower bowls without kinks.', '''
for n,x,t in [('top',24,6),('left',12,26),('right',36,26)]:
 p(n,(x,t),[('C',(x+6,t+10),(x+2,t+3),(x+6,t+7)),('A',(x,t+16),6,6,True),('A',(x-6,t+10),6,6,True),('C',(x,t),(x-6,t+7),(x-2,t+3))],True)
''','Lucide droplet (inspected in prior batch): curved sides tangent to the lower circular bowl; one repeated shape owns all drops.')
# Increase portrait hair clearance without changing the circular lower jaw.
for i in (5,6):
 key,plan,body,ref,omit=D[i]
 body=body.replace("('L',(6,20)),('A',(24,6),18,14,True),('A',(42,20),18,14,True)","('L',(6,16)),('A',(24,6),18,10,True),('A',(42,16),18,10,True)")
 # The outer head is wider at the jaw's side extrema; crown reaches the exact top edge.
 design(i,key,plan,body,ref,omit)
key,plan,body,ref,omit=D[9]
body=body.replace("ring('lower',10,37,5,((14,34),))","ring('lower',11,37,5,((15,34),))").replace("(14,34),'lower'","(15,34),'lower'")
design(9,key,plan,body,ref,omit)
for i in (5,6):
 key,plan,body,ref,omit=D[i]
 start=body.index("p('face'");end=body.index("p('left-neck'",start)
 stop=28 if i==6 else 26
 body=body[:start]+f"""p('face',(16,26),[('C',(16,20),(15,24),(16,22)),('C',(24,15),(19,18),(22,17)),('C',(32,20),(26,17),(29,18)),('C',(32,26),(32,22),(33,24)),('A',(30,28),10,10,True),('A',(18,28),10,10,True),('A',(16,26),10,10,True)],True)
p('hair',(6,{stop}),[('L',(6,20)),('A',(24,6),18,14,True),('A',(42,20),18,14,True),('L',(42,{stop}))])
"""+body[end:]
 design(i,key,plan,body,ref,omit)
key,plan,body,ref,omit=D[11]
start=body.index("p('deck'");end=body.index("p('platter'",start)
body=body[:start]+"poly('deck',(6,6),(42,6),(42,42),(6,42),closed=True)\n"+body[end:]
design(11,key,'Turntable with a square deck, circular platter and diagonal tonearm. Equal edges and round stroke joins replace flattened elliptical corners.',body,ref,omit)
key,plan,body,ref,omit=D[11]
body='''
p('deck',(10,6),[('L',(38,6)),('A',(42,10),4,4,True),('L',(42,38)),('A',(38,42),4,4,True),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,10)),('A',(10,6),4,4,True)],True)
oval('platter',24,24,9,9)
# The source tonearm crosses the platter rim, rather than ending at it.
# Length sqrt(8^2+9^2)>9 proves a real rim intersection on this ray.
line('tonearm',(24,24),(16,33));join('tonearm','platter')
'''
design(11,key,'Turntable with a rounded deck, circular platter and diagonal tonearm crossing the rim, as in the reference. Preserve 9-unit clearance between platter and deck.',body,ref,omit)
if __name__=='__main__':write()
