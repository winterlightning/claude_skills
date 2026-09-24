from _author import *
# Each composition retains the supplied source identity through write().
design(1,'VRECT_L','Two bent electrical terminals with real cross arms over a rounded open-bottom housing; panel divided into two roomy cells.', '''
p('housing',(8,44),[('L',(8,22)),('A',(12,18),4,4,True),('L',(14,18)),('L',(30,18)),('L',(36,18)),('A',(40,22),4,4,True),('L',(40,44))])
for j,x in enumerate((20,36)):
 p(f'terminal-{j}',(x-6,18),[('L',(x-6,10)),('A',(x-2,6),4,4,True),('L',(x,6)),('L',(x+4,6))])
 p(f'cross-{j}',(x,4),[('L',(x,6)),('L',(x,10))])
 join(f'terminal-{j}',f'cross-{j}');join(f'terminal-{j}','housing')
p('panel',(17,35),[('L',(17,27)),('L',(31,27)),('L',(31,35)),('L',(31,44)),('L',(17,44)),('L',(17,35))],True)
line('division',(17,35),(31,35));join('division','panel')
''','Lucide smartphone: coherent rounded housing; no exact terminal match.','Inset panel reduced from three sections to two to maintain 8-unit centerline bands.')
design(3,'SQUARE','An open droplet at upper left and three elliptical blood cells. Keep oval cell silhouettes instead of the rejected circular substitutions.', '''
p('drop',(10,26),[('C',(6,20),(7,25),(6,23)),('C',(14,6),(6,15),(10,10)),('C',(21,15),(17,9),(20,12))])
oval('upper-cell',36,15,6,4)
oval('middle-cell',15,38,5,4)
oval('lower-cell',36,38,6,4)
''','Lucide droplet: continuous curved sides; open source boundary preserved.')
design(4,'SQUARE','Cloudberry with four rounded fruit regions and two spreading pointed leaves around a shared junction; retain center fruit rather than a generic cloud.', '''
p('center-fruit',(24,15),[('C',(31,26),(29,19),(31,22)),('C',(24,33),(31,29),(27,32)),('C',(17,26),(21,32),(17,29)),('C',(24,15),(17,22),(19,19))],True)
p('outer-fruit',(17,26),[('C',(9,18),(11,25),(9,22)),('C',(17,13),(9,12),(13,10)),('C',(24,6),(17,8),(20,6)),('C',(31,13),(28,6),(31,8)),('C',(39,18),(35,10),(39,12)),('C',(31,26),(39,22),(37,25))])
join('center-fruit','outer-fruit')
for side in (-1,1):
 m=lambda x,y:(24+side*x,y)
 p('leaf-'+str(side),m(0,33),[('C',m(18,24),m(8,32),m(15,29)),('C',m(0,33),m(18,42),m(7,43))],True)
 join('leaf-'+str(side),'center-fruit')
join('leaf--1','leaf-1')
line('stem',(24,33),(24,42))
for n in ('center-fruit','leaf--1','leaf-1'):join('stem',n)
''','Lucide grape: a small set of legible fruit regions; leaf shape from supplied original.')
design(6,'SQUARE','A right-facing crested chicken with elongated neck, scooped back, rounded belly and visible beak; keep the foot as a distinct extension.', '''
p('body',(12,25),[('C',(23,23),(20,28),(23,27)),('L',(23,16)),('A',(30,9),7,7,True),('A',(37,16),7,7,True),('C',(42,23),(40,17),(42,20)),('L',(37,23)),('L',(37,26)),('C',(25,36),(37,32),(32,36)),('C',(12,25),(18,36),(12,31))],True)
p('tail',(6,21),[('L',(9,21)),('C',(12,25),(12,21),(12,23))]);join('tail','body')
p('crest',(25,6),[('C',(30,9),(28,6),(30,7))]);join('crest','body')
line('leg',(25,36),(25,42));join('leg','body')
''','Lucide bird: circular head, curved belly and deliberate beak attachment.')
design(7,'HRECT_L','A side-profile face beside an upright phone, with smooth forehead, nose and rounded mouth hollow; straight left cut indicates a cropped head.', '''
p('face',(4,40),[('L',(4,8)),('L',(7,8)),('C',(14,13),(10,8),(12,9)),('L',(21,25)),('C',(15,30),(17,26),(15,27)),('C',(19,36),(15,34),(16,35)),('C',(17,40),(21,38),(20,40)),('L',(4,40))],True)
p('phone',(33,12),[('L',(40,12)),('A',(44,16),4,4,True),('L',(44,31)),('L',(44,36)),('A',(40,40),4,4,True),('L',(33,40)),('A',(29,36),4,4,True),('L',(29,31)),('L',(29,16)),('A',(33,12),4,4,True)],True)
line('screen-edge',(29,31),(44,31));join('screen-edge','phone')
''','Lucide smartphone: rounded housing; human user.svg and full_body_ref.png inform smooth human curves. Cropped continuous profile has no detached head.','Omit the short eye stroke to keep the narrow facial region clear.')
design(8,'VRECT_L','Cropped pregnant torso with a smooth protruding belly and a resting bent arm. Shared hand/back attachment; retain natural directional asymmetry.', '''
p('belly',(18,4),[('C',(18,12),(14,7),(14,9)),('C',(8,28),(12,16),(8,21)),('C',(18,40),(8,35),(12,39)),('L',(18,44))])
p('arm',(30,4),[('C',(26,17),(30,9),(29,13)),('L',(20,23)),('C',(23,31),(15,27),(18,31)),('C',(36,22),(30,31),(34,26))])
p('back',(40,4),[('C',(36,22),(40,11),(39,17)),('C',(40,44),(36,30),(38,38))]);join('arm','back')
''','Human user.svg and full_body_ref.png: coherent torso and curved limbs. Cropped torso has no head, so no detached-head gap applies.','Fingers omitted; preserve the broad resting hand.')
design(9,'SQUARE','Japanese hiragana a (あ): three coherent pen strokes with an upright crossing bar and a flowing loop. Split real intersections at shared integer nodes.', '''
p('top-bar',(6,12),[('L',(19,12)),('L',(42,12))])
p('stem',(19,6),[('L',(19,12)),('L',(19,23)),('C',(20,35),(19,28),(19,32)),('C',(24,42),(21,38),(22,40))])
p('loop',(32,18),[('C',(20,35),(30,24),(25,31)),('C',(7,39),(15,40),(10,42)),('C',(6,34),(6,38),(6,36)),('C',(19,23),(6,29),(12,24)),('C',(29,22),(22,22),(25,22)),('C',(42,32),(37,22),(42,26)),('C',(32,42),(42,38),(38,41))])
join('top-bar','stem');join('loop','stem')
''','No useful Lucide glyph match; preserve the three source pen strokes.','None; crossings are deliberate parts of the character.')
design(10,'SQUARE','Three open ring nodes with a diagonal inward arrow and a flowing lower U connection. Enlarge nodes and align arrow shaft on a true diagonal.', '''
for n,x,y in [('source',10,10),('upper',36,10),('lower',10,29)]:oval(n,x,y,4,4)
p('arrow',(14,10),[('L',(28,26))])
poly('arrow-head',(22,26),(28,26),(28,20));join('arrow','arrow-head');join('arrow','source')
p('loop',(36,14),[('C',(42,26),(40,17),(42,21)),('C',(27,42),(42,37),(37,42)),('C',(10,33),(19,42),(10,39))]);join('loop','upper');join('loop','lower')
''','Lucide settings circular outline principle; source determines node and arrow arrangement.')
design(16,'HRECT_L','Low whale with smooth back, rising tail, two flukes and a pectoral fin; water spout grows from the back. Preserve horizontal animal proportions.', '''
p('body',(4,29),[('C',(15,25),(5,26),(10,25)),('L',(20,25)),('L',(32,25)),('C',(36,21),(35,25),(36,24)),('C',(30,19),(36,19),(33,18)),('C',(38,15),(31,12),(35,13)),('C',(44,8),(38,10),(40,8)),('L',(44,25)),('C',(35,36),(44,30),(40,34)),('L',(37,40)),('C',(28,38),(33,40),(30,39)),('C',(4,29),(18,41),(7,35))],True)
p('fin',(25,31),[('L',(28,38))]);join('fin','body')
p('spout-left',(10,10),[('C',(20,17),(12,6),(18,8))])
p('spout-right',(20,17),[('C',(30,10),(22,8),(28,6))]);join('spout-left','spout-right')
line('spout-stem',(20,17),(20,25));join('spout-stem','spout-left');join('spout-stem','spout-right');join('spout-stem','body')
''','Lucide bird: coherent animal silhouette; source supplies whale tail and spout.','Omit the fine internal lower belly line to preserve open space.')
design(17,'SQUARE','Triceratops profile with large rounded frill, two visible horns, hooked beak and a short neck; remove polygonal kinks from the face and frill.', '''
p('head',(31,6),[('C',(42,23),(38,10),(42,17)),('C',(28,37),(42,31),(36,37)),('C',(14,35),(22,37),(18,35)),('L',(7,32)),('L',(12,28)),('L',(6,28)),('C',(9,21),(6,25),(7,22)),('C',(7,12),(7,18),(6,15)),('C',(15,21),(9,17),(12,20)),('L',(26,21)),('C',(22,7),(26,15),(25,11)),('C',(32,21),(28,10),(31,15)),('C',(31,6),(36,20),(31,14))],True)
p('neck',(28,37),[('C',(35,42),(29,39),(32,41))]);join('neck','head')
''','Lucide bird: coherent curved animal contour; no useful dinosaur match.','Omit the added eye absent from the original; keep horn and frill silhouette.')
if __name__=='__main__':write()
