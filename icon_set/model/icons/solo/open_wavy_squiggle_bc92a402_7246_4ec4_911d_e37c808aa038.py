"""Abstract Wavy Squiggle.

Plan: A single tall wave, three alternating turns; extremes 10,4–38,44. Quarter and half ellipses share horizontal tangents.
Construction reference: cable (local original and atomic-debug inspected).
Simplification: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc92a402-7246-4ec4-911d-e37c808aa038'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/path 1_bc92a402-7246-4ec4-911d-e37c808aa038.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'open-wavy-squiggle'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('abstract', 'wavy', 'squiggle')

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

        self.add_arc('upper',(24,4),(24,18),radius_x=14,radius_y=7,sweep=False)
        self.add_arc('middle',(24,18),(24,32),radius_x=14,radius_y=7,sweep=True)
        self.add_arc('lower',(24,32),(10,44),radius_x=14,radius_y=12,sweep=False)
        self.add_contour('wave','upper','middle','lower')
