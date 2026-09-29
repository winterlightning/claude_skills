from author_batch import *
records=json.loads((Path(__file__).parent/'runs.json').read_text())
SPECS[1]['code']=SPECS[1]['code'].replace("('C',(34,16),(36,18),(35,17)),('C',(29,10),(33,12),(31,10))","('C',(35,14),(36,18),(36,16)),('C',(29,10),(34,11),(31,10))").replace('(28,22),(34,16),(42,8),(42,6)','(28,22),(35,14),(42,6)').replace('(34,16) and (14,34)','(35,14) and (14,34)')
SPECS[7]['code']=SPECS[7]['code'].replace("'target',(10,17)","'target',(11,17)").replace("('C',(10,31)","('C',(11,31)").replace("'node',10,24,7","'node',11,24,7")
SPECS[11]['code']=SPECS[11]['code'].replace("'jaw-top',(26,14),[('C',(26,21),(24,16),(24,19)),('C',(32,20),(28,23),(31,22))]","'jaw-top',(28,12),[('C',(26,18),(25,12),(23,16)),('C',(32,15),(29,20),(32,18))]").replace("(22,25),(26,21)","(22,25),(26,18)")
SPECS[20]['code']='''
self.path('case',(8,12),[('L',(32,12)),('A',(36,16),4,4,True),('L',(36,20)),('L',(36,28)),('L',(36,32)),('A',(32,36),4,4,True),('L',(8,36)),('A',(4,32),4,4,True),('L',(4,16)),('A',(8,12),4,4,True)],True)
self.path('terminal',(36,20),[('L',(42,20)),('A',(44,22),2,2,True),('L',(44,26)),('A',(42,28),2,2,True),('L',(36,28))])
self.relate('connect','case','terminal')
self.add_polyline('charge',(12,18),(18,18),(18,30),(12,30),closed=True)
'''
for n in (1,7,11,20):records[n-1]=author(n,'r2')
(Path(__file__).parent/'final-runs.json').write_text(json.dumps(records,indent=2))
