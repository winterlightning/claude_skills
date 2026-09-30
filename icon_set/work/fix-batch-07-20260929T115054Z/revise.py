from animals import *
SPECS[0]['code']=SPECS[0]['code'].replace("(12,28),6)","(12,28),6,7)").replace("(24,28),6)","(24,28),6,7)").replace("(30,34),(18,34),6,8","(30,35),(18,35),6,7")
SPECS[1]['code']='''
rect('shell',8,4,32,40,6)
for j,(x,y) in enumerate(((18,15),(30,15),(18,27),(18,35))):self.add_dot('button'+str(j),(x,y))
line('rocker',(30,27),(30,35))
'''
SPECS[1]['note']='The current remote omits a lower button and compresses the rocker. No written feedback. Restored all four button positions and a longer volume rocker inside a rounded shell; the divider and tiny label are omitted to preserve control spacing.'
SPECS[3]['code']=SPECS[3]['code'].replace('(24,9)','(24,8)').replace('(22,9)','(22,8)').replace('(26,9)','(26,8)').replace('(18,30)','(19,29)')
SPECS[6]['code']='''
circle('head',24,14,10)
bez('smile',(23,14),((23,16),(25,16),(25,14)))
arc('body-left',(8,44),(24,28),16);arc('body-right',(24,28),(40,44),16)
join('head','body-left');join('head','body-right')
poly('emblem',(20,38),(24,42),(28,38))
'''
SPECS[6]['note']='The current superhero has a small blank head. No written feedback. Enlarged the circular head and restored a smile over broad cape shoulders and an open chest chevron; tiny eyes and the enclosed emblem are omitted for spacing.'
SPECS[7]['code']=SPECS[7]['code'].replace("('C',(30,32),(22,32),(27,32))","('C',(30,35),(22,34),(27,35))")
SPECS[8]['code']=SPECS[8]['code'].replace("('C',(8,28),(8,16),(8,21))","('C',(8,22),(8,12),(8,18)),('L',(8,28))").replace("bez('wisp',(26,4),((22,6),(22,10),(22,12)))","bez('wisp',(30,4),((27,5),(26,7),(26,9)))")
SPECS[9]['code']='''
path('face',(6,24),[('L',(6,23)),('C',(16,15),(6,17),(10,15)),('A',(32,15),8,9,True),('C',(42,23),(38,15),(42,17)),('L',(42,24)),('A',(6,24),18)],True)
for x in (18,30):circle('lens'+str(x),x,26,3)
line('bridge',(21,26),(27,26));join('bridge','lens18','lens30')
'''
SPECS[9]['note']='The rejected glasses look like filled dots and the hair looks rectangular. No written feedback. Restored visible round lens openings, a bridge, an integrated rounded bun and a circular jaw. The small smile, ears and hair partition are omitted to keep the lenses clear.'
SPECS[10]['code']=SPECS[10]['code'].replace('(19,16)','(23,16)').replace('(19,42)','(23,42)').replace('(15,38)','(19,38)').replace('(15,20)','(19,20)').replace('(6,14)','(6,13)').replace('(6,28)','(6,27)')
if __name__=='__main__':
 for i in map(int,sys.argv[1:]):make(i)
