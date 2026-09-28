"""Left sidebar panel with three repeated navigation strokes and shared divider x=22. Bounds (4,8)-(44,40).
Construction reference: panel-left.
Reduction: Corner arcs omitted to certify exact navigation clearances.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '779a7169-b4d5-52a9-a799-2ce7e82c5026'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/apps/sidebar line left_779a7169-b4d5-52a9-a799-2ce7e82c5026.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-001/references/sidebar line left_779a7169-b4d5-52a9-a799-2ce7e82c5026.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'left-sidebar-navigation-layout-batch-001-r2'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'apps'
    categories = ('apps', 'primitives')
    aliases = ()
    keywords = ('left', 'sidebar', 'navigation', 'layout')
    def build(self):
        x=22
        self.add_polyline('frame',(4,8),(x,8),(44,8),(44,40),(x,40),(4,40),closed=True)
        self.add_line('divider',(x,8),(x,40)); self.relate('connect','divider','frame')
        for j,y in enumerate((16,24,32)):
            self.add_line(f'menu-{j}',(12,y),(14,y))

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

