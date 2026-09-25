"""Right fist over rising forearm with broad rounded elbow and bicep bulge; details minimized.
Keyshape SQUARE: exact SOLO48 centerline envelope, chosen for subject proportions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '797f6b01-5eb2-4d71-88e6-cfb04c38ea5d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/forelimb_797f6b01-5eb2-4d71-88e6-cfb04c38ea5d.svg'
AUTHOR = 'gpt-6'
class Batch045Icon14(Solo48):
    icon_id = 'flexed-arm-with-right-fist-batch-045'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('arm', 'muscle', 'bicep', 'flex', 'fist', 'strength', 'body')
    # Reference: biceps-flexed: fist, forearm and bicep silhouette. Human full_body_ref.png inspected for continuous rounded limb vocabulary.
    # Reduction: Dropped interior muscle creases; continuous flexed arm with fist and bicep retained.
    # Bounds: (4, 4, 44, 44)
    # Isolated arm: no head/torso or detached-head measurement applies.
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

        path('arm',(6,30),('A',(24,30),9,10,True),('L',(26,14)),('A',(32,6),6,8,True),('L',(36,6)),('A',(42,12),6,6,True),('A',(36,18),6,6,True),('L',(34,18)),('L',(42,34)),('A',(34,42),8,8,True),('L',(18,42)),('A',(6,30),12,12,True),closed=True)
