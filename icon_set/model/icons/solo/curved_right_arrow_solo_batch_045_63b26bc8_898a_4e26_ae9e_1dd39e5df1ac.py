"""Quarter-circle turn and long right-pointing arrow; tail and head share junction.
Keyshape SQUARE: exact SOLO48 centerline envelope, chosen for subject proportions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '63b26bc8-898a-4e26-ae9e-1dd39e5df1ac'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/flick_63b26bc8-898a-4e26-ae9e-1dd39e5df1ac.svg'
AUTHOR = 'gpt-6'
class Batch045Icon5(Solo48):
    icon_id = 'curved-right-arrow-solo-batch-045'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('arrow', 'right', 'curved', 'forward', 'direction', 'turn', 'navigation')
    # Reference: undo-2: tangent quarter-turn and shared arrow junction.
    # Reduction: No defining feature removed.
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

        path('shaft',(6,42),('L',(6,36)),('A',(26,16),20,20,True),('L',(42,16)))
        self.add_polyline('head',(32,6),(42,16),(32,26))
        self.relate('connect','shaft','head')
