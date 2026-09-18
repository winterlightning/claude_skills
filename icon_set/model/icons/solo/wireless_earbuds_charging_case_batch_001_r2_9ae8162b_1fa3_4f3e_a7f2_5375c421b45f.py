"""Two circular earbud heads (centers 12,12 and 36,12; radius 6) with inward stems attach to a shared charging case rim. Bounds (6,6)-(42,42).
Construction reference: ear.
Reduction: Tiny speaker holes and lightning/status indicator omitted: the shallow case cannot contain a separate mark with 4-unit ink clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9ae8162b-1fa3-4f3e-a7f2-5375c421b45f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/audio/earpods charge_9ae8162b-1fa3-4f3e-a7f2-5375c421b45f.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-001/references/earpods charge_9ae8162b-1fa3-4f3e-a7f2-5375c421b45f.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'wireless-earbuds-charging-case-batch-001-r2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/audio'
    aliases = ()
    keywords = ('wireless', 'earbuds', 'charging', 'case')
    def build(self):
        # A shared rounded case supports two circular speaker heads on inward stems.
        self.add_polyline('rim',(6,28),(18,28),(30,28),(42,28))
        self.add_line('case-right',(42,28),(42,32))
        self.add_arc('bottom-right',(42,32),(32,42),radius_x=10)
        self.add_line('bottom',(32,42),(16,42))
        self.add_arc('bottom-left',(16,42),(6,32),radius_x=10)
        self.add_line('case-left',(6,32),(6,28))
        self.add_contour('case-body','case-right','bottom-right','bottom','bottom-left','case-left')
        self.relate('connect','rim','case-body')
        for side in (-1,1):
            cx=24+side*12
            x=24+side*6
            pre='earbud-'+str(side)
            self.circle(pre,cx,12,6)
            self.add_line(pre+'-stem',(x,12),(x,28))
            self.relate('connect',pre,pre+'-stem')
            self.relate('connect',pre+'-stem','rim')

    def rect(self, name, l, t, r, b, radius=4, top=(), bottom=()):
        # One rounded rectangle owns matching corner radii and attachment nodes.
        pts=[(l+radius,t),*[(x,t) for x in sorted(top)],(r-radius,t),(r,t+radius),(r,b-radius),(r-radius,b),*[(x,b) for x in sorted(bottom,reverse=True)],(l+radius,b),(l,b-radius),(l,t+radius)]
        members=[]
        for j,(p,q) in enumerate(zip(pts,pts[1:]+pts[:1])):
            n=f'{name}-{j}'; members.append(n)
            if p[0]!=q[0] and p[1]!=q[1]: self.add_arc(n,p,q,radius_x=radius)
            else: self.add_line(n,p,q)
        self.add_contour(name,*members,closed=True)

    def circle(self,name,x,y,r):
        self.add_arc(name+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-a',name+'-b',closed=True)

