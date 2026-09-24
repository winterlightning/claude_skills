"""genie.
Plan: Turbaned genie face over curling smoke body. Shared human references; continuous portrait/torso arrangement rather than detached stick figure. No useful Lucide exact match.
Keyshape VRECT_L: visible bounds (6, 2, 42, 46); centerlines inset 2 from these bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='f9d2a78b-2eb0-40a5-bcec-c567992dd9f2'
SOURCE_PATH='pictographic-primitives/_uncategorized_20/genie_f9d2a78b-2eb0-40a5-bcec-c567992dd9f2.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='genie'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=('genie',)
    def build(self):
        self.path('turban',(14,16),[('A',(24,6),10,10,True),('A',(34,16),10,10,True)])
        self.path('jaw',(14,16),[('L',(14,20)),('A',(24,30),10,10,False),('A',(34,20),10,10,False),('L',(34,16))])
        self.relate('connect','turban','jaw')
        self.add_polyline('mustache',(19,20),(24,18),(29,20))
        self.path('smoke',(14,30),[('A',(6,38),8,8,False),('A',(14,46),8,8,False),('L',(26,46)),('A',(26,38),4,4,False),('L',(34,38)),('A',(42,30),8,8,False)])

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
