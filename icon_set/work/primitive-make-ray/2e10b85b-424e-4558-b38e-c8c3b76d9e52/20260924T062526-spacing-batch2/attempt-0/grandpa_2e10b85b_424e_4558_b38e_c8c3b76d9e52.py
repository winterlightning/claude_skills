"""grandpa.
Plan: Grandpa with paired spectacles, frown and bust shoulders. Lucide glasses circular lenses and shared bridge; human-reference.md circular jaw and shoulder contact. Bust ink contact: jaw bottom36, body apex40, gap0. Initial spectacle placement to be repaired.
Keyshape VRECT_L: visible bounds (6, 2, 42, 46); centerlines inset 2 from these bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='2e10b85b-424e-4558-b38e-c8c3b76d9e52'
SOURCE_PATH='pictographic-primitives/_uncategorized_21/grandpa_2e10b85b-424e-4558-b38e-c8c3b76d9e52.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='grandpa'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=('grandpa',)
    def build(self):
        self.path('head',(8,20),[('A',(24,4),16,16,True),('A',(40,20),16,16,True)])
        self.path('jaw',(8,20),[('A',(24,36),16,16,False),('A',(40,20),16,16,False)])
        self.relate('connect','head','jaw')
        for n,x in [('left',16),('right',32)]:self.circle('glasses-'+n,x,18,4)
        self.add_line('bridge',(20,18),(28,18));self.relate('connect','bridge','glasses-left');self.relate('connect','bridge','glasses-right')
        self.add_arc('frown',(21,28),(27,28),radius_x=4,sweep=True)
        self.path('body',(8,44),[('A',(24,40),16,4,True),('A',(40,44),16,4,True)])
        self.relate('connect','jaw','body')

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
