"""Three horizontal screen bands over an attached pull tab. Bounds (6,6)-(42,42).
Construction reference: panel-left.
Reduction: Dropped tiny drawer chevron because the tab cannot fit it with required clearances.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b791a328-23eb-4943-b1f0-55d32115fef6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/apps/ui screen split_b791a328-23eb-4943-b1f0-55d32115fef6.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-001/references/ui screen split_b791a328-23eb-4943-b1f0-55d32115fef6.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'triple-horizontal-screen-split-batch-001-r2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'apps'
    aliases = ()
    keywords = ('triple', 'horizontal', 'screen', 'split')
    def build(self):
        self.add_polyline('screen',(6,6),(42,6),(42,14),(42,22),(42,30),(32,30),(16,30),(6,30),(6,22),(6,14),closed=True)
        for j,y in enumerate((14,22)):
            self.add_line(f'band-{j}',(6,y),(42,y)); self.relate('connect',f'band-{j}','screen')
        self.add_polyline('drawer',(16,30),(16,42),(32,42),(32,30)); self.relate('connect','drawer','screen')

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

