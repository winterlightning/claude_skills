from revise import *
SPECS[15]['code']='''
path('bird',(6,17),[('L',(8,15)),('A',(17,6),9),('A',(26,15),9),('C',(28,20),(26,18),(27,19)),('L',(42,34)),('C',(36,42),(42,40),(40,42)),('L',(24,32)),('C',(18,32),(22,33),(20,33)),('C',(10,20),(10,30),(10,24)),('L',(6,17))],True)
self.add_dot('eye',(17,15))
poly('leg',(18,32),(16,42),(10,42));join('leg','bird')
'''
SPECS[17]['code']=SPECS[17]['code'].replace('(6,35)','(6,36)').replace('(17,32)','(20,33)').replace('(10,39)','(12,42)').replace('((26,19),(27,23),(24,25))','((23,21),(25,23),(24,25))')
SPECS[6]['code']='''
circle('head',24,14,10)
bez('smile',(23,14),((23,16),(25,16),(25,14)))
poly('body',(8,44),(8,36),(16,30),(24,28),(32,30),(40,36),(40,44));join('head','body')
poly('emblem',(24,34),(32,39),(24,44),(16,39),closed=True)
line('collar',(24,28),(24,34));join('collar','body','emblem')
'''
SPECS[6]['note']='The rejected superhero is a blank head over a generic arch. No written feedback. Restored a smiling head, angular cape shoulders and an attached diamond chest emblem; tiny eyes and hair seams are omitted.'
if __name__=='__main__':
 for i in map(int,sys.argv[1:]):make(i)
