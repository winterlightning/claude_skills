"""Active Person Running Fast.

Plan: Running stick figure with bent limbs; head (29,9), radius5, neck (24,21) gives exact 13−5−4=4 ink gap. Deliberate running lean; extrema 8,4–40,44.
Construction reference: human_ref/full_body_ref.png (local original and atomic-debug inspected).
Simplification: Outline limbs reduced to the shared single-stroke human vocabulary.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '361bd1bd-a5a8-4b2b-bd6f-94ac528417cb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/person running_361bd1bd-a5a8-4b2b-bd6f-94ac528417cb.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'running-person-bent-arms'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('active', 'person', 'running', 'fast')

    def build(self):
        def circle(name, x, y, r):
            self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
            self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)

        def rect(name, left, top, right, bottom, r=2):
            pts=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),(right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
            members=[]
            for j,a in enumerate(pts):
                b=pts[(j+1)%8]; eid=f'{name}-{j}'; members.append(eid)
                if j%2: self.add_arc(eid,a,b,radius_x=r)
                else: self.add_line(eid,a,b)
            self.add_contour(name,*members,closed=True)

        circle('head',29,9,5)
        self.add_line('torso',(24,21),(19,33))
        self.add_polyline('back-arm',(24,21),(15,21),(10,28))
        self.add_polyline('front-arm',(24,21),(32,28),(40,24))
        self.add_polyline('rear-leg',(19,33),(15,39),(8,40))
        self.add_polyline('front-leg',(19,33),(29,37),(26,44))
        for part in ('back-arm','front-arm','rear-leg','front-leg'): self.relate('connect','torso',part)
        self.relate('connect','back-arm','front-arm')
        self.relate('connect','rear-leg','front-leg')
        self.mark_human_figure('runner',head='head',torso='torso',torso_junction='start')
