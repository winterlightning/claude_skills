from faces import *
spec(12,'SQUARE','The rejected alpaca is angular and reads like a blocky dog. No written feedback. Rebuilt a taller neck, rounded muzzle, upright ear and softer back and haunch while preserving two visible legs; tiny eye and far legs are omitted.', '''
path('alpaca',(6,28),[('C',(12,22),(6,24),(8,22)),('L',(25,22)),('L',(25,13)),('C',(29,10),(25,11),(27,10)),('L',(29,6)),('L',(32,12)),('C',(36,14),(34,12),(36,12)),('L',(39,14)),('C',(42,18),(42,14),(42,16)),('C',(38,22),(42,21),(40,22)),('L',(35,22)),('L',(37,42)),('L',(28,42)),('L',(27,32)),('L',(18,32)),('L',(15,42)),('L',(6,42)),('L',(8,33)),('C',(6,28),(6,32),(6,30))],True)
''','Source defines long neck and standing profile; no useful local alpaca body match.')
spec(13,'SQUARE','The current head is squat and the pointed wing dominates the round body. No written feedback. Gave the bird a taller round head and neck, a broad smoothly folded wing and two aligned legs.', '''
path('bird',(6,26),[('C',(25,16),(12,20),(20,16)),('L',(25,13)),('A',(32,6),7),('A',(39,13),7),('L',(42,15)),('L',(38,18)),('C',(26,34),(40,27),(34,34)),('C',(6,26),(18,34),(12,31))],True)
bez('wing',(25,16),((32,24),(24,30),(6,26)));join('wing','bird')
for x in (22,32):line('leg'+str(x),(x,34),(x,42));join('leg'+str(x),'bird')
poly('foot',(20,42),(22,42),(32,42),(36,42));join('foot','leg22','leg32')
''','Lucide bird: coherent head/body and a broad folded wing; source supplies long neck and wing arrangement.')
spec(14,'HRECT_L','The current bull has a triangular muzzle and tiny uneven horns. No written feedback. Rounded the shoulders and muzzle, widened the body and rebuilt two rising horns above the head; far legs and facial marks are omitted.', '''
path('bull',(4,40),[('L',(4,26)),('A',(14,16),10),('L',(28,16)),('C',(34,12),(28,12),(32,12)),('C',(44,24),(38,12),(42,20)),('L',(37,24)),('C',(30,33),(34,24),(34,30)),('L',(30,40)),('L',(22,40)),('L',(22,31)),('L',(12,31)),('L',(12,40))])
bez('horn-left',(28,16),((25,14),(25,10),(27,8)))
bez('horn-right',(34,12),((39,14),(41,11),(40,8)))
join('bull','horn-left','horn-right')
''','No useful local bull profile; source supplies broad body, lowered muzzle and paired horns.')
spec(15,'SQUARE','The rejected magpie has a short solid tail and no eye. No written feedback. Restored an elongated outlined tapering tail, a round head with a visible eye, and a supporting bent leg; the second foot and wing seam are omitted for spacing.', '''
path('bird',(6,17),[('L',(8,15)),('A',(17,6),9),('A',(26,15),9),('C',(35,30),(26,20),(32,25)),('L',(42,40)),('C',(38,42),(42,42),(40,42)),('L',(26,33)),('C',(10,20),(18,36),(10,30)),('L',(6,17))],True)
self.add_dot('eye',(17,15))
poly('leg',(18,33),(16,42),(10,42));join('leg','bird')
''','Lucide bird: circular head and purposeful eye; source supplies left-facing pose and long tail.')
spec(16,'HRECT_L','The current cougar has a dog-like angular head and almost no tail. No written feedback. Restored a long curved tail, a small rounded ear, softer muzzle and horizontal back above two clear legs.', '''
path('cat',(16,20),[('L',(28,20)),('C',(33,13),(30,18),(31,15)),('C',(36,8),(33,8),(34,8)),('C',(39,13),(38,8),(39,11)),('C',(44,17),(42,13),(44,15)),('C',(39,22),(44,20),(42,22)),('L',(38,40)),('L',(30,40)),('L',(30,30)),('L',(22,30)),('L',(22,40)),('L',(14,40)),('L',(14,28)),('C',(16,20),(14,23),(14,20))],True)
bez('tail',(16,20),((8,20),(4,24),(4,32)));join('tail','cat')
''','Lucide cat: small rounded facial vocabulary; source defines the long-tailed full-body cougar.')
spec(17,'SQUARE','The current nightingale loses its folded wing and broad tail. No written feedback. Restored a short outlined tail, visible eye, curved wing seam and two bent legs around a rounded breast.', '''
path('bird',(6,35),[('L',(22,18)),('L',(22,15)),('A',(31,6),9),('A',(40,15),9),('L',(42,17)),('L',(38,20)),('C',(32,32),(39,27),(36,30)),('C',(22,34),(28,34),(25,34)),('C',(17,32),(20,34),(18,33)),('L',(10,39)),('L',(6,35))],True)
self.add_dot('eye',(31,15))
bez('wing',(22,18),((26,19),(27,23),(24,25)));join('wing','bird')
poly('leg-left',(22,34),(24,42),(28,42));poly('leg-right',(32,32),(36,42),(40,42));join('leg-left','bird');join('leg-right','bird')
''','Lucide bird: eye, folded wing and coherent silhouette; source supplies short broad tail and two feet.')
if __name__=='__main__':
 for i in map(int,sys.argv[1:]):make(i)
