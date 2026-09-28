"""autism disorder symptoms.
Plan: Asymmetric head with missing upper-left puzzle region. Shared human user.svg smooth anatomical construction, continuous neck; no detached head. No useful Lucide match.
Keyshape SQUARE: visible bounds (4, 4, 44, 44); centerlines inset 2 from these bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='4a264e06-6d44-57cc-8176-d57369c6c0ee'
SOURCE_PATH='pictographic-primitives/health/autism disorder symptoms_4a264e06-6d44-57cc-8176-d57369c6c0ee.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='autism-disorder-symptoms'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=('autism', 'disorder', 'symptoms')
    def build(self):
        # Detached puzzle piece and continuous anatomical neck profile.
        self.path('piece',(6,14),[('A',(14,6),8,8,True),('L',(22,6)),('L',(22,17)),('L',(18,17)),('A',(10,17),4,4,True),('L',(6,17)),('L',(6,14))],True)
        self.path('profile',(16,42),[('L',(16,38)),('A',(10,30),8,8,True),('L',(20,30)),('A',(30,30),5,5,False),('L',(32,30)),('L',(32,14)),('A',(38,24),10,10,True),('L',(42,30)),('L',(38,30)),('L',(38,34)),('A',(34,38),4,4,True),('L',(30,38)),('L',(30,42))])

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def path(self,n,start,ops,closed=False):
        at=start; members=[]
        for i,op in enumerate(ops):
            eid=f'{n}-{i}';kind,end,*args=op
            if end==at:continue
            if kind=='L':self.add_line(eid,at,end)
            elif kind=='A':self.add_arc(eid,at,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            at=end;members.append(eid)
        self.add_contour(n,*members,closed=closed)
