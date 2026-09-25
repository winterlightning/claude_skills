"""Paired hemispheres, central fissure and three rounded outer lobes each; axis x=24. Bounds (8,4)-(40,44).
Construction reference: brain.
Reduction: Minor inward folds omitted for clear hemispheres.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4cc51cde-8646-5c24-82c4-d7386922eb24'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/artificial-intelligence/brain_4cc51cde-8646-5c24-82c4-d7386922eb24.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-001/references/brain_4cc51cde-8646-5c24-82c4-d7386922eb24.svg'
SAVED_BRIEF_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/artificial-intelligence/brain_4cc51cde-8646-5c24-82c4-d7386922eb24.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'human-brain-hemispheres-batch-001-r2'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'artificial-intelligence'
    aliases = ()
    keywords = ('human', 'brain', 'hemispheres')
    def build(self):
        # Two mirrored lobed hemispheres; outer lobes reach x=8 and x=40.
        for side in (-1,1):
            def p(x,y): return (24+side*x,y)
            pre='left' if side<0 else 'right'
            self.add_arc(pre+'-top',p(0,12),p(12,12),radius_x=6,radius_y=8,sweep=side>0)
            self.add_arc(pre+'-middle',p(12,12),p(12,32),radius_x=4,radius_y=10,sweep=side>0)
            self.add_arc(pre+'-bottom',p(12,32),p(0,32),radius_x=6,radius_y=12,sweep=side>0)
            self.add_contour(pre,pre+'-top',pre+'-middle',pre+'-bottom')
        self.add_line('fissure',(24,12),(24,32))
        self.relate('connect','left','right','fissure')

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

