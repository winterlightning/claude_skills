"""Right-facing fish below a hanging hook. Fish lens and forked tail; water and float removed.
Keyshape SQUARE: exact SOLO48 centerline envelope, chosen for subject proportions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7a16b0c8-f6dd-4867-a6ce-f19d89d9e971'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/fishing hook fish 1_7a16b0c8-f6dd-4867-a6ce-f19d89d9e971.svg'
AUTHOR = 'gpt-6'
class Batch045Icon10(Solo48):
    icon_id = 'fish-beneath-fishing-hook-batch-045'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('fish', 'fishing', 'hook', 'line', 'float', 'water', 'angling')
    # Reference: fish: closed lens body and attached forked tail.
    # Reduction: Dropped float, water strokes and eye; fish and hook retained.
    # Bounds: (4, 4, 44, 44)
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

        path('hook',(36,6),('L',(36,14)),('A',(24,14),6,6,True))
        path('fish',(16,34),('A',(42,34),16,10,True),('A',(16,34),16,10,True),closed=True)
        self.add_polyline('tail',(16,34),(6,26),(6,42),(16,34))
        self.relate('connect','fish','tail')
