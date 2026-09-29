"""Rejected three tiny bumps no longer read as curled fingers. Restore a long index, raised thumb and three broad rounded folded-finger levels."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='b249903e-3cbd-4e65-ad2d-7ccb681f7fed'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__right-pointing-hand-with-raised-thumb/20260929T044747Z-thuan-mac/reference/hand pointer right_b249903e-3cbd-4e65-ad2d-7ccb681f7fed.svg'
AUTHOR='gpt-6'
PLAN='Rejected three tiny bumps no longer read as curled fingers. Restore a long index, raised thumb and three broad rounded folded-finger levels.'
CONSTRUCTION_REFERENCE='Previously inspected Lucide hand: round finger tips and one flowing palm contour.'
OMISSIONS='Secondary source detail simplified only where needed for 48 px legibility.'
class Drawing(Solo48):
    icon_id='right-pointing-hand-with-raised-thumb'
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
        self.path('palm',(24,17),[('C',(26,8),(30,13),(30,8)),('L',(13,14)),('C',(4,27),(7,17),(4,20)),('L',(4,30)),('A',(14,40),10,10,False),('L',(25,40)),('A',(25,33),4,4,False),('L',(20,33))])
        self.path('index',(24,17),[('L',(40,17)),('A',(40,25),4,4,True),('L',(23,25))])
        self.path('middle',(30,25),[('A',(30,33),4,4,True),('L',(23,33))])
        self.relate('connect','palm','index');self.relate('connect','index','middle');self.relate('connect','middle','palm')
