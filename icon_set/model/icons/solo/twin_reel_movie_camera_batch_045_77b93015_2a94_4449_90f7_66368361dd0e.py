"""Twin reels above a camera body with flared right lens. Reels share radius and baseline.
Keyshape SQUARE: exact SOLO48 centerline envelope, chosen for subject proportions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '77b93015-2a94-4449-90f7-66368361dd0e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/filmmaker_77b93015-2a94-4449-90f7-66368361dd0e.svg'
AUTHOR = 'gpt-6'
class Batch045Icon2(Solo48):
    icon_id = 'twin-reel-movie-camera-batch-045'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('camera', 'movie', 'cinema', 'reels', 'lens', 'film', 'equipment')
    # Reference: video: rounded body and projecting lens; source provides twin reels.
    # Reduction: Dropped side inset; increased reels after visual review; detached flared lens preserves clearance.
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

        for x in (11,29): circle(f'reel-{x}',x,11,5)
        path('body',(6,28),('A',(10,24),4,4,True),('L',(24,24)),('L',(24,42)),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,28)),closed=True)
        self.add_polyline('lens',(42,24),(32,33),(42,42),closed=True)
