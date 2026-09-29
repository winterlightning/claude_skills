"""Rejected tight sawtooth knuckles obscure the folded fingers. Restore broad finger arcs and the downward thumb below the extended index."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='f5998a23-038d-5b25-93ae-d109ee0a5cea'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__right-pointing-hand-with-lower-thumb/20260929T044747Z-thuan-mac/reference/hand pointer right_f5998a23-038d-5b25-93ae-d109ee0a5cea.svg'
AUTHOR='gpt-6'
PLAN='Rejected tight sawtooth knuckles obscure the folded fingers. Restore broad finger arcs and the downward thumb below the extended index.'
CONSTRUCTION_REFERENCE='Previously inspected Lucide hand: rounded fingers and coherent palm; thumb orientation follows original.'
OMISSIONS='Secondary source detail simplified only where needed for 48 px legibility.'
class Drawing(Solo48):
    icon_id='right-pointing-hand-with-lower-thumb'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=()

    def circle(self,n,x,y,r):
        self.add_arc(n+'a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'a',n+'b',closed=True)
    def path(self,n,start,commands,closed=False):
        ids=[]; here=start
        for i,c in enumerate(commands):
            tag,end,*args=c; eid=f'{n}-{i}'
            if tag=='L': self.add_line(eid,here,end)
            elif tag=='A': self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif tag=='C': self.add_bezier(eid,here,(args[0],args[1],end))
            ids.append(eid); here=end
        self.add_contour(n,*ids,closed=closed)
    def box(self,n,l,t,r,b,rad=3):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

    def build(self):
        self.path('palm',(23,32),[('C',(25,40),(30,36),(29,40)),('L',(12,33)),('C',(4,21),(7,30),(4,27)),('L',(4,18)),('A',(14,8),10,10,True),('L',(25,8)),('A',(25,16),4,4,True),('L',(20,16))])
        self.path('index',(23,32),[('L',(40,32)),('A',(40,24),4,4,False),('L',(23,24))])
        self.path('middle',(30,24),[('A',(30,16),4,4,False),('L',(25,16))])
        self.relate('connect','palm','index');self.relate('connect','index','middle');self.relate('connect','middle','palm')
