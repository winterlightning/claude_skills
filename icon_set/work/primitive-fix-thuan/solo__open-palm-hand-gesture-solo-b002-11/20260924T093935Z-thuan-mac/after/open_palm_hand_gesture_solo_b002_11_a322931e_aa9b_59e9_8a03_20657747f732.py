'Upturned offering hand with rounded thumb above palm and long fingers pointing right. Centerline4,10 to44,38.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a322931e-aa9b-59e9-8a03-20657747f732'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__open-palm-hand-gesture-solo-b002-11/20260924T093935Z-thuan-mac/reference/begging hand ask_a322931e-aa9b-59e9-8a03-20657747f732.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'Lucide hand-helping: rounded thumb returning into palm and long finger edge.'
OMISSIONS = 'Finger divisions omitted as in source.'

def path(s,n,p,cs,closed=False):
    ids=[]
    for j,c in enumerate(cs):
        eid=f'{n}-{j}';q=c[-1]
        if c[0]=='L':s.add_line(eid,p,q)
        elif c[0]=='A':s.add_arc(eid,p,q,radius_x=c[1],radius_y=c[2],sweep=c[3])
        elif c[0]=='C':s.add_bezier(eid,p,(c[1],c[2],q))
        ids.append(eid);p=q
    s.add_contour(n,*ids,closed=closed)
def circle(s,n,x,y,r):
    path(s,n,(x-r,y),[('A',r,r,True,(x+r,y)),('A',r,r,True,(x-r,y))],True)

class Drawing(Solo48):
    icon_id = 'open-palm-hand-gesture-solo-b002-11'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('begging', 'hand', 'ask')
    def build(self):
        path(self,'hand',(4,34),[('L',(4,16)),('C',(10,14),(13,10),(18,10)),('C',(22,10),(26,12),(28,14)),('A',5,5,True,(24,24)),('L',(17,22))])
        path(self,'fingers',(24,24),[('L',(37,16)),('C',(41,13),(44,15),(44,19)),('C',(44,21),(43,23),(41,24)),('L',(27,35)),('C',(24,38),(21,38),(19,38)),('C',(18,38),(17,37),(16,37)),('L',(4,34))])
        self.relate('connect','hand','fingers')
