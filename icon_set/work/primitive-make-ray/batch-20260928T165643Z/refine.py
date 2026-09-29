from author_batch import *
SPECS[1]['code']=SPECS[1]['code'].replace("('L',(12,14)),('L',(16,10)),('L',(32,10)),('L',(36,14))","('L',(9,14)),('L',(13,10)),('L',(35,10)),('L',(39,14))").replace("('L',(36,34)),('L',(32,38)),('L',(16,38)),('L',(12,34))","('L',(39,34)),('L',(35,38)),('L',(13,38)),('L',(9,34))").replace("(17,32),(31,32)","(18,31),(30,31)")
SPECS[2]['code']=SPECS[2]['code'].replace('(18,25)','(17,24)').replace('(14,32),(34,32)','(14,31),(34,31)')
SPECS[3]['code']=SPECS[3]['code'].replace('(44,16),(41,21)','(42,16),(41,21)')
SPECS[6]['code']='''
# Continuous robed neck: real shared contacts at the head left and bottom.
# human_ref/full_body_ref.png supplies circular-head proportions; source owns flowing robe.
self.path('head',(28,18),[('A',(34,12),6,6,True),('A',(40,18),6,6,True),('A',(34,24),6,6,True),('A',(28,18),6,6,True)],True)
self.path('halo',(26,4),[('A',(42,4),8,2,True)])
self.path('robe',(34,24),[('C',(28,42),(34,30),(31,38)),('C',(6,29),(18,42),(10,36)),('C',(28,18),(16,27),(24,23))])
self.relate('connect','head','robe')
self.path('wing',(22,15),[('C',(6,6),(15,12),(10,9)),('C',(13,19),(6,13),(7,18))])
'''
SPECS[6]['change']='Restored a full swept robe and circular head with real continuous-neck joins, and separated the open rear wing with visible negative space.'
SPECS[7]['code']='''
self.path('heart',(24,10),[('C',(15,6),(21,7),(18,6)),('C',(6,16),(9,6),(6,10)),('C',(24,42),(6,34),(14,39)),('C',(42,16),(34,39),(42,34)),('C',(33,6),(42,10),(39,6)),('C',(24,10),(30,6),(27,7))],True)
self.circle('head',24,20,3)
# user.svg: head bottom23, shoulders top31 = exact 4 ink gap.
self.path('shoulders',(20,33),[('A',(24,31),4,2,True),('A',(28,33),4,2,True)])
'''
SPECS[10]['code']=SPECS[10]['code'].replace("('C',(20,24),(26,37),(20,31))","('C',(23,33),(27,38),(25,36)),('C',(20,24),(21,30),(20,27))").replace("'rear',(22,32)","'rear',(23,33)")
SPECS[15]['code']=SPECS[15]['code'].replace('(30,17)','(29,17)')
SPECS[18]['code']=SPECS[18]['code'].replace('(22,36),(26,36)','(22,35),(26,35)')
SPECS[19]['code']=SPECS[19]['code'].replace('(18,28),(18,20)','(19,28),(19,20)').replace('(30,20),(30,28)','(29,20),(29,28)')
SPECS[20]['code']=SPECS[20]['code'].replace('(22,36),(26,36)','(22,35),(26,35)')
records=json.loads((Path(__file__).parent/'runs.json').read_text())
for n in [1,2,3,6,7,10,15,18,19,20]:
    records[n-1]=author(n,'r3' if n==1 else 'r2')
(Path(__file__).parent/'refined-runs.json').write_text(json.dumps(records,indent=2))
