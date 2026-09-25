"""Concentric elliptical bridge arches over two shallow waves. Shared center x=24; horizontal radii 20 and 10.
Keyshape HRECT_L: exact SOLO48 centerline envelope, chosen for subject proportions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '20f585a9-bcee-488a-89f8-f8604d84d722'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/ford_20f585a9-bcee-488a-89f8-f8604d84d722.svg'
AUTHOR = 'gpt-6'
class Batch045Icon1(Solo48):
    icon_id = 'arch-bridge-above-water-batch-045'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('bridge', 'arch', 'water', 'waves', 'span', 'crossing', 'structure')
    # Reference: No close subject match; own concentric arch construction.
    # Reduction: Two shallow waves retained; arch flattened to preserve separation.
    # Bounds: (2, 6, 46, 42)
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

        path('bridge',(4,20),('A',(44,20),20,12,True),('L',(34,20)),('A',(14,20),10,4,False),('L',(4,20)),closed=True)
        for i,y in enumerate((30,39)):
            path(f'water-{i}',(4,y),('A',(14,y),5,1,False),('A',(24,y),5,1,True),('A',(34,y),5,1,False),('A',(44,y),5,1,True))
