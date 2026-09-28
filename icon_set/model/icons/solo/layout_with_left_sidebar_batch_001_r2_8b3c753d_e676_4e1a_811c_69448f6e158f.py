"""Straight-sided panel with round stroke joins and three evenly spaced sidebar dots. Bounds (4,8)-(44,40).
Construction reference: panel-left.
Reduction: Short dashed divider reduced to three dots; corner arcs omitted to certify exact gaps.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8b3c753d-e676-4e1a-811c-69448f6e158f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/apps/sidebar dots left_8b3c753d-e676-4e1a-811c-69448f6e158f.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-001/references/sidebar dots left_8b3c753d-e676-4e1a-811c-69448f6e158f.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'layout-with-left-sidebar-batch-001-r2'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'apps'
    categories = ('apps', 'primitives')
    aliases = ()
    keywords = ('layout', 'with', 'left', 'sidebar')
    def build(self):
        self.add_polyline('frame',(4,8),(44,8),(44,40),(4,40),closed=True)
        for j,y in enumerate((16,24,32)): self.add_dot(f'divider-{j}',(18,y))

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

