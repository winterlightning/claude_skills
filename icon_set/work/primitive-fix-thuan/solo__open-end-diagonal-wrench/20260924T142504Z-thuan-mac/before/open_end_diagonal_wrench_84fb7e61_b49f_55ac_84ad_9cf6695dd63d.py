"""Maintenance and Repair Wrench.

Plan: One continuous open-jaw wrench silhouette; square extrema 6,6–42,42. Rounded cap and circular head; deliberate diagonal handle.
Construction reference: wrench (local original and atomic-debug inspected).
Simplification: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '84fb7e61-b49f-55ac-84ad-9cf6695dd63d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/tools/tools wrench_84fb7e61-b49f-55ac-84ad-9cf6695dd63d.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'open-end-diagonal-wrench'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/tools'
    aliases = ()
    keywords = ('maintenance', 'and', 'repair', 'wrench')

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

        self.add_line('jaw-a',(30,6),(22,14))
        self.add_line('jaw-b',(22,14),(30,22))
        self.add_line('jaw-c',(30,22),(42,10))
        self.add_line('jaw-tip',(42,10),(42,18))
        self.add_arc('head-right',(42,18),(30,30),radius_x=12)
        self.add_line('handle-right',(30,30),(14,41))
        self.add_arc('handle-end',(14,41),(8,33),radius_x=5)
        self.add_line('handle-left',(8,33),(18,18))
        self.add_arc('head-left',(18,18),(30,6),radius_x=12)
        self.add_contour('outline','jaw-a','jaw-b','jaw-c','jaw-tip','head-right','handle-right','handle-end','handle-left','head-left',closed=True)
