"""Flamingo with hooked beak, S neck, pointed body and one straight supporting leg.
Keyshape VRECT_L: exact SOLO48 centerline envelope, chosen for subject proportions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '81d15e2a-dffb-4f68-873c-f118f99d99a6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/flamingo_81d15e2a-dffb-4f68-873c-f118f99d99a6.svg'
AUTHOR = 'gpt-6'
class Batch045Icon13(Solo48):
    icon_id = 'flamingo-on-one-leg-batch-045'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('flamingo', 'bird', 'leg', 'beak', 'neck', 'wading', 'animal')
    # Reference: No useful local flamingo match; source establishes curved neck and raised body.
    # Reduction: Dropped raised bent leg and eye; one supporting leg retained.
    # Bounds: (6, 2, 42, 46)
    def build(self):
        def path(name, start, *steps, closed=False):
            members=[]; p=start
            for i,step in enumerate(steps):
                q=step[1]
                if p == q: continue
                member=f"{name}-{i}"
                if step[0]=='L': self.add_line(member,p,q)
                else: self.add_arc(member,p,q,radius_x=step[2],radius_y=step[3],sweep=step[4])
                members.append(member); p=q
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True),closed=True)

        path('neck',(8,12),('A',(20,12),6,8,True),('L',(12,24)),('A',(24,30),12,6,False))
        path('body',(24,30),('A',(40,24),12,8,False),('L',(36,18)),('A',(24,30),12,8,False),closed=True)
        self.add_polyline('beak',(8,12),(8,15))
        self.relate('connect','neck','beak');self.relate('connect','neck','body')
        self.add_polyline('leg',(28,30),(28,44),(22,44));self.relate('connect','leg','body')
