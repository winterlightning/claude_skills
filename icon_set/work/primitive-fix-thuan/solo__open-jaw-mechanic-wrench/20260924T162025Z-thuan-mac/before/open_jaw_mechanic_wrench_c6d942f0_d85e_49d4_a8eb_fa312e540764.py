"""Adjustable Mechanic Wrench Tool.

Plan: Continuous diagonal wrench silhouette; widened upper crescent and side-facing angular jaw. Square extrema 6,6–42,42.
Construction reference: wrench (local original and atomic-debug inspected).
Simplification: Jaw widened to keep its opening visible.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c6d942f0-d85e-49d4-a8eb-fa312e540764'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/pipe wrench_c6d942f0-d85e-49d4-a8eb-fa312e540764.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'open-jaw-mechanic-wrench'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/tools'
    aliases = ()
    keywords = ('adjustable', 'mechanic', 'wrench', 'tool')

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

        self.add_arc('head-upper',(18,18),(30,6),radius_x=12)
        self.add_arc('head-tip',(30,6),(42,18),radius_x=12)
        self.add_line('jaw-1',(42, 18),(32, 16))
        self.add_line('jaw-2',(32, 16),(26, 22))
        self.add_line('jaw-3',(26, 22),(38, 30))
        self.add_arc('head-lower',(38,30),(28,30),radius_x=10)
        self.add_line('handle-right',(28,30),(14,41))
        self.add_arc('cap',(14,41),(8,33),radius_x=5)
        self.add_line('handle-left',(8,33),(18,18))
        self.add_contour('outline','head-upper','head-tip','jaw-1','jaw-2','jaw-3','head-lower','handle-right','cap','handle-left',closed=True)
