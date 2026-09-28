"""sign language thank you.
Plan: Open hand and downward sweeping arrow. Lucide hand rounded fingertip arcs and shared boundaries; human_ref/user.svg and full_body_ref.png human vocabulary, no detached head. Deliberate hand asymmetry.
Keyshape SQUARE: visible bounds (4, 4, 44, 44); centerlines inset 2 from these bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
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
        # Rounded fingertips share actual attachment nodes with separator strokes.
        self.path('hand',(6,24),[('L',(6,30)),('A',(18,42),12,12,False),('L',(22,42)),('A',(30,34),8,8,False),('L',(38,26)),('L',(38,18)),('A',(30,18),4,4,False),('L',(30,14)),('A',(22,14),4,4,False),('L',(22,10)),('A',(14,10),4,4,False),('L',(14,26)),('L',(6,24))],True)
        self.add_line('finger-middle',(22,14),(22,24));self.relate('connect','hand','finger-middle')
        self.add_line('finger-ring',(30,18),(30,26));self.relate('connect','hand','finger-ring')
        self.path('motion',(30,26),[('A',(36,32),6,6,True),('L',(36,42))])
        self.add_polyline('arrow',(30,36),(36,42),(42,36));self.relate('connect','motion','arrow')

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
