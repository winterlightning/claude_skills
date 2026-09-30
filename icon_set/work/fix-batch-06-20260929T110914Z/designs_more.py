# Additional fresh SOLO48 revisions; source metadata is embedded by author.make.
from author import *
spec(7,'SQUARE','The rejected brain is a pinched clover and the facial jaw is angular. No written feedback. Opened the brain into broad rounded lobes and smoothed the left-facing head and neck; omitted internal folds.', '''
path('head',(35,42),[('C',(42,22),(32,33),(42,33)),('C',(25,6),(42,12),(35,6)),('C',(10,21),(16,6),(10,12)),('L',(6,28)),('L',(10,28)),('L',(10,33)),('C',(14,36),(10,35),(11,36)),('L',(22,36)),('L',(22,42))])
path('brain',(20,26),[('C',(19,20),(16,26),(17,21)),('C',(26,16),(18,15),(23,13)),('C',(33,22),(32,13),(36,17)),('C',(28,28),(36,26),(32,30)),('L',(28,26)),('L',(20,26))],True)
''','Lucide brain: coherent rounded lobes. Shared human user reference: smooth head and shoulder vocabulary.')
spec(8,'SQUARE','The rejected version is an ordinary wrench and drops the lightning-shaped lower edge in the original. No written feedback. Restored the open lightning stroke below the wrench jaw and the rounded left handle end.', '''
path('wrench',(13,42),[('C',(8,32),(6,42),(6,36)),('L',(20,21)),('C',(30,6),(17,12),(22,6)),('L',(24,14)),('L',(32,22)),('L',(42,12)),('C',(36,27),(42,21),(40,25))])
poly('lightning',(27,27),(18,36),(38,32),(28,42))
''','Lucide wrench: round shoulder and purposeful open jaw; reference supplies lightning.')
spec(9,'HRECT_L','The rejected masks have no eyes and tiny mouth marks, so they read as bowls. No written feedback. Restored eyes and broad opposing mouth curves on overlapping theatrical faces.', '''
path('front',(4,8),[('L',(28,8)),('L',(28,22)),('C',(16,34),(28,30),(22,34)),('C',(4,22),(10,34),(4,30)),('L',(4,8))],True)
self.add_dot('eye-left',(12,17));self.add_dot('eye-right',(20,17))
bez('frown',(12,27),((14,23),(18,23),(20,27)))
path('back',(28,14),[('L',(44,14)),('L',(44,28)),('C',(32,40),(44,36),(39,40)),('C',(22,33),(26,40),(23,36))]);join('back','front')
self.add_dot('rear-eye',(36,23))
bez('smile',(31,31),((33,34),(35,34),(37,31)))
''')
spec(10,'SQUARE','The rejected owl is a flat wide face with a dot beak, losing the pointed ears and tapered body. No written feedback. Restored ear tufts, a rounder body and a short pointed beak below matched circular eyes.', '''
path('body',(6,6),[('C',(24,11),(8,13),(17,8)),('C',(42,6),(31,8),(40,13)),('L',(42,25)),('C',(24,42),(42,36),(34,42)),('C',(6,25),(14,42),(6,36)),('L',(6,6))],True)
for x in (16,32):circle(f'eye{x}',x,22,3)
poly('beak',(22,32),(24,35),(26,32))
''','Lucide bird: simple body and identifying beak; bilateral eyes share radius.')
spec(11,'SQUARE','The current palm is mechanically symmetric and crowded against a flattened island. No written feedback. Rebuilt an asymmetric curved trunk and three flowing fronds over a broad island arc and water line.', '''
bez('trunk',(25,15),((26,23),(25,28),(22,34)))
bez('upper-left',(25,15),((19,6),(13,6),(8,6)))
bez('upper-right',(25,15),((29,6),(34,6),(40,6)))
bez('lower-left',(25,15),((14,13),(6,18),(6,23)))
bez('lower-right',(25,15),((33,15),(42,18),(42,23)))
join('trunk','upper-left','upper-right','lower-left','lower-right')
bez('island',(6,42),((9,37),(15,34),(22,34)),((30,34),(37,37),(42,42)));join('trunk','island')
''','No local palm-tree original found; source informs intentional leaning trunk and irregular fronds.')
spec(12,'SQUARE','The rejected firework is three alert marks above tiny isolated heads. No written feedback. Rebuilt a spreading three-trail burst with star endpoints and broadened the spectators shoulders; retained all three spectators.', '''
for x in (9,24,39):
 circle('head'+str(x),x,29,3)
 arc('shoulders'+str(x),(x-3,42),(x+3,42),3,2)
# Curved trajectories and cross-shaped sparkles establish fireworks.
bez('trail-left',(16,20),((13,15),(10,12),(6,12)))
bez('trail-mid',(24,18),((24,12),(23,8),(20,6)))
bez('trail-right',(33,20),((35,15),(38,12),(42,12)))
''','Shared human user.svg and full_body_ref.png: three identical round heads, exactly 4-unit ink gap to shoulder apex.')
spec(13,'VRECT_L','The rejected hawk loses the folded wing and reads as a thin generic bird. No written feedback. Broadened the chest and tail, restored a short folded-wing contour, and kept the hooked beak and perch foot.', '''
path('outline',(8,37),[('C',(21,14),(12,28),(21,23)),('C',(31,4),(21,7),(25,4)),('C',(40,14),(37,4),(40,8)),('L',(34,12)),('C',(29,34),(34,23),(36,30)),('C',(8,37),(23,39),(13,39))],True)
bez('wing',(23,18),((28,21),(25,28),(18,31)))
poly('leg',(27,36),(29,44),(37,44));join('leg','outline')
''','Lucide bird: folded wing, hooked head and simple attached feet.')
spec(14,'SQUARE','The current atomizer has stacked cramped rectangular necks and a tiny circular bulb. No written feedback. Simplified the neck to one open spray stem and enlarged the squeeze bulb; restored a taller rounded bottle.', '''
rect('bottle',6,21,24,21,5)
poly('neck',(14,21),(14,6),(22,6),(22,21));join('neck','bottle')
line('hose',(22,10),(32,10));join('hose','neck')
path('bulb',(32,10),[('C',(37,6),(32,7),(34,6)),('C',(42,12),(41,6),(42,9)),('C',(37,18),(42,15),(41,18)),('C',(32,10),(32,18),(31,14))],True);join('bulb','hose')
''','Lucide cooking-pot: rounded body with clear attachment; source supplies atomizer hose and bulb.')
if __name__=='__main__':
 for i in map(int,sys.argv[1:]):make(i)
