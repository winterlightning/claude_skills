"""Alchemical Symbol for Silica.

Plan: One upright triangle over a mirrored pair of circles; extrema 6,6–42,42. Circle radius6, center spacing24.
Construction reference: triangle, circle (local original and atomic-debug inspected).
Simplification: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5afbf3b8-cc49-4e47-9558-556ab12d8408'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/silica_5afbf3b8-cc49-4e47-9558-556ab12d8408.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'triangle-above-two-circles'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('alchemical', 'symbol', 'for', 'silica')

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

        self.add_polyline('triangle',(24,6),(14,21),(34,21),closed=True)
        for name,x in [('circle-left',12),('circle-right',36)]: circle(name,x,36,6)
