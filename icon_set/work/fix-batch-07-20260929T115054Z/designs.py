from author import *
spec(0,'SQUARE','The rejected grapes are six isolated tiny rings. No written feedback. Rebuilt a connected six-berry bunch with larger circular upper berries, rounded lower lobes and a forked stem; no berry is dropped.', '''
for j,x in enumerate((12,24,36)):circle('grape'+str(j),x,22,6)
join('grape0','grape1');join('grape1','grape2')
arc('lower-left',(24,28),(12,28),6)
arc('lower-right',(36,28),(24,28),6)
join('lower-left','grape0','grape1');join('lower-right','grape1','grape2')
arc('bottom',(30,34),(18,34),6,8)
join('bottom','lower-left','lower-right')
path('stem',(24,16),[('L',(24,12)),('C',(16,6),(24,8),(20,6))]);join('stem','grape1')
bez('stem-right',(24,12),((24,8),(28,6),(32,6)));join('stem-right','stem')
''','Lucide grape: connected berry cluster and a curved stem; source supplies the 3/2/1 grouping.')
spec(1,'VRECT_L','The current remote loses a lower button and turns all round controls into dots. No written feedback. Rebalanced the divided remote and restored two lower left controls with a longer volume rocker.', '''
rect('shell',8,4,32,40,6)
line('divider',(8,23),(40,23));join('divider','shell')
for j,(x,y) in enumerate(((18,13),(30,13),(18,32),(18,40))):self.add_dot('button'+str(j),(x,y))
line('rocker',(30,32),(30,36))
''','No useful local remote match; rounded enclosure and equal button spacing from the supplied reference.')
spec(10,'SQUARE','The current front page is squat and sharp, and the rear dashed sheet loses its rounded lower corner. No written feedback. Restored a taller front document with a clipped corner and rounded base, plus coherent rear corner dashes.', '''
path('front',(19,16),[('L',(31,16)),('L',(42,27)),('L',(42,38)),('A',(38,42),4),('L',(19,42)),('A',(15,38),4),('L',(15,20)),('A',(19,16),4)],True)
path('back-top',(6,14),[('L',(6,10)),('A',(10,6),4),('L',(16,6))])
line('back-top-dash',(24,6),(31,6))
line('back-side',(6,22),(6,28))
path('back-bottom',(6,36),[('L',(6,38)),('A',(10,42),4,4,False)])
''','Lucide files and copy: rounded page corners and a coherent overlapping-page structure.')
spec(11,'SQUARE','The second car is only a small U and the first car resembles a generic box. No written feedback. Reconstructed two staggered complete overhead car silhouettes with windshield divisions.', '''
rect('car-front',26,6,16,25,6)
line('windshield-front',(26,16),(42,16));join('car-front','windshield-front')
rect('car-back',6,19,12,23,5)
line('windshield-back',(6,29),(18,29));join('car-back','windshield-back')
''','Lucide car: rounded vehicle enclosure; source defines overhead stagger rather than side-view details.')
spec(18,'VRECT_L','The rejected figure has sharp elbows and widely splayed legs, unlike the still reference. No written feedback. Rebuilt smooth hanging arms and two parallel standing legs around a simple torso.', '''
circle('head',24,10,6)
line('torso',(24,24),(24,32))
bez('arms',(8,33),((8,27),(14,24),(24,24)),((34,24),(40,27),(40,33)));join('arms','torso')
path('legs',(18,44),[('L',(18,36)),('A',(24,32),6,4,True),('A',(30,36),6,4,True),('L',(30,44))]);join('torso','legs')
self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
''','Shared human full_body_ref.png: round head and coherent limbs; head bottom16 to neck24 gives exact 4-unit ink gap.')
spec(19,'VRECT_M','The current microphone capsule is broad and squat with a large foot. No written feedback. Restored a taller capsule, two spaced grille rows, a centered thin stem and a shorter base.', '''
path('capsule',(14,14),[('A',(24,4),10),('A',(34,14),10),('L',(34,24)),('A',(24,34),10),('A',(14,24),10),('L',(14,14))],True)
for y in (14,24):
 line('left'+str(y),(14,y),(20,y));line('right'+str(y),(28,y),(34,y));join('left'+str(y),'capsule');join('right'+str(y),'capsule')
line('stem',(24,34),(24,44));poly('foot',(10,44),(24,44),(38,44));join('stem','capsule','foot')
''','Lucide mic: long capsule and centered supporting stem; supplied reference owns the grille and foot.')
if __name__=='__main__':
 for i in map(int,sys.argv[1:]):make(i)
