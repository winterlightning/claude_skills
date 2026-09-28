"""Left-facing skeleton with curved head, straight spine, two repeated ribs and flared tail.
Keyshape HRECT_M: exact SOLO48 centerline envelope, chosen for subject proportions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bf61ecc2-03d2-41b3-b000-f2bc244b2351'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/fishbone_bf61ecc2-03d2-41b3-b000-f2bc244b2351.svg'
AUTHOR = 'gpt-6'
class Batch045Icon11(Solo48):
    icon_id = 'fish-skeleton-batch-045'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('fish', 'skeleton', 'bone', 'spine', 'ribs', 'tail', 'animal')
    # Reference: fish: head/spine/tail hierarchy, reduced to skeleton.
    # Reduction: Two ribs and open flared tail retained; omitted eye.
    # Bounds: (2, 8, 46, 40)
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

        path('head',(16,10),('A',(4,24),20,20,False),('A',(16,38),20,20,False),('L',(16,24)),('L',(16,10)),closed=True)
        self.add_line('spine',(16,24),(42,24));self.relate('connect','head','spine')
        for x in (24,24+9):
            self.add_polyline(f'rib-{x}',(x+2,12),(x,24),(x+2,36));self.relate('connect','spine',f'rib-{x}')
        self.add_polyline('tail',(44,10),(42,24),(44,38));self.relate('connect','tail','spine')
