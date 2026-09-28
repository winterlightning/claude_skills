"""Mirrored rounded dome, paired antennae and two U-shaped feet; exact centerline bounds (8,4)-(40,44).
Construction reference: No useful mascot match; panel-left provides seam/outline construction..
Reduction: Blank face and body retained; no arms.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5a895be7-0613-57bb-9e1f-038063cbd8b8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/apps/android_5a895be7-0613-57bb-9e1f-038063cbd8b8.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-001/references/android_5a895be7-0613-57bb-9e1f-038063cbd8b8.svg'
SAVED_BRIEF_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/apps/android_5a895be7-0613-57bb-9e1f-038063cbd8b8.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'android-mascot-robot-icon-batch-001-r2'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface'
    aliases = ()
    keywords = ('android', 'mascot', 'robot', 'icon')
    def build(self):
        # Symmetric semicircular dome and simple rounded U feet share the body seam.
        self.add_arc('dome-left',(8,20),(20,8),radius_x=12)
        self.add_line('dome-top',(20,8),(28,8))
        self.add_arc('dome-right',(28,8),(40,20),radius_x=12)
        self.add_contour('dome','dome-left','dome-top','dome-right')
        for side,x,tip in [('left',20,16),('right',28,32)]:
            self.add_line('antenna-'+side,(x,8),(tip,4))
            self.relate('connect','antenna-'+side,'dome')
        pts=[(8,20),(8,32),(12,32),(12,40)]
        for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_line('body-'+str(j),a,b)
        self.add_arc('left-foot',(12,40),(20,40),radius_x=4,sweep=False)
        pts=[(20,40),(20,32),(28,32),(28,40)]
        for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_line('crotch-'+str(j),a,b)
        self.add_arc('right-foot',(28,40),(36,40),radius_x=4,sweep=False)
        pts=[(36,40),(36,32),(40,32),(40,20)]
        for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_line('right-body-'+str(j),a,b)
        self.add_contour('lower','body-0','body-1','body-2','left-foot','crotch-0','crotch-1','crotch-2','right-foot','right-body-0','right-body-1','right-body-2')
        self.add_line('seam',(8,20),(40,20)); self.relate('connect','dome','lower','seam')

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

