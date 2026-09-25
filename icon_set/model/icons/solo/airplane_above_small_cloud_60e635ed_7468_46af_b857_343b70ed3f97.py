"""Airplane Flying Above Cloud.

Plan: Right-facing aircraft and a detached two-lobed cloud; square extrema 6,6–42,42. Swept wings and fuselage are widened for clearance.
Construction reference: plane (local original and atomic-debug inspected).
Simplification: Cloud and tail reduced; both swept wings and the separate cloud retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '60e635ed-7468-46af-b857-343b70ed3f97'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/plane trip cloud_60e635ed-7468-46af-b857-343b70ed3f97.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'airplane-above-small-cloud'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('airplane', 'flying', 'above', 'cloud')

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

        self.add_line('plane-1',(6, 10),(10, 14))
        self.add_line('plane-2',(10, 14),(24, 14))
        self.add_line('plane-3',(24, 14),(16, 6))
        self.add_line('plane-4',(16, 6),(30, 6))
        self.add_line('plane-5',(30, 6),(38, 14))
        self.add_line('underside-1',(38, 22),(30, 22))
        self.add_line('underside-2',(30, 22),(22, 32))
        self.add_line('underside-3',(22, 32),(14, 32))
        self.add_line('underside-4',(14, 32),(18, 22))
        self.add_line('underside-5',(18, 22),(10, 22))
        self.add_line('underside-6',(10, 22),(6, 10))
        self.add_arc('nose',(38,14),(38,22),radius_x=4)
        self.add_contour('aircraft',*(f'plane-{j}' for j in range(1,6)),'nose',*(f'underside-{j}' for j in range(1,7)),closed=True)
        self.add_arc('cloud-left',(32,42),(32,36),radius_x=3)
        self.add_arc('cloud-top',(32,36),(38,36),radius_x=3)
        self.add_arc('cloud-right',(38,36),(38,42),radius_x=3)
        self.add_line('cloud-base',(38,42),(32,42))
        self.add_contour('cloud','cloud-left','cloud-top','cloud-right','cloud-base',closed=True)
