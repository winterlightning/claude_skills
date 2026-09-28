"""Extinguisher cylinder, top lever and flared horn; shoulder attaches valve at center.
Keyshape VRECT_L: exact SOLO48 centerline envelope, chosen for subject proportions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3f9582f0-2d09-40b4-9994-e281fa50f35f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/fire extinguisher_3f9582f0-2d09-40b4-9994-e281fa50f35f.svg'
AUTHOR = 'gpt-6'
class Batch045Icon6(Solo48):
    icon_id = 'fire-extinguisher-with-horn-nozzle-batch-045'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('fire', 'extinguisher', 'safety', 'emergency', 'cylinder', 'nozzle', 'equipment')
    # Reference: fire-extinguisher: domed bottle, valve and outlet hierarchy.
    # Reduction: Dropped secondary handle and cylinder seam; flared horn and raised valve preserve clearance.
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

        path('tank',(8,34),('A',(28,34),10,10,True),('L',(28,40)),('A',(24,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,34)),closed=True)
        self.add_line('valve',(18,24),(18,4))
        self.add_line('lever',(8,4),(24,4))
        self.add_polyline('horn',(40,4),(30,12),(40,20),closed=True)
        self.add_line('outlet',(18,12),(30,12))
        self.relate('connect','tank','valve')
        self.relate('connect','valve','lever')
        self.relate('connect','outlet','valve')
        self.relate('connect','outlet','horn')
