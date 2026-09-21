"""Adjustable C-Clamp Tool.

Plan: Left-opening C frame with central screw and cross handle; envelope 8,4–40,44. Frame wall thickness 8; screw has two true T junctions.
Construction reference: wrench (local original and atomic-debug inspected).
Simplification: Thread ridges and doubled handle outline removed to keep the screw legible.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '27d4aaa8-b81d-43f6-9c9d-037843e2726b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/c clamp_27d4aaa8-b81d-43f6-9c9d-037843e2726b.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'c-clamp-with-screw-handle'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/tools'
    aliases = ()
    keywords = ('adjustable', 'c-clamp', 'tool')

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

        self.add_polyline('frame',(12,4),(36,4),(40,8),(40,32),(36,36),(16,36),(8,36),(8,28),(16,28),(30,28),(30,12),(12,12),closed=True)
        self.add_polyline('pressure',(8,20),(16,20),(24,20))
        self.add_polyline('screw',(16,20),(16,28),(16,36),(16,44))
        self.add_polyline('handle',(8,44),(16,44),(26,44))
        self.relate('connect','pressure','screw')
        self.relate('connect','screw','frame')
        self.relate('connect','screw','handle')
