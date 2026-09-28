"""Outlined upward arrow and paired tail dashes; symmetric x=24; bounds (8,4)-(40,44).
Construction reference: No useful outlined dashed-arrow match; geometric arrow silhouette..
Reduction: One tail dash per side retains the broken shaft at 48px.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5443e1f9-f37f-4884-b268-88955bf863e3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/arrows/arrow dash up_5443e1f9-f37f-4884-b268-88955bf863e3.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-001/references/arrow dash up_5443e1f9-f37f-4884-b268-88955bf863e3.svg'
SAVED_BRIEF_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/arrows/arrow dash up_5443e1f9-f37f-4884-b268-88955bf863e3.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'upward-pointing-dashed-arrow-batch-001-r2'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('upward', 'pointing', 'dashed', 'arrow')
    def build(self):
        self.add_polyline('arrow',(16,30),(16,20),(8,20),(24,4),(40,20),(32,20),(32,30))
        for x in (16,32): self.add_line(f'tail-{x}',(x,38),(x,44))

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

