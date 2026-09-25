"""Fire engine with raised ladder bed, sloping cab, beacon and paired round wheels.
Keyshape HRECT_L: exact SOLO48 centerline envelope, chosen for subject proportions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1097acb8-838c-4373-b993-78bf0d6c4312'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/fire engine_1097acb8-838c-4373-b993-78bf0d6c4312.svg'
AUTHOR = 'gpt-6'
class Batch045Icon9(Solo48):
    icon_id = 'fire-engine-with-roof-beacon-batch-045'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('truck', 'fire', 'engine', 'ladder', 'emergency', 'vehicle', 'beacon')
    # Reference: truck: cab/body hierarchy and paired wheel baseline.
    # Reduction: Dropped cab window; ladder and beacon retained.
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

        path('body',(12,36),('L',(4,36)),('L',(4,22)),('L',(28,22)),('L',(28,16)),('L',(36,16)),('L',(44,28)),('L',(44,36)),('L',(36,36)))
        self.add_line('axle',(20,36),(28,36))
        for x in (16,32):
            circle(f'wheel-{x}',x,36,4)
            self.relate('connect','body',f'wheel-{x}')
            self.relate('connect','axle',f'wheel-{x}')
        self.add_polyline('ladder',(4,22),(4,10),(20,10),(20,22))
        self.add_line('rung',(12,10),(12,22))
        self.relate('connect','ladder','body'); self.relate('connect','rung','ladder');self.relate('connect','rung','body')
        self.add_line('beacon',(32,16),(32,8));self.relate('connect','beacon','body')
