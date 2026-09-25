"""Skipping rope has a broad upper arch and lower U loop joining two upright handles.
Keyshape VRECT_L: exact SOLO48 centerline envelope, chosen for subject proportions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '604a15fb-4b8c-4dc1-a1c3-d58abbb9c0e9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/fitness jumping rope 3_604a15fb-4b8c-4dc1-a1c3-d58abbb9c0e9.svg'
AUTHOR = 'gpt-6'
class Batch045Icon12(Solo48):
    icon_id = 'jump-rope-with-two-handles-batch-045'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('rope', 'jump', 'skipping', 'fitness', 'exercise', 'handles', 'sport')
    # Reference: No useful local rope match; repeated capsule handles and continuous rope.
    # Reduction: Dropped transverse seams; two capsule handles retained.
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

        path('rope',(12,28),('L',(12,16)),('A',(24,16),6,12,True),('L',(24,35)),('A',(36,35),6,9,False),('L',(36,20)))
        path('left-handle',(8,32),('A',(16,32),4,4,True),('L',(16,40)),('A',(8,40),4,4,True),('L',(8,32)),closed=True)
        path('right-handle',(32,8),('A',(40,8),4,4,True),('L',(40,16)),('A',(32,16),4,4,True),('L',(32,8)),closed=True)
        self.relate('connect','rope','left-handle');self.relate('connect','rope','right-handle')
