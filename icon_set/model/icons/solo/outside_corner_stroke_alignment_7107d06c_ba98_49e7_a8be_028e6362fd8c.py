"""Align Stroke to Outside Corner.

Plan: L-shaped outline with small corner-square straddling the inner junction. Envelope 6,6–42,42; corner square width8.
Construction reference: align-start-horizontal (local original and atomic-debug inspected).
Simplification: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7107d06c-ba98-49e7-a8be-028e6362fd8c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_02/align stroke to outside_7107d06c-ba98-49e7-a8be-028e6362fd8c.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'outside-corner-stroke-alignment'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('align', 'stroke', 'to', 'outside', 'corner')

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

        self.add_polyline('outer',(22,19),(22,6),(6,6),(6,42),(42,42),(42,24),(30,24))
        self.add_polyline('corner',(19,19),(22,19),(30,19),(30,24),(30,30),(19,30),closed=True)
        self.relate('connect','outer','corner')
