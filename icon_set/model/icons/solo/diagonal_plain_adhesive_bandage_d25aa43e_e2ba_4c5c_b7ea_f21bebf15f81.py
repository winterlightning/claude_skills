"""Adhesive Bandage Strip.

Plan: Diagonal capsule with two transverse pad seams; endpoints and paired cap radii are shared. Envelope 6,6–42,42.
Construction reference: bandage (local original and atomic-debug inspected).
Simplification: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd25aa43e-e2ba-4c5c-b7ea-f21bebf15f81'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/plaster_d25aa43e-e2ba-4c5c-b7ea-f21bebf15f81.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'diagonal-plain-adhesive-bandage'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/medical'
    aliases = ()
    keywords = ('adhesive', 'bandage', 'strip')

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

        self.add_arc('cap-low',(22,40),(10,24),radius_x=10)
        self.add_line('side-left-a',(10,24),(14,20))
        self.add_line('side-left-b',(14,20),(22,12))
        self.add_line('side-left-c',(22,12),(26,8))
        self.add_arc('cap-high',(26,8),(38,24),radius_x=10)
        self.add_line('side-right-a',(38,24),(34,28))
        self.add_line('side-right-b',(34,28),(26,36))
        self.add_line('side-right-c',(26,36),(22,40))
        self.add_contour('outline','cap-low','side-left-a','side-left-b','side-left-c','cap-high','side-right-a','side-right-b','side-right-c',closed=True)
        for j,(a,b) in enumerate([((14,20),(26,36)),((22,12),(34,28))]):
            self.add_line(f'pad-seam-{j}',a,b)
            self.relate('connect','outline',f'pad-seam-{j}')
