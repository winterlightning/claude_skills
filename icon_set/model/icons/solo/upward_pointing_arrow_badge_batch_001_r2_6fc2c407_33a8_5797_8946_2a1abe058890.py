"""Upright pointed badge with centered upward chevron; symmetric x=24; bounds (8,4)-(40,44).
Construction reference: square-chevron-up.
Reduction: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6fc2c407-33a8-5797-8946-2a1abe058890'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/arrows/arrow badge top_6fc2c407-33a8-5797-8946-2a1abe058890.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-001/references/arrow badge top_6fc2c407-33a8-5797-8946-2a1abe058890.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'upward-pointing-arrow-badge-batch-001-r2'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('upward', 'pointing', 'arrow', 'badge')
    def build(self):
        self.add_polyline('badge',(8,44),(8,20),(24,4),(40,20),(40,44),closed=True)
        self.add_polyline('chevron',(16,32),(24,24),(32,32))

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

