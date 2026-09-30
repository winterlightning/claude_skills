from author import *
D['right-indentation-action']['code']=D['right-indentation-action']['code'].replace('8,20,28,28','8,20,27,28').replace('16,36,28,44','16,36,27,44')
D['science-apple-gravity']['shape']='HRECT_L'
D['science-apple-gravity']['code']="""
path('apple',(24,14),[('C',(10,16),(16,8),(10,10)),('C',(18,27),(10,22),(14,27)),('C',(24,26),(20,27),(22,26)),('C',(30,27),(26,26),(28,27)),('C',(38,16),(34,27),(38,22)),('C',(24,14),(38,10),(32,8))],True)
path('stem',(24,14),[('C',(28,8),(24,11),(26,9))]);join('stem','apple')
for x,top in ((8,32),(24,35),(40,32)):
 n='fall'+str(x);line(n,(x,top),(x,40));poly(n+'head',(x-4,36),(x,40),(x+4,36));join(n,n+'head')
"""
D['shaped-armor-breastplate']['code']=D['shaped-armor-breastplate']['code'].replace("('L',(16,4)),('A',(32,4),8,8,False)","('L',(17,4)),('A',(31,4),7,7,False)").replace("(17,22)","(18,22)").replace("(17,28)","(18,28)").replace("(31,22)","(30,22)").replace("(31,28)","(30,28)")
D['seat-find']['code']=D['seat-find']['code'].replace('(20,26)','(20,28)').replace('(6,40),(14,32),(18,36),(22,42)','(6,42),(14,32),(20,35),(22,42)')
D['shoe-resting-on-open-rack']['code']="""
poly('rack',(6,42),(6,34),(6,14),(6,6),(42,6),(42,14),(42,34),(42,42))
for y in (14,34,42):line('shelf'+str(y),(6,y),(42,y));join('shelf'+str(y),'rack')
path('shoe',(14,34),[('L',(14,23)),('C',(23,23),(18,26),(19,26)),('C',(34,25),(27,23),(28,24)),('L',(34,34))]);join('shoe','shelf34')
"""
D['short-haired-woman-with-visible-sleeve-seams']['code']="""
path('face',(17,20),[('A',(31,20),7,7,False),('C',(26,15),(29,19),(28,17)),('C',(17,20),(24,18),(20,19))],True)
path('hair',(8,24),[('L',(8,20)),('A',(40,20),16,16,True),('L',(40,24))])
path('body',(8,44),[('L',(8,39)),('A',(24,31),16,8,True),('A',(40,39),16,8,True),('L',(40,44)),('L',(32,44)),('L',(16,44)),('L',(8,44))],True);join('face','body')
for x in (16,32):line('sleeve'+str(x),(x,41),(x,44));join('sleeve'+str(x),'body')
"""
D['six-legged-termite']['code']=D['six-legged-termite']['code'].replace('(24,8)','(24,7)').replace('(28,8),(30,9)','(28,7),(30,8)').replace('(18,9),(20,8)','(18,8),(20,7)').replace('(x,20),(end,16),(end,10)','(x,20),(end,20),(end,10)')
D['smiling-tree-trunk-batch-086']['code']=D['smiling-tree-trunk-batch-086']['code'].replace('(11,','(12,').replace('(37,','(36,').replace('(4,13)','(4,12)').replace('(44,13)','(44,12)').replace('7,7,False','8,8,False').replace('7,7,True','8,8,True')
D['spool-wrapped-with-thread']['code']=D['spool-wrapped-with-thread']['code'].replace("box('thread-body',8,12,40,36,4)","box('thread-body',8,12,40,36,2)")
D['policewoman-with-rounded-helmet']['code']=D['policewoman-with-rounded-helmet']['code'].replace("path('shoulders',(8,44),[('L',(8,40)),('C',(16,34),(8,36),(12,34)),('C',(24,32),(18,32),(21,32)),('C',(32,34),(27,32),(30,32)),('C',(40,40),(36,34),(40,36)),('L',(40,44))])", "path('shoulders',(9,44),[('L',(9,42)),('A',(15,34),15,10,True),('A',(24,32),15,10,True),('A',(33,34),15,10,True),('A',(39,42),15,10,True),('L',(39,44))])").replace("(16,34),(24,42),(32,34)","(15,34),(24,42),(33,34)")
if __name__=='__main__':generate(sys.argv[1:])
