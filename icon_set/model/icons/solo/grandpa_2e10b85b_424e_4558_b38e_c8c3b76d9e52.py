"""grandpa.
Plan: Grandpa bust with spectacle frames genuinely attached to head dome and jaw. Lucide glasses common bridge; human-reference.md circular jaw and zero-ink shoulder contact at y38/42. Omit frown to clear facial band.
Keyshape VRECT_L: visible bounds (6, 2, 42, 46); centerlines inset 2 from these bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='2e10b85b-424e-4558-b38e-c8c3b76d9e52'
SOURCE_PATH='pictographic-primitives/_uncategorized_21/grandpa_2e10b85b-424e-4558-b38e-c8c3b76d9e52.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='grandpa'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    human_construction="bust"
    aliases=()
    keywords=('grandpa',)
    def build(self):
        self.path('dome',(8,20),[('A',(24,4),16,16,True),('A',(40,20),16,16,True)])
        for n,l in [('left',8),('right',28)]:
            self.add_polyline('glasses-'+n,(l,20),(l+12,20),(l+12,24),(l+12,28),(l+6,28),(l,28),(l,20),closed=True)
            self.relate('connect','dome','glasses-'+n)
        self.add_line('bridge',(20,24),(28,24));self.relate('connect','bridge','glasses-left');self.relate('connect','bridge','glasses-right')
        self.path('jaw',(14,28),[('A',(24,38),10,10,False),('A',(34,28),10,10,False)])
        self.relate('connect','jaw','glasses-left');self.relate('connect','jaw','glasses-right')
        self.path('body',(8,44),[('A',(24,42),16,2,True),('A',(40,44),16,2,True)])
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
