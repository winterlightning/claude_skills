"""Rejected angular horse has a flat body and narrow head; the toy variant also has a flat sled base. Restore a rounded horse silhouette, arched belly and a visibly curved rocker."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='695d2eba-c368-5a10-a94f-69eec9ba9e64'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__rocking-horse-toy/20260929T044747Z-thuan-mac/reference/rocking-horse-toy_695d2eba-c368-5a10-a94f-69eec9ba9e64.svg'
AUTHOR='gpt-6'
PLAN='Rejected angular horse has a flat body and narrow head; the toy variant also has a flat sled base. Restore a rounded horse silhouette, arched belly and a visibly curved rocker.'
CONSTRUCTION_REFERENCE='No useful Lucide subject match; original reference establishes silhouette and arrangement.'
OMISSIONS='Eye omitted to keep muzzle open; rounded neck, arched belly, tail and curved rocker retained.'
class Drawing(Solo48):
    icon_id='rocking-horse-toy'
    keyshape=Keyshape.SQUARE
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
        self.path('horse',(8,22),[('C',(6,15),(3,21),(4,17)),('L',(16,9)),('C',(21,12),(19,7),(20,9)),('L',(25,22)),('L',(33,22)),('C',(39,29),(38,22),(38,25)),('L',(42,36)),('L',(35,39)),('C',(27,31),(33,33),(32,31)),('C',(15,36),(21,29),(17,31)),('L',(12,39)),('L',(6,36)),('L',(15,24)),('L',(13,19)),('L',(8,22))],True)
        self.add_bezier('rocker',(4,36),((14,46),(34,46),(44,36)))
        self.path('tail',(37,25),[('C',(44,29),(41,21),(44,25))])
        self.relate('connect','horse','rocker','tail')
