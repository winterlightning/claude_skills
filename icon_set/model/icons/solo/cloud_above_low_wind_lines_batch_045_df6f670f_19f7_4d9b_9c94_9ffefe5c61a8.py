"""Broad cloud with one large crown and lower mist strokes; wind curl reduced to preserve air.
Keyshape HRECT_L: exact SOLO48 centerline envelope, chosen for subject proportions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'df6f670f-19f7-4d9b-9c94-9ffefe5c61a8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/fog_df6f670f-19f7-4d9b-9c94-9ffefe5c61a8.svg'
AUTHOR = 'gpt-6'
class Batch045Icon4(Solo48):
    icon_id = 'cloud-above-low-wind-lines-batch-045'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('cloud', 'fog', 'wind', 'mist', 'weather', 'air', 'sky')
    # Reference: cloud-fog: lobe hierarchy and separate fog strokes.
    # Reduction: Wind curl simplified to second mist stroke.
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

        path('cloud',(10,24),('A',(10,14),5,5,True),('A',(32,14),11,6,True),('L',(36,14)),('A',(36,24),8,5,True),('L',(10,24)),closed=True)
        self.add_line('mist',(4,32),(44,32))
        self.add_line('wind',(12,40),(36,40))
