"""Rounded frame with sidebar and two stacked right content cells; shared divider x=24; exact bounds (6,6)-(42,42).
Construction reference: panel-left.
Reduction: Content tiles share the panel edges so both remain legible; menu strokes become dots.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1b1a16b4-9e7f-486d-9436-8970f83666d9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/apps/categorization list_1b1a16b4-9e7f-486d-9436-8970f83666d9.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-001/references/categorization list_1b1a16b4-9e7f-486d-9436-8970f83666d9.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'categorized-sidebar-layout-batch-001-r2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'apps'
    categories = ('apps', 'primitives')
    aliases = ()
    keywords = ('categorized', 'sidebar', 'layout')
    def build(self):
        self.rect('frame',6,6,42,42,4,top=(24,),bottom=(24,))
        self.add_polyline('divider',(24,6),(24,24),(24,42)); self.relate('connect','divider','frame')
        # Split the frame's right wall at the content-cell junction.
        # Two inset content tiles fit without an enclosing outer right wall.
        self.add_line('tile-divider',(24,24),(42,24))
        self.relate('connect','tile-divider','divider')
        self.relate('connect','tile-divider','frame')
        for j,y in enumerate((18,30)): self.add_dot(f'menu-{j}',(15,y))

    def rect(self, name, l, t, r, b, radius=4, top=(), bottom=()):
        # One rounded rectangle owns matching corner radii and attachment nodes.
        pts=[(l+radius,t),*[(x,t) for x in sorted(top)],(r-radius,t),(r,t+radius),(r,b-radius),(r-radius,b),*[(x,b) for x in sorted(bottom,reverse=True)],(l+radius,b),(l,b-radius),(l,t+radius)]
        members=[]
        for j,(p,q) in enumerate(zip(pts,pts[1:]+pts[:1])):
            n=f'{name}-{j}'; members.append(n)
            if p[0]!=q[0] and p[1]!=q[1]: self.add_arc(n,p,q,radius_x=radius)
            elif name=='frame' and p==(r,t+radius) and q==(r,b-radius):
                self.add_line(n,p,(r,24)); self.add_line(n+'-split',(r,24),q); members.append(n+'-split')
            else: self.add_line(n,p,q)
        self.add_contour(name,*members,closed=True)

    def circle(self,name,x,y,r):
        self.add_arc(name+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-a',name+'-b',closed=True)

