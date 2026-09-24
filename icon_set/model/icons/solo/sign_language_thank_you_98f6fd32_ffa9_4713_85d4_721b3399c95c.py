"""sign language thank you.
Plan: Four rounded fingertips and thumb with downward motion arrow. Lucide hand coherent finger arches; human-reference.md and user.svg/full_body_ref.png inspected; no detached head.
Keyshape SQUARE: visible bounds (4, 4, 44, 44); centerlines inset 2 from these bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='98f6fd32-ffa9-4713-85d4-721b3399c95c'
SOURCE_PATH='pictographic-primitives/messages/sign language thank you_98f6fd32-ffa9-4713-85d4-721b3399c95c.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='sign-language-thank-you'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=('sign', 'language', 'thank', 'you')
    def build(self):
        self.path('hand',(26,30),[('A',(14,34),10,10,True),('L',(6,22)),('L',(10,26)),('L',(10,14)),('A',(18,14),4,4,True),('L',(18,10)),('A',(26,10),4,4,True),('L',(26,14)),('A',(34,14),4,4,True),('L',(34,18)),('A',(42,18),4,4,True),('L',(42,26))])
        for n,x,y in [('index',18,14),('middle',26,14),('ring',34,18)]:
            self.add_line(n,(x,y),(x,18));self.relate('connect','hand',n)
        self.path('motion',(26,30),[('A',(36,40),10,10,True),('L',(36,42))])
        self.add_polyline('arrow',(32,38),(36,42),(40,38));self.relate('connect','motion','arrow');self.relate('connect','hand','motion')

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
