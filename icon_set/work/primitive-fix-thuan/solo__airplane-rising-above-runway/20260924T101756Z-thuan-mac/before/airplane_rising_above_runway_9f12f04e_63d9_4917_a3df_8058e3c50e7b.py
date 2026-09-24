"""Airplane Taking Off.

Plan: Ascending aircraft above a detached runway; envelope 4,8–44,40. Broad upper wing and fuselage retain the takeoff direction.
Construction reference: plane (local original and atomic-debug inspected).
Simplification: Wings widened; short lower wing and detached runway retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9f12f04e-63d9-4917-a3df-8058e3c50e7b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/plane arrival_9f12f04e-63d9-4917-a3df-8058e3c50e7b.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'airplane-rising-above-runway'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/transportation'
    aliases = ()
    keywords = ('airplane', 'taking', 'off')

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

        self.add_line('upper-1',(4, 22),(10, 22))
        self.add_line('upper-2',(10, 22),(20, 17))
        self.add_line('upper-3',(20, 17),(8, 8))
        self.add_line('upper-4',(8, 8),(22, 8))
        self.add_line('upper-5',(22, 8),(34, 17))
        self.add_line('upper-6',(34, 17),(36, 13))
        self.add_arc('nose',(36,13),(42,21),radius_x=5)
        self.add_line('lower-1',(42, 21),(30, 27))
        self.add_line('lower-2',(30, 27),(26, 31))
        self.add_line('lower-3',(26, 31),(20, 31))
        self.add_line('lower-4',(20, 31),(21, 27))
        self.add_line('lower-5',(21, 27),(12, 31))
        self.add_line('lower-6',(12, 31),(8, 30))
        self.add_line('lower-7',(8, 30),(4, 22))
        self.add_contour('plane',*(f'upper-{j}' for j in range(1,7)),'nose',*(f'lower-{j}' for j in range(1,8)),closed=True)
        self.add_line('runway',(4,40),(44,40))
