"""engineer project superviser 1.
Plan: Helmeted supervisor beside plan bracket. human-reference.md/user.svg shared circular head radius8, lower22 and shoulder apex30 give exactly4 ink gap; semicircular shoulder construction. Omit small helmet ridge. No useful Lucide exact match.
Keyshape SQUARE: visible bounds (4, 4, 44, 44); centerlines inset 2 from these bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='9ec9ed06-396b-4bca-8680-e36e1ed302bf'
SOURCE_PATH='pictographic-primitives/_uncategorized_16/engineer project superviser 1_9ec9ed06-396b-4bca-8680-e36e1ed302bf.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='engineer-project-superviser-1'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=('engineer', 'project', 'superviser', '1')
    def build(self):
        self.circle('head',18,14,8)
        self.add_polyline('brim',(6,14),(10,14),(26,14),(30,14));self.relate('connect','head','brim')
        self.path('shoulders',(6,42),[('A',(18,30),12,12,True),('A',(30,42),12,12,True)])
        self.path('plan',(42,6),[('A',(38,10),4,4,False),('L',(38,18)),('L',(38,26)),('A',(42,30),4,4,False)])
        self.add_line('plan-mark',(38,18),(42,18));self.relate('connect','plan','plan-mark')

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
