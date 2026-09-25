"""Agricultural Farm Plough.

Plan: A long slanted handle meets a broad curved plough beam above a connected pointed share; envelope 4,8–44,40.
Construction reference: wrench (local original and atomic-debug inspected).
Simplification: Handle meets the top of the enlarged curved beam; blade stays connected.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0ade6366-b7b9-4f77-94f0-db5a9e5e5b57'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/plough_0ade6366-b7b9-4f77-94f0-db5a9e5e5b57.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'curved-agricultural-plough'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('agricultural', 'farm', 'plough')

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

        self.add_polyline('handle',(4,8),(10,8),(36,16))
        self.add_arc('beam-outer',(20,32),(36,16),radius_x=16)
        self.add_arc('beam-tip',(36,16),(44,24),radius_x=8)
        self.add_line('beam-bottom',(44,24),(36,24))
        self.add_arc('shank-curve',(36,24),(30,30),radius_x=6,sweep=False)
        self.add_line('shank',(30,30),(30,32))
        self.add_contour('beam','beam-outer','beam-tip','beam-bottom','shank-curve','shank')
        self.add_polyline('share',(10,32),(20,32),(30,32),(38,40),(20,40),closed=True)
        self.relate('connect','handle','beam')
        self.relate('connect','beam','share')
