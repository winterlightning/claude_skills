"""Hand enters from upper right and grips card. Portrait head center (16,24), radius 2; shoulders y=34. Bounds (6,6)-(42,42).
Construction reference: hand; shared human_ref/user.svg.
Reduction: Shoulders reduced to one short line; exact detached-head ink gap 34-(24+2)-4=4.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cb16642c-e584-52b6-ae9d-bff1579af112'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/apps/digital policies data breach user_cb16642c-e584-52b6-ae9d-bff1579af112.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-001/references/digital policies data breach user_cb16642c-e584-52b6-ae9d-bff1579af112.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'hand-holding-identity-card-batch-001-r2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'apps'
    aliases = ()
    keywords = ('hand', 'holding', 'identity', 'card')
    def build(self):
        self.add_polyline('card',(24,14),(16,14),(6,14),(6,42),(32,42),(32,28))
        self.add_polyline('hand-top',(16,14),(22,6),(34,6),(42,6))
        self.relate('connect','hand-top','card')
        self.add_polyline('thumb',(34,14),(26,22),(32,28),(42,18))
        self.relate('connect','thumb','card')
        self.circle('head',16,24,2)
        # Head bottom 26 -> shoulders 34: 8 centerline, exactly 4 visible units.
        self.add_line('shoulders',(14,34),(22,34))

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

